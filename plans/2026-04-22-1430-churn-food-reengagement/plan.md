# Churn Food Re-engagement Campaign

## Overview
Re-engage food users who placed at least 3 orders historically but have been inactive for the past 30 days. We will send a personalized push notification with a discount voucher to bring them back. A/B test two offer levels (20% vs 30% off) to find the most cost-effective incentive.

---

## Goal & KPIs

| Goal | Target | Measurement |
|------|--------|-------------|
| Reactivate churned food users | 8% conversion rate | `Order Placed` event within 7 days of push |
| Minimize discount cost | Use lowest effective offer | Compare conversion between variant A and B |

**Success Event**: `Order Placed`
**Baseline**: 0 orders in last 30 days

---

## Audience Segment

**Segment Name**: `Churned Food Power Users - Apr 2026`
**Estimated Size**: ~45,000 users

```yaml
filters:
  - type: event
    event: "Order Placed"
    condition: did_at_least
    count: 3
    period: ever
  - type: event
    event: "Order Placed"
    condition: did_not_do
    period: last_30_days
  - type: property
    property: custom_user_type
    operator: contains
    value: food
```

---

## Campaign Details

**Channel**: Push Notification
**Schedule**: 2026-04-28 11:00 (local time)
**Frequency Cap**: 1 per user
**Respect DND**: Yes

### Variant A (Control — 20% off)
**Title**: `We miss you, {{name}}! 🍔`
**Body**: `It's been a while. Come back and enjoy 20% off your next food order today.`
**CTA**: Order Now
**Deep Link**: `app://food/promo?code=BACK20`

### Variant B (30% off)
**Title**: `We miss you, {{name}}! 🍔`
**Body**: `Special offer just for you — 30% off your next food order. Today only!`
**CTA**: Claim Offer
**Deep Link**: `app://food/promo?code=BACK30`

| Variant | Offer | Expected CTR | Expected Conversion |
|---------|-------|-------------|---------------------|
| A | 20% off | 4% | 7% |
| B | 30% off | 5% | 10% |

---

## Tracking Events

| Event | Status | Notes |
|-------|--------|-------|
| `Order Placed` | Exists | Primary conversion event |
| `Voucher Applied` | Exists | Track code BACK20 / BACK30 usage |
| `Voucher Failed` | Exists | Monitor for voucher errors at checkout |

No new events needed for this campaign.

---

## Tasks

| Task | Description | Assignee | Points | Due Date |
|------|-------------|----------|--------|----------|
| Create segment in CleverTap | Build audience filters: 3+ orders ever, no order in 30 days, food user type | Minh | 1 | 2026-04-25 |
| Set up A/B push campaign | Configure 2 variants with copy, voucher codes, deep links, 11:00 schedule | Linh | 2 | 2026-04-27 |
| Verify voucher codes with product team | Confirm BACK20 and BACK30 are active and have usage limits set | Duc | 1 | 2026-04-25 |
| QA campaign on staging | Send test push to internal devices, verify deep link and voucher apply correctly | Minh | 2 | 2026-04-27 |
| Monitor 48h post-launch | Pull delivery, CTR, conversion stats; flag any anomalies | Linh | 1 | 2026-04-30 |

---

## Timeline

| Milestone | Date |
|-----------|------|
| Plan confirmed | 2026-04-22 |
| Voucher codes confirmed | 2026-04-25 |
| Segment created | 2026-04-25 |
| Campaign configured | 2026-04-27 |
| QA sign-off | 2026-04-27 |
| Launch | 2026-04-28 11:00 |
| First performance review | 2026-04-30 (48h post-launch) |

---

## Risks & Notes

- **Risk**: Push opt-in rate for churned users may be lower than average — expected ~60% deliverability
- **Risk**: Voucher stacking — ensure BACK20/BACK30 cannot be combined with other active promos
- **Dependency**: Product team must confirm voucher codes are live before campaign goes out
- **Note**: If variant B CTR is >2x variant A, consider rolling out 30% offer to full segment
