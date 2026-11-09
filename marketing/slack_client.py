"""Slack Communication Tool Client for Engineering Manager (Marcus) and Team Notifications."""

import datetime
from typing import Dict, Any


def post_channel_message(channel: str, message: str) -> Dict[str, Any]:
    """Format and simulate posting a formatted message to a Slack channel."""
    msg_id = f"msg_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    channel_name = channel if channel.startswith('#') else f"#{channel}"
    
    return {
        'status': 'sent',
        'message_id': msg_id,
        'channel': channel_name,
        'message_preview': message[:150],
        'posted_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }


def post_standup_summary(sprint_name: str, completed_tasks: list, blockers: list) -> Dict[str, Any]:
    """Generate and post a structured sprint standup summary to #engineering."""
    blocker_str = "\n".join([f"- ⚠️ {b}" for b in blockers]) if blockers else "None"
    task_str = "\n".join([f"- ✅ {t}" for t in completed_tasks]) if completed_tasks else "- None"
    
    body = (
        f"*Daily Standup Summary - {sprint_name}*\n\n"
        f"*Completed Today:*\n{task_str}\n\n"
        f"*Blockers / Attention Required:*\n{blocker_str}\n"
    )
    
    return post_channel_message('#engineering-standup', body)
