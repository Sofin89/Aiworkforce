# AI Workforce — Project Documentation

---

## COVER PAGE

---

<div align="center">

### UNIVERSITY NAME
*GLS University*

### DEPARTMENT NAME
*Feculty of Computer Application Information Technology*

---

### PROJECT REPORT

### On

# **AI Workforce — Autonomous Marketing Employees Platform**

---

**Submitted in partial fulfilment of the requirements for the degree of**

*Master of Science (Information Technology)*

---

**Submitted By:**

| Field | Details |
|-------|---------|
| **Group No.** | *40* |
| **Semester / Year** | *7th Semester / 4th Year* |


---

**Submitted To:**

| Field | Details |
|-------|---------|
| **Faculty Name** | *Ankita ma'am* |


---

**Date of Submission:** *27/10/2026*

**Academic Session:** *2026-2027*

</div>

---

<div style="page-break-after: always;"></div>

## TABLE OF CONTENTS

| Sr. No. | Section | Page |
|---------|---------|------|
| 1 | Cover Page | 1 |
| 2 | Table of Contents | 2 |
| 3 | Introduction | 3 |
| 3.1 | Project Objective | 3 |
| 3.2 | Purpose and Scope | 3 |
| 3.3 | Technology Stack | 4 |
| 3.4 | Project Architecture | 4 |
| 4 | Screenshots — User Side | 5 |
| 4.1 | Landing Page (Public) | 5 |
| 4.2 | Login Page | 5 |
| 4.3 | Registration Page | 6 |
| 4.4 | Dashboard | 6 |
| 4.5 | AI Employees (Chat Interface) | 7 |
| 4.6 | Approvals Queue | 8 |
| 4.7 | Approval Detail | 8 |
| 4.8 | Users Management | 9 |
| 4.9 | Configurations (LLM Providers) | 9 |
| 4.10 | MCP Tools | 10 |
| 4.11 | MCP Server Detail | 10 |
| 4.12 | Knowledge Base | 11 |
| 4.13 | Multi-Agent Workflows | 11 |
| 5 | Screenshots — Admin Side | 12 |
| 5.1 | Admin Dashboard (Index Page) | 12 |
| 5.2 | AI Employees — List View (Flagship Admin) | 12 |
| 5.3 | AI Employees — Change/Edit Form | 13 |
| 5.4 | Profiles — List View | 13 |
| 5.5 | LLM Providers — List View | 14 |
| 5.6 | LLM Models — List View | 14 |
| 5.7 | MCP Servers — List View | 15 |
| 5.8 | MCP Tools — List View | 15 |
| 5.9 | Conversations — List View | 15 |
| 5.10 | Chat Messages — List View | 16 |
| 5.11 | Approval Queue — List View | 16 |
| 5.12 | Marketing Campaigns — List View | 17 |
| 5.13 | Leads — List View | 17 |
| 5.14 | Social Posts — List View | 17 |
| 5.15 | Email Outreach — List View | 18 |
| 5.16 | Analytics Metrics — List View | 18 |
| 6 | Key Features Checklist | 19 |
| 7 | References | 20 |

---

<div style="page-break-after: always;"></div>

## 3. INTRODUCTION

### 3.1 Project Objective

**AI Workforce** is a full-stack Django web application that simulates an autonomous marketing department staffed entirely by AI employees. The core objective is to demonstrate how artificial intelligence agents can be orchestrated to perform marketing operations — drafting social media posts, sourcing sales prospects, composing outreach emails, and analysing campaign performance — while keeping a **human-in-the-loop** at every critical decision point.

Every piece of content produced by an AI employee is routed through a **mandatory approval queue** before it can reach the outside world. This ensures that no AI-generated output is published, sent, or acted upon without explicit human authorisation.

### 3.2 Purpose and Scope

The purpose of this project is to build a **production-grade Django application** that demonstrates:

1. **AI Agent Management** — Create, configure and converse with specialised AI employees, each backed by a real language model (OpenRouter, NVIDIA NIM, or Ollama).

