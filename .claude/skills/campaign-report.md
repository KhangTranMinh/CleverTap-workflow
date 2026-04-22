# Skill: campaign-report

When the user invokes `/campaign-report` or asks for campaign results/stats:

## Step 1 — Identify Campaign

Ask which campaign to report on if not specified. Options:
- By campaign name (search plans/ for the campaign ID)
- By CleverTap campaign ID directly
- All campaigns in a date range

## Step 2 — Fetch Stats

Run the report script:
```bash
python3 scripts/campaign_report.py --campaign-id <id>
```

Or for a date range:
```bash
python3 scripts/campaign_report.py --from 2024-01-01 --to 2024-01-31
```

## Step 3 — Format the Report

Present results in this format:

### Campaign: {Name}
**Period**: {date range}
**Channel**: {push/email/sms/in-app}

| Metric | Count | Rate |
|--------|-------|------|
| Sent | X | 100% |
| Delivered | X | X% |
| Opened | X | X% |
| Clicked | X | X% |
| Converted | X | X% |

**Goal Event**: {event name} — {count} conversions
**Revenue Impact**: {if available}

### Analysis
- Compare CTR/conversion against benchmarks (Push: 3–5% CTR, Email: 20% open)
- Flag underperforming metrics
- Suggest next actions (A/B test copy, adjust timing, refine segment)

## Step 4 — Recommendations

Based on performance:
- If CTR < 2% on push: Suggest copy A/B test or segment refinement
- If delivery rate < 70%: Check push token validity / email bounces
- If conversion < target: Check deep link, landing page, offer relevance

Always end with: "Want me to create a follow-up campaign or segment refinement plan?"

## Benchmarks (Super App)
| Channel | Open Rate | CTR | Conversion |
|---------|-----------|-----|------------|
| Push | 15–25% | 3–5% | 1–3% |
| In-App | 80–90% | 10–15% | 5–10% |
| Email | 20–30% | 2–4% | 0.5–2% |
| SMS | 90–95% | 5–8% | 2–5% |
