# Skill: create-jira

When the user invokes `/create-jira` or confirms a plan and asks to create tickets:

## Step 1 — Read the Plan

Read the plan file the user confirmed. If they didn't specify which file, list files in `plans/` and ask.

## Step 2 — Extract Tasks

From the plan's Tasks section, extract each task with:
- Title
- Description (from plan context)
- Assignee (Minh / Linh / Duc)
- Story points
- Labels: `clevertap`, `crm`, and one of `campaign` / `tracking` / `engineering`
- Epic link (use plan name as epic)
- Due date (from plan timeline)

## Step 3 — Create Tickets

Run the Jira creation script:
```bash
cd /Users/khangtran/Documents/CleverTap-workflow
python3 scripts/create_jira_tickets.py --plan plans/<filename>.md
```

If the script is not yet configured (missing `.env`), tell the user:

> To create Jira tickets, I need your Jira credentials. Please fill in `scripts/.env`:
> ```
> JIRA_URL=https://yourcompany.atlassian.net
> JIRA_EMAIL=your@email.com
> JIRA_API_TOKEN=your-api-token
> JIRA_PROJECT_KEY=CRM
> ```
> Then run: `python3 scripts/create_jira_tickets.py --plan plans/<file>.md`

## Step 4 — Report Results

After tickets are created, show a summary table:

| Ticket | Title | Assignee | Points | Due |
|--------|-------|----------|--------|-----|
| CRM-123 | ... | Minh | 3 | ... |

Then ask: "Do you want me to set up the campaigns in CleverTap using the API scripts? I can automate the campaign creation based on this plan."

## Step 5 — Offer Automation

If user says yes → use `/campaign-setup`
If user says no → remind them the plan is at `plans/<file>.md` and tickets are created