2. **Human-in-the-Loop Governance** — A complete approval pipeline where AI proposals are reviewed, edited and approved or rejected by human staff before any external action is taken.

3. **Model Context Protocol (MCP) Integration** — Seven MCP tool servers (Gmail, Instagram, Database, Memory, Sequential Thinking, Spotify, LinkedIn, Calendar, Slack, GitHub/Jira, Web Search) modelled and connected, giving AI employees callable capabilities.

4. **Role-Based Access Control (RBAC)** — Four roles (Owner, Manager, Analyst, Viewer) with graduated permissions controlling who may chat, approve, configure, or manage users.

5. **Enterprise Knowledge Base & RAG** — Document upload, chunking, and Retrieval-Augmented Generation for grounding AI answers with source citations.

6. **Multi-Agent Team Workflows** — Orchestrate complex business operations across multiple specialised AI employees with automated context handoffs.

### 3.3 Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend Framework** | Django 6.1 (Python) |
| **Database** | SQLite 3 |
| **Frontend** | HTML5, CSS3 (Custom Design System), Vanilla JavaScript |
| **CSS Architecture** | Design Tokens -> Base -> Layout -> Components -> Pages -> Utilities |
| **Icons** | Font Awesome 6 |
| **LLM Integration** | urllib.request (no third-party HTTP library) |
| **Template Engine** | Django Template Language with custom template tags |
| **Authentication** | Django Auth (Session-based) |
| **Admin** | Django Admin (Fully Customised) |

### 3.4 Project Architecture

```
AiworkForce-main/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies (Django 6.1)
├── db.sqlite3                   # SQLite database
├── .env                         # Environment variables (API keys, email)
│
├── marketpulse/                 # Django project settings
│   ├── settings.py              # Main configuration
│   ├── urls.py                  # Root URL configuration
│   ├── wsgi.py / asgi.py        # Deployment entry points
│   └── env.py                   # .env file loader
│
├── marketing/                   # Main Django application
│   ├── models.py                # 20+ database models (1225 lines)
│   ├── views.py                 # ~50 view functions (1529 lines)
│   ├── admin.py                 # Fully customised admin (537 lines)
│   ├── forms.py                 # Django ModelForms (18KB)
│   ├── urls.py                  # URL patterns (101 lines)
│   ├── roles.py                 # RBAC permission constants
│   ├── signals.py               # Django signals
│   ├── context_processors.py    # Global template context
│   ├── agent_engine.py          # AI agent logic
│   ├── llm_client.py            # LLM API integration
│   ├── mcp_client.py            # MCP protocol simulation
│   ├── rag_engine.py            # RAG retrieval engine
│   ├── workflow_engine.py       # Multi-agent workflow orchestration
│   ├── mailer.py                # Email delivery
│   ├── mail_agent.py            # Gmail integration
│   ├── gmail_client.py          # Gmail API client
│   ├── templatetags/            # Custom template tags
│   └── management/commands/     # Management commands (seed_data)
│
├── templates/                   # HTML templates (18 pages + 14 partials)
│   ├── base.html                # Authenticated page shell
│   ├── base_public.html         # Public page shell
│   ├── dashboard.html           # Dashboard page
│   ├── agents.html              # AI Employees chat interface
│   ├── approvals.html           # Approval queue
│   ├── approval_detail.html     # Single approval detail
│   ├── users.html               # User management
│   ├── configurations.html      # LLM provider configuration
│   ├── mcp_tools.html           # MCP tool servers
│   ├── mcp_server_detail.html   # Single MCP server detail
│   ├── knowledge_base.html      # Knowledge base & RAG
│   ├── workflows.html           # Multi-agent workflows
│   ├── login.html               # Sign in
│   ├── register.html            # Create account
│   ├── static_landing.html      # Public landing page
│   └── partials/                # 14 reusable template fragments
│
└── static/
    ├── css/                     # 6-file design system
    │   ├── tokens.css           # Design tokens (colours, spacing, fonts)
    │   ├── base.css             # Reset and base styles
    │   ├── layout.css           # Grid and layout system
    │   ├── components.css       # Reusable components
    │   ├── pages.css            # Page-specific styles
    │   └── utilities.css        # Utility classes
    └── js/                      # JavaScript modules
```

