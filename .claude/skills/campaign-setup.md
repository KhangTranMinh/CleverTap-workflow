# Skill: campaign-setup

When the user invokes `/campaign-setup` or asks to set up a campaign via the CleverTap API:

## Step 1 — Confirm Credentials

Check if `scripts/.env` exists and has CleverTap credentials:
```
CLEVERTAP_ACCOUNT_ID=...
CLEVERTAP_PASSCODE=...
```

If missing, tell the user to fill them in before proceeding.

## Step 2 — Determine What to Set Up

Ask the user which plan to execute, or read the most recent confirmed plan from `plans/`.

Determine what needs to be created:
- **Segments** — if the plan defines audience filters
- **Campaigns** — push notifications, in-app messages, etc.
- **Both**

## Step 3 — Run the Setup Script

For segments:
```bash
python3 scripts/campaign_setup.py --plan plans/<file>.md --action create-segment
```

For campaigns:
```bash
python3 scripts/campaign_setup.py --plan plans/<file>.md --action create-campaign
```

For both:
```bash
python3 scripts/campaign_setup.py --plan plans/<file>.md --action all
```

## Step 4 — Verify and Report

After setup, run:
```bash
python3 scripts/campaign_setup.py --action verify --campaign-id <id>
```

Report back with created resource IDs and a link to the CleverTap dashboard.

## Step 5 — Schedule Monitoring

Ask: "Do you want me to check campaign performance after launch? I can pull stats using `/campaign-report`."

## Notes
- Always create segment first, then campaign
- For recurring campaigns, verify the cron expression before submitting
- Transactional campaigns bypass frequency caps — confirm with user if using them
