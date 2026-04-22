# Skill: create-plan

When the user invokes `/create-plan` or asks to create/generate a plan, follow these steps:

## Step 1 — Gather Requirements

If the user hasn't provided enough detail, ask these questions (all at once, not one by one):
- **Goal**: What is the business objective? (e.g., re-engage churned users, boost food orders, increase ride frequency)
- **Audience**: Who is the target? (e.g., users inactive for 30 days, new users, food-only users)
- **Channel**: Push, in-app, email, SMS, or multi-channel?
- **Timeline**: When should this launch? Any deadline?
- **Success metric**: How will we measure success? (conversion event, CTR, revenue)

If the user's request clearly answers these, skip directly to Step 2.

## Step 2 — Save the Request

Create a folder at `plans/YYYY-MM-DD-HHMM-{slug}/` using today's date, current time (24h HHMM), and a short slug (lowercase, hyphens).

Inside the folder create `request.md` capturing the user's original ask verbatim, plus any clarifications exchanged:

```markdown
# Request

**Date**: YYYY-MM-DD HH:MM
**Requested by**: (user)

## Original Request
<paste the user's exact words here>

## Clarifications
<any follow-up questions and answers, or "None" if request was clear>
```

## Step 3 — Generate the Plan

Inside the same folder create `plan.md` using `templates/campaign-plan-template.md` filled in completely.

The plan must include:
1. **Overview** — One-paragraph summary
2. **Goal & KPIs** — Business goal + measurable targets
3. **Audience Segment** — CleverTap filter logic (event-based or property-based)
4. **Campaign Details** — Channel, message copy drafts, schedule, frequency cap
5. **Tracking Events** — New events to instrument (if any)
6. **Tasks** — Broken down by team member (Minh/Linh/Duc) with story point estimates
7. **Timeline** — Milestone dates
8. **Risks & Notes** — Edge cases, dependencies

## Step 4 — Update history.md

Append a row to `history.md` at the project root (create it if missing):

```
| YYYY-MM-DD HH:MM | [Campaign Name](plans/YYYY-MM-DD-HHMM-{slug}/plan.md) | — | Planning |
```

Columns: `Date | Initiative | Jira Epic | Status`
Status progression: `Planning` → `Confirmed` → `In Progress` → `Launched` → `Reported`

## Step 5 — Confirm with User

After writing the files, tell the user:

> Plan saved to `plans/YYYY-MM-DD-HHMM-{slug}/plan.md`. Please review and edit it, then confirm when ready so I can create Jira tickets.

Do NOT proceed to Jira creation automatically. Wait for explicit user confirmation.

## Guidelines

- Cross-reference `knowledge/campaign-types.md` for channel recommendations
- Cross-reference `knowledge/super-app-events.md` for event names
- Cross-reference `knowledge/team-config.md` for task assignment
- Story points: 1 = 1–2 hours, 2 = half day, 3 = full day, 5 = 2–3 days
- Distribute tasks evenly across Minh, Linh, and Duc — all three are CRM specialists with equal capability
- Always include a QA/testing task before launch