---

<div style="page-break-after: always;"></div>

## 4. SCREENSHOTS — USER SIDE

> **Note:** To capture these screenshots, run the application with `python manage.py runserver` and visit `http://127.0.0.1:8000/`. Insert your actual screenshots below each label.

---

### 4.1 Landing Page (Public)

**URL:** `http://127.0.0.1:8000/`
**Template:** `templates/static_landing.html`
**View:** `landing_page()`

**Description:** The public landing page is the first screen visitors see. It features a hero section with the headline *"Marketing employees that never sleep, and never publish without you"*. Below the hero are statistics (4 AI employees, 7 MCP servers, 100% human approval) and feature cards describing each AI employee type. Call-to-action buttons lead to registration and login. A signed-in user is automatically redirected to the Dashboard.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/ in browser -> Take screenshot -> Paste here)*

---

### 4.2 Login Page

**URL:** `http://127.0.0.1:8000/login/`
**Template:** `templates/login.html`
**View:** `login_view()`

**Description:** A centred authentication card with a purple avatar icon, "Sign in" heading, and subtitle "Access your AI workforce and approval queue." Contains two form fields (Username and Password) and a purple "Sign in" button. A link at the bottom directs new users to the registration page. Uses Django's built-in `AuthenticationForm` for validation.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/login/ in browser -> Take screenshot -> Paste here)*

---

### 4.3 Registration Page

**URL:** `http://127.0.0.1:8000/register/`
**Template:** `templates/register.html`
**View:** `register_view()`

**Description:** A registration form with fields for username, email, and password. The subtitle states "Four AI employees and seven MCP servers are provisioned automatically." On successful registration, the system automatically provisions 4 AI agents, 3 LLM providers with their model catalogues, and 7 MCP servers with their tools via `agent_engine.ensure_workspace_for_user()`.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/register/ in browser -> Take screenshot -> Paste here)*

---

### 4.4 Dashboard (PAGE 1 of 6)

**URL:** `http://127.0.0.1:8000/workspace/`
**Template:** `templates/dashboard.html`
**View:** `dashboard_view()`

**Description:** The main workspace dashboard visible after login. Contains:
- **Left Sidebar** — Navigation with links to all 6 workspace pages: Dashboard, AI Employees, Approvals, Users, Configurations, and MCP Tools, plus Knowledge Base and Workflows.
- **Top Bar** — Greeting "Welcome back, {username}" with action buttons (New Campaign, Talk to an Employee, Review Queue).
- **KPI Tiles (4)** — Total Prospects, Awaiting Approval, Published Posts, Active Campaigns — each with icon, value and coloured accent.
- **AI Employees Card** — Lists all AI employees with avatars, roles, and assigned LLM models.
- **Platform Status Card** — Shows MCP server connection health, LLM provider status.
- **Campaigns Table** — Active marketing campaigns with status badges.
- **Recent Activity** — Latest approvals and social posts.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/workspace/ in browser after login -> Take screenshot -> Paste here)*

---

### 4.5 AI Employees — Chat Interface (PAGE 2 of 6)

**URL:** `http://127.0.0.1:8000/agents/`
**Template:** `templates/agents.html`
**View:** `agents_view()`

**Description:** A full chat screen with three-panel layout:
- **Left Rail** — Conversation history grouped by AI employee, with "New conversation" buttons for each agent type.
- **Centre Panel** — Active chat thread displaying messages in bubbles. Each AI reply includes generation source badges (Live LLM / Template Fallback), token count, and "Send for Approval" buttons for actionable content.
- **Right Panel (Slide-out)** — Employee configuration: name, role, persona description, system prompt, LLM model selector, temperature slider, max tokens, and attached MCP tools.

