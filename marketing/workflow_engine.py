"""Multi-Agent Sequential Workflow & Team Orchestration Engine.

Manages multi-step team workflows where complex goals are broken down,
executed sequentially by specialized AI agents with task handoffs, and routed
into the approval queue when sensitive/outbound actions are created.
"""

from typing import List, Dict, Any, Optional

from . import agent_engine, rag_engine
from .models import (AIAgent, ApprovalRequest, MultiAgentWorkflow, WorkflowStep)


PRESET_WORKFLOWS = {
    'campaign_launch': {
        'title': 'Q3 Enterprise Campaign Launch',
        'objective': 'Conduct market research, draft social media announcements, and prepare email outreach.',
        'steps': [
            {
                'agent_type': 'research',
                'role_name': 'Market Research & Intelligence',
                'prompt': 'Analyze current market trends for enterprise SaaS automation and summarize top 3 buying signals.',
            },
            {
                'agent_type': 'content',
                'role_name': 'Social Content Generation',
                'prompt': 'Based on the research findings above, draft a high-converting LinkedIn post announcing our solution.',
            },
            {
                'agent_type': 'outreach',
                'role_name': 'Outreach Email Preparation',
                'prompt': 'Draft a personalized outreach email to target SaaS VPs of Marketing based on the campaign theme.',
                'requires_approval': True,
                'item_type': 'email',
            },
        ]
    },
    'hr_onboarding': {
        'title': 'Employee Onboarding & Technical Setup',
        'objective': 'Prepare HR onboarding itinerary, technical environment setup, and welcome communications.',
        'steps': [
            {
                'agent_type': 'hr',
                'role_name': 'HR Screening & Orientation',
                'prompt': 'Draft a comprehensive first-week orientation schedule and welcome checklist for a new team member.',
            },
            {
                'agent_type': 'developer',
                'role_name': 'Dev Environment Setup',
                'prompt': 'Generate a technical repository setup and workstation configuration guide for the new developer.',
            },
            {
                'agent_type': 'outreach',
                'role_name': 'Welcome Email Delivery',
                'prompt': 'Draft the formal welcome email to send to the new employee with orientation details.',
                'requires_approval': True,
                'item_type': 'email',
            },
        ]
    },
    'product_release': {
        'title': 'Product Release & Standup Coordination',
        'objective': 'Synthesize sprint deliverables, generate release notes, and draft social release announcement.',
        'steps': [
            {
                'agent_type': 'eng_mgr',
                'role_name': 'Sprint & Deliverables Triage',
                'prompt': 'Summarize completed sprint backlog items and identify major release highlights.',
            },
            {
                'agent_type': 'research',
                'role_name': 'Release Impact Analysis',
                'prompt': 'Evaluate product release impact against competitor features and highlight key customer benefits.',
            },
            {
                'agent_type': 'content',
                'role_name': 'Product Announcement Post',
                'prompt': 'Draft a product launch social media update detailing the new capabilities.',
                'requires_approval': True,
                'item_type': 'social_post',
            },
        ]
    }
}


def create_preset_workflow(user, preset_key: str) -> Optional[MultiAgentWorkflow]:
    """Create a MultiAgentWorkflow and its WorkflowStep instances from a preset definition."""
    preset = PRESET_WORKFLOWS.get(preset_key)
    if not preset:
        return None

    workflow = MultiAgentWorkflow.objects.create(
        user=user,
        title=preset['title'],
        objective=preset['objective'],
        status='pending',
    )

    agents = {agent.agent_type: agent for agent in AIAgent.objects.filter(user=user)}

    for idx, s_data in enumerate(preset['steps'], start=1):
        agent = agents.get(s_data['agent_type'])
        if not agent:
            # Fallback to any active agent if type not found
            agent = AIAgent.objects.first()

        WorkflowStep.objects.create(
            workflow=workflow,
            agent=agent,
            step_order=idx,
            role_name=s_data['role_name'],
            input_prompt=s_data['prompt'],
            status='pending',
        )

    return workflow


def run_workflow_step(step: WorkflowStep) -> str:
    """Execute one workflow step using its assigned agent, carrying over prior step context."""
    step.status = 'in_progress'
    step.save(update_fields=['status'])

    # Gather outputs from previous steps as context handoff
    prev_steps = step.workflow.steps.filter(step_order__lt=step.step_order, status='completed')
    context_handoff = ""
    if prev_steps.exists():
        handoffs = [f"--- STEP {s.step_order} ({s.agent.name} - {s.role_name}) ---\n{s.output_text}" for s in prev_steps]
        context_handoff = "\n\n[CONTEXT FROM PRECEDING STEPS]:\n" + "\n\n".join(handoffs) + "\n\n"

    full_prompt = f"{step.input_prompt}{context_handoff}"

    # Use start_conversation or fallback generation engine directly
    temp_conv = agent_engine.start_conversation(
        step.workflow.user or step.agent.user,
        step.agent,
        title=f"Workflow Step {step.step_order}: {step.role_name}"
    )

    _user_msg, assistant_msg = agent_engine.send_message(temp_conv, full_prompt)
    output = assistant_msg.content

    step.output_text = output

    # Check if this step produces an approval request
    preset_key = None
    for k, v in PRESET_WORKFLOWS.items():
        if v['title'] == step.workflow.title:
            preset_key = k
            break

    if preset_key:
        step_defs = PRESET_WORKFLOWS[preset_key]['steps']
        if step.step_order <= len(step_defs):
            s_def = step_defs[step.step_order - 1]
            if s_def.get('requires_approval'):
                item_type = s_def.get('item_type', 'insight')
                recipient_email = 'team@example.com' if item_type == 'email' else ''
                approval = agent_engine.submit_message_for_approval(
                    assistant_msg,
                    item_type=item_type,
                    title=f"[{step.workflow.title}] {step.role_name}",
                    recipient_email=recipient_email,
                )
                step.approval_request = approval
                step.status = 'awaiting_approval'
                step.save(update_fields=['output_text', 'status', 'approval_request'])
                return output

    step.status = 'completed'
    step.save(update_fields=['output_text', 'status'])
    return output


def run_full_workflow(workflow: MultiAgentWorkflow) -> MultiAgentWorkflow:
    """Execute all steps in a multi-agent workflow sequentially."""
    workflow.status = 'in_progress'
    workflow.save(update_fields=['status'])

    pending_steps = workflow.steps.filter(status='pending').order_by('step_order')

    for step in pending_steps:
        run_workflow_step(step)
        if step.status == 'awaiting_approval':
            # Pause workflow execution until approval is reviewed
            workflow.status = 'in_progress'
            workflow.save(update_fields=['status'])
            return workflow

    # If all steps finished
    if not workflow.steps.exclude(status='completed').exists():
        workflow.status = 'completed'
    workflow.save(update_fields=['status'])

    return workflow
