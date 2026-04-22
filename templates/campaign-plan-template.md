# [Campaign Name]

## Overview
[One-paragraph summary of the campaign, its goal, and the expected impact]

---

## Goal & KPIs

| Goal | Target | Measurement |
|------|--------|-------------|
| [e.g. Reactivate churned food users] | [e.g. 5% conversion rate] | [e.g. "Order Placed" event] |

**Success Event**: [Event name to track conversion]
**Baseline**: [Current metric before campaign]

---

## Audience Segment

**Segment Name**: [Name in CleverTap]
**Estimated Size**: [~X users]

```yaml
filters:
  - type: event
    event: "[Event Name]"
    condition: did_not_do
    period: last_30_days
  - type: property
    property: [property_name]
    operator: greater_than
    value: [value]
```

---

## Campaign Details

**Channel**: [Push / In-App / Email / SMS]
**Schedule**: [YYYY-MM-DD HH:MM or "Triggered on [event]"]
**Frequency Cap**: [e.g. 1 per user]
**Respect DND**: [Yes / No]

**Title**: [Push title or email subject]
**Body**: [Message copy]
**CTA**: [Button text if applicable]
**Deep Link**: [app://...]

### Variants (A/B Test)
| Variant | Title | Body | Expected CTR |
|---------|-------|------|-------------|
| A (Control) | | | |
| B | | | |

---

## Tracking Events

| Event | Status | Owner |
|-------|--------|-------|
| [New event name] | New (needs instrumentation) | Duc |
| [Existing event] | Exists | — |

---

## Tasks

| Task | Description | Assignee | Points | Due Date |
|------|-------------|----------|--------|----------|
| Create segment in CleverTap | Build audience filters per spec above | Minh | 1 | YYYY-MM-DD |
| Set up campaign in CleverTap | Configure push with copy, schedule, A/B | Linh | 2 | YYYY-MM-DD |
| Instrument [event] on Android/iOS | Add SDK calls per tracking spec | Duc | 3 | YYYY-MM-DD |
| QA event tracking | Verify events in Live View on both platforms | Minh | 2 | YYYY-MM-DD |
| Monitor campaign post-launch | Pull 48h stats, report anomalies | Linh | 1 | YYYY-MM-DD |

---

## Timeline

| Milestone | Date |
|-----------|------|
| Plan confirmed | YYYY-MM-DD |
| Tracking events instrumented | YYYY-MM-DD |
| Campaign configured | YYYY-MM-DD |
| QA sign-off | YYYY-MM-DD |
| Launch | YYYY-MM-DD |
| First performance review | YYYY-MM-DD (48h post-launch) |

---

## Risks & Notes

- **Risk**: [e.g. Push opt-in rate is low in this segment — consider SMS fallback]
- **Dependency**: [e.g. Requires new deep link route from Duc first]
- **Note**: [e.g. Coordinate with product team on landing page readiness]