Chat uses JSON API endpoints (`/api/chat/send/`, `/api/chat/new/`, etc.) for real-time messaging without full page reloads.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/agents/ in browser -> Take screenshot -> Paste here)*

---

### 4.6 Approvals Queue (PAGE 3 of 6)

**URL:** `http://127.0.0.1:8000/approvals/`
**Template:** `templates/approvals.html`
**View:** `approvals_view()`

**Description:** The human-in-the-loop approval interface with:
- **Status Tabs** — Pending, Approved, Rejected, All — each with live count badges, rendered as server-side links (`?status=pending`).
- **Type Filter & Search** — Dropdown to filter by item type (Social Post, Email, Lead, Insight) and a search bar.
- **Approval Cards** — Each card shows the item title, producing AI agent, item type icon, priority badge, generation source, timestamp, and Approve/Reject action buttons.
- **Bulk Actions** — Checkbox selection with "Approve selected" and "Reject selected" bulk operations.
- **Pagination** — Server-side pagination with page navigation.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/approvals/ in browser -> Take screenshot -> Paste here)*

---

### 4.7 Approval Detail

**URL:** `http://127.0.0.1:8000/approvals/<id>/`
**Template:** `templates/approval_detail.html`
**View:** `approval_detail_view()`

**Description:** A two-column detail page for a single approval request:
- **Left Column** — Full content preview (social post text, email body, or lead details), editable before approval. For social posts, the reviewer can edit title, content, hashtags, and platform before approving.
- **Right Column** — Metadata card showing the AI agent that produced it, item type, priority, generation source, LLM model used, token count, and the decision form (Approve/Reject with reason text field).
- **Audit Trail** — Full history of every action taken on this approval (created, edited, approved/rejected) with actor and timestamp.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/approvals/1/ in browser -> Take screenshot -> Paste here)*

---

### 4.8 Users Management (PAGE 4 of 6)

**URL:** `http://127.0.0.1:8000/users/`
**Template:** `templates/users.html`
**View:** `users_view()`

**Description:** User management console displaying:
- **KPI Tiles (4)** — Total Accounts, Active Users, Staff Users, Showing (current page count).
- **Role Permission Matrix** — Table showing what each role (Owner, Manager, Analyst, Viewer) can do: Read, Chat & Submit, Approve/Reject, Configure, and Manage Users.
- **User Cards** — Each user displayed as a card with avatar (coloured initial), username, email, role badge, job title, last activity timestamp, and action buttons (Edit, Toggle Active/Suspended, Set Staff, Delete). Permission-protected actions only appear for authorised users.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/users/ in browser -> Take screenshot -> Paste here)*

---

### 4.9 Configurations — LLM Providers (PAGE 5 of 6)

**URL:** `http://127.0.0.1:8000/configurations/`
**Template:** `templates/configurations.html`
**View:** `configurations_view()`

**Description:** LLM provider configuration page with:
- **KPI Tiles (5)** — Providers, Configured, Tested Online, Models Available, Email Delivery Status.
- **Email Delivery Section** — Read-only panel showing SMTP configuration status (Live or Console mode) with environment variable guidance.
- **Provider Cards** — One card per provider (OpenRouter, NVIDIA NIM, Ollama) showing:
  - Connection status badge (Online/Untested/Error)
  - API key (masked) with key source (database/environment/none)
  - Base URL
  - "Test Connection" button (triggers real HTTP request)
  - "Fetch Models" button (syncs model catalogue)
  - Cascading model dropdown
  - Last tested timestamp and latency

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/configurations/ in browser -> Take screenshot -> Paste here)*

---

### 4.10 MCP Tools (PAGE 6 of 6)

**URL:** `http://127.0.0.1:8000/mcp-tools/`
**Template:** `templates/mcp_tools.html`
**View:** `mcp_tools_view()`

**Description:** Model Context Protocol server overview with:
- Server cards for each registered MCP server (Gmail, Instagram, Database, Memory, Sequential Thinking, Spotify, LinkedIn, Calendar, Slack, GitHub/Jira, Web Search).
- Each card shows: server name, category badge, transport type, tool count, connection status, enable/disable toggle, and "Test" / "View Details" buttons.
- "Register a server" button for adding new MCP servers.
- Connection tests run `mcp_client.simulate_handshake()` — a configuration-based simulation rather than a live connection.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/mcp-tools/ in browser -> Take screenshot -> Paste here)*

---

### 4.11 MCP Server Detail

**URL:** `http://127.0.0.1:8000/mcp-tools/<id>/`
**Template:** `templates/mcp_server_detail.html`
**View:** `mcp_server_detail_view()`

**Description:** Detailed view for a single MCP server showing:
- **Connection Settings** — Transport type, command/endpoint, authentication token, protocol version, and JSON configuration.
- **Tool Registry** — List of all tools advertised by this server, each showing tool name, display name, description, input schema, destructive flag, and call count.
- **Call Log** — History of simulated MCP tool invocations with agent, arguments, outcome, and timestamp.
- Edit form for server settings and "Add Tool" form for registering new capabilities.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/mcp-tools/1/ in browser -> Take screenshot -> Paste here)*

---

### 4.12 Knowledge Base

**URL:** `http://127.0.0.1:8000/knowledge/`
**Template:** `templates/knowledge_base.html`
**View:** `knowledge_base_view()`

**Description:** Enterprise document management and RAG search interface:
- **KPI Tiles (3)** — Documents Uploaded, Text Chunks Indexed, RAG Citations Active.
- **Upload Card** — Form for uploading enterprise documents (TXT, PDF, etc.) with title and file input.
- **Search Card** — RAG-powered semantic search across all indexed document chunks, returning results with source citations.
- **Document Library** — List of all uploaded documents with file type, size, chunk count, and delete action.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/knowledge/ in browser -> Take screenshot -> Paste here)*

---

### 4.13 Multi-Agent Team Workflows

**URL:** `http://127.0.0.1:8000/workflows/`
**Template:** `templates/workflows.html`
**View:** `workflows_view()`

**Description:** Multi-agent workflow orchestration page with:
- **Preset Workflow Launcher** — Grid of pre-built workflow templates (e.g., "Product Launch Campaign", "Market Research Sprint") each with title, objective description, participating agents with step assignments, and "Launch" button.
- **Active Workflows** — List of running and completed workflows showing title, status, step progress, and timeline.
- Each workflow step shows the assigned agent, role name, input prompt, output text, and status (Pending/Running/Completed/Awaiting Approval/Failed).

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/workflows/ in browser -> Take screenshot -> Paste here)*

---

<div style="page-break-after: always;"></div>

## 5. SCREENSHOTS — ADMIN SIDE

> **Note:** Access the admin panel at `http://127.0.0.1:8000/admin/` using a superuser account. Create one with: `python manage.py createsuperuser`

---

### 5.1 Admin Dashboard (Index Page)

**URL:** `http://127.0.0.1:8000/admin/`

**Description:** The Django admin index page, customised with:
- **Site Header:** "AI Workforce Administration"
- **Site Title:** "AI Workforce Admin"
- **Index Title:** "Autonomous Marketing Control Centre"
- Lists all 16 registered models grouped under the "Marketing" app: AI Employees, Agent Tool Attachments, Analytics Metrics, Approval Queue, Approval Audit Trail, Chat Messages, Conversations, Knowledge Base Documents, Leads, LLM Models, LLM Providers, Marketing Campaigns, MCP Call Log, MCP Servers, MCP Tools, Outreach Emails, Social Posts, User Profiles.

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/ in browser -> Take screenshot -> Paste here)*

---

### 5.2 AI Employees — List View (Flagship Admin)

**URL:** `http://127.0.0.1:8000/admin/marketing/aiagent/`

**Description:** The **flagship customised admin** demonstrating advanced Django admin features:

- **`list_display`** — Coloured avatar swatch (initial circle), name, role, agent type, owner link (clickable to user admin), LLM badge (model ID + provider), MCP tool count (annotated), performance bar (CSS progress bar with colour coding), tasks completed, status (editable), is_active (editable checkbox).
- **`list_filter` (Filters Panel)** — Agent type, status, is_active, LLM provider (`llm_model__provider__provider_key` — relation traversal), created_at (DateFieldListFilter).
- **`list_editable`** — Status and is_active can be changed directly from the list.
- **`search_fields`** — Search across name, role, persona_description, system_prompt, user__username, user__email.
- **`date_hierarchy`** — Date drill-down by created_at.
- **Custom `@admin.display` methods** — `avatar_swatch()` renders coloured HTML circles, `owner_link()` renders clickable links, `llm_badge()` renders formatted model info, `performance_bar()` renders CSS progress bars.
- **Custom `get_queryset()`** — Uses `select_related` + `annotate` for optimised queries; non-superusers see only their own employees.
- **Bulk Actions** — "Mark as active", "Set to idle", "Reset task counters", "Regenerate system prompts".

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/aiagent/ in browser -> Take screenshot -> Paste here)*

---

### 5.3 AI Employees — Change/Edit Form

**URL:** `http://127.0.0.1:8000/admin/marketing/aiagent/<id>/change/`

**Description:** The AI Employee edit form with:
- **Fieldsets (5 groups, some collapsible):**
  1. *Identity* — user (autocomplete), name, role, agent_type, avatar_icon, avatar_color, is_active, status
  2. *Persona and system prompt* (collapsible) — persona_description, system_prompt, prompt_preview (readonly, formatted HTML pre block)
  3. *Language model configuration* — llm_model (autocomplete), temperature, max_tokens
  4. *MCP capability* (collapsible) — tool_summary (readonly, computed HTML)
  5. *Performance and audit* (collapsible) — tasks_completed, success_rate, approval_stats (readonly, computed), created_at, updated_at
- **Inlines (3):**
  1. `AgentToolLinkInline` — Editable table of attached MCP tools with autocomplete
  2. `ConversationInline` — Read-only list of chat threads (show_change_link)
  3. `ApprovalRequestInline` — Read-only history of submitted approvals
- **`autocomplete_fields`** — user, llm_model
- **`readonly_fields`** — created_at, updated_at, tasks_completed, tool_summary, prompt_preview, approval_stats
- **`save_model()` override** — Auto-assigns owner and generates default system prompt

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/aiagent/1/change/ in browser -> Take screenshot -> Paste here)*

---

### 5.4 Profiles — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/profile/`

**Description:** User profile admin with:
- **`list_display`** — user, role, job_title, theme, last_activity
- **`list_filter`** — role, theme
- **`search_fields`** — user__username, user__email, job_title
- **`autocomplete_fields`** — user
- **`readonly_fields`** — created_at, updated_at, last_activity

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/profile/ in browser -> Take screenshot -> Paste here)*

---

### 5.5 LLM Providers — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/llmprovider/`

**Description:** LLM Provider admin with:
- **`list_display`** — provider_key_display, user, masked_key, is_enabled, connection_status, model_count, last_tested_at
- **`list_filter`** — provider_key, is_enabled, connection_status
- **Fieldsets** — Provider settings, Connection details, Last test results (collapsible)
- **Inline** — LLMModelInline (child models table)
- **Custom display** — `masked_key()` shows partially hidden API key

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/llmprovider/ in browser -> Take screenshot -> Paste here)*

---

### 5.6 LLM Models — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/llmmodel/`

**Description:** Language model catalogue admin with:
- **`list_display`** — model_id, display_name, provider, context_length, source, is_enabled
- **`list_filter`** — provider__provider_key, source, is_enabled
- **`list_editable`** — is_enabled (toggle directly from list)
- **`search_fields`** — model_id, display_name, description

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/llmmodel/ in browser -> Take screenshot -> Paste here)*

---

### 5.7 MCP Servers — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/mcpserver/`

**Description:** MCP Server admin with:
- **`list_display`** — name, server_key, user, category, transport, tool_count (computed), is_enabled (editable), connection_status, last_handshake_at
- **`list_filter`** — category, transport, is_enabled, connection_status
- **Fieldsets** — Server identity, Connection settings, Last handshake (collapsible)
- **Inline** — MCPToolInline (registered tools)

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/mcpserver/ in browser -> Take screenshot -> Paste here)*

---

### 5.8 MCP Tools — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/mcptool/`

**Description:** MCP Tool admin with:
- **`list_display`** — display_name, tool_name, server, is_enabled (editable), is_destructive, call_count
- **`list_filter`** — server__server_key, is_enabled, is_destructive

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/mcptool/ in browser -> Take screenshot -> Paste here)*

---

### 5.9 Conversations — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/conversation/`

**Description:** Conversation admin with:
- **`list_display`** — title, agent, user, message_count (computed property), updated_at
- **`list_filter`** — agent__agent_type, is_archived, updated_at (DateFieldListFilter)
- **`date_hierarchy`** — updated_at
- **Inline** — ChatMessageInline (read-only message history)

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/conversation/ in browser -> Take screenshot -> Paste here)*

---

### 5.10 Chat Messages — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/chatmessage/`

**Description:** Chat message admin with:
- **`list_display`** — created_at, conversation, role, short_content (truncated to 80 chars), generation_source, llm_model_used, tokens_used
- **`list_filter`** — role, generation_source, created_at (DateFieldListFilter)
- Custom `short_content()` display method

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/chatmessage/ in browser -> Take screenshot -> Paste here)*

---

### 5.11 Approval Queue — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/approvalrequest/`

**Description:** Approval request admin with:
- **`list_display`** — title, item_type, agent, user, status, priority, generation_source, requested_at, decided_by
- **`list_filter`** — status, item_type, priority, generation_source, social_post__platform (relation traversal), requested_at (DateFieldListFilter)
- **`date_hierarchy`** — requested_at
- **Inline** — ApprovalAuditLogInline (full audit trail)
- **Custom `get_queryset()`** — Optimised with `select_related` across 5 related models

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/approvalrequest/ in browser -> Take screenshot -> Paste here)*

---

### 5.12 Marketing Campaigns — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/marketingcampaign/`

**Description:** Campaign admin with:
- **`list_display`** — name, user, status (editable), target_audience, budget, assigned_agent, start_date
- **`list_filter`** — status, start_date
- **`autocomplete_fields`** — user, assigned_agent

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/marketingcampaign/ in browser -> Take screenshot -> Paste here)*

---

### 5.13 Leads — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/lead/`

**Description:** Lead management admin with:
- **`list_display`** — full_name, company, email, user, industry, lead_score, score_tier, status (editable), created_at
- **`list_filter`** — score_tier, status, industry
- **`date_hierarchy`** — created_at
- **`autocomplete_fields`** — user, campaign, discovered_by

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/lead/ in browser -> Take screenshot -> Paste here)*

---

### 5.14 Social Posts — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/socialpost/`

**Description:** Social post admin with:
- **`list_display`** — title, user, platform, status (editable), likes, shares, comments, published_at, created_at
- **`list_filter`** — platform, status
- **`date_hierarchy`** — created_at

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/socialpost/ in browser -> Take screenshot -> Paste here)*

---

### 5.15 Email Outreach — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/emailoutreach/`

**Description:** Email outreach admin with:
- **`list_display`** — subject, lead, user, sequence_step, status (editable), sent_at
- **`list_filter`** — status, sequence_step

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/emailoutreach/ in browser -> Take screenshot -> Paste here)*

---

### 5.16 Analytics Metrics — List View

**URL:** `http://127.0.0.1:8000/admin/marketing/analyticsmetric/`

**Description:** Analytics metric admin with:
- **`list_display`** — title, user, category, value, change_percent, is_positive, metric_date
- **`list_filter`** — category, is_positive

> 📸 **INSERT SCREENSHOT HERE**
> *(Open http://127.0.0.1:8000/admin/marketing/analyticsmetric/ in browser -> Take screenshot -> Paste here)*

---

<div style="page-break-after: always;"></div>

## 6. KEY FEATURES CHECKLIST

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 1 | **Customised Templates for Design Consistency** | ✅ Present | `base.html` template inheritance + 14 reusable partials (`_sidebar.html`, `_topbar.html`, `_kpi_tile.html`, `_status_badge.html`, etc.) + 6-file CSS design system (`tokens.css` to `utilities.css`) + custom context processor (`workspace_chrome`) |
| 2 | **Appropriate Views & Templates** | ✅ Present | 18 HTML templates + ~50 view functions covering all CRUD operations, chat interface, approval workflow, and configuration management |
| 3 | **At least 1 User Defined Model** | ✅ Present | **20+ custom models** in `models.py` (1225 lines): Profile, LLMProvider, LLMModel, MCPServer, MCPTool, AIAgent, AgentToolLink, Conversation, ChatMessage, MCPCallLog, MarketingCampaign, Lead, SocialPost, EmailOutreach, AnalyticsMetric, ApprovalRequest, ApprovalAuditLog, Document, DocumentChunk, MultiAgentWorkflow, WorkflowStep |
| 4 | **At least 1 Filter on Admin Panel** | ✅ Present | **Extensive `list_filter`** on all 16 admin classes. Flagship `AIAgentAdmin` has 5 filters including relation traversal (`llm_model__provider__provider_key`) and DateFieldListFilter. Plus `search_fields`, `date_hierarchy`, `autocomplete_fields` across all models |
| 5 | **Cookies and Session Settings** | ✅ Present | `django.contrib.sessions` in INSTALLED_APPS, `SessionMiddleware` in MIDDLEWARE, session-based authentication via `login()`/`logout()`, CSRF cookie via `{% csrf_token %}` on every page |
| 6 | **REST API Interface** | ✅ Present | **17+ JSON API endpoints** in `views.py` returning `JsonResponse`: `/api/edit-agent/`, `/api/chat/send/`, `/api/chat/new/`, `/api/approvals/decide/`, `/api/providers/test/`, `/api/mcp/test/`, `/api/users/toggle-active/`, `/api/preferences/theme/`, etc. All decorated with `@login_required` and `@require_POST` |

---

<div style="page-break-after: always;"></div>

## 7. REFERENCES

1. **Django Documentation** (v6.1)
   - https://docs.djangoproject.com/en/6.1/
   - Topics: Models, Views, Templates, Admin, Authentication, Sessions, CSRF

2. **Django Admin Customisation**
   - https://docs.djangoproject.com/en/6.1/ref/contrib/admin/
   - Features used: `list_display`, `list_filter`, `list_editable`, `search_fields`, `fieldsets`, `inlines`, `autocomplete_fields`, `actions`, `date_hierarchy`, `get_queryset()`, `save_model()`

3. **Model Context Protocol (MCP) Specification**
   - https://modelcontextprotocol.io/
   - Reference for tool server modelling and `initialize` handshake simulation

4. **OpenRouter API**
   - https://openrouter.ai/docs
   - Used for multi-provider LLM integration

5. **NVIDIA NIM API**
   - https://docs.nvidia.com/nim/
   - Used for NVIDIA language model integration

6. **Ollama**
   - https://ollama.com/
   - Used for local language model deployment

7. **Font Awesome 6**
   - https://fontawesome.com/
   - Icon library used throughout the UI

8. **Django REST Framework** (Reference)
   - https://www.django-rest-framework.org/
   - Reference for REST API best practices

9. **Python Standard Library — urllib.request**
   - https://docs.python.org/3/library/urllib.request.html
   - Used for all HTTP calls to LLM providers (no third-party HTTP libraries)

10. **Retrieval-Augmented Generation (RAG)**
    - Lewis, P., et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020.*
    - https://arxiv.org/abs/2005.11401

---

*End of Documentation*
