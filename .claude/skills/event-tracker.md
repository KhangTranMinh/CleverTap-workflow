# Skill: event-tracker

When the user invokes `/event-tracker` or asks to define/design event tracking:

## Step 1 — Understand the Feature

Ask:
- What new feature or user flow needs tracking?
- Platform: Android / iOS / both?
- Do they need server-side or client-side events?
- What decisions will this data support? (segmentation, campaign trigger, funnel analysis)

## Step 2 — Design the Event Schema

For each event in the flow, define:
```yaml
event:
  name: "Event Name"  # Title Case, matches super-app-events.md convention
  trigger: "When user does X"
  platform: android, ios
  type: client-side | server-side
  properties:
    - name: property_name
      type: string | number | boolean
      required: true | false
      example: "example_value"
      notes: "Additional context"
```

Cross-reference `knowledge/super-app-events.md` — reuse existing events where possible, only define new ones when truly needed.

## Step 3 — Generate Implementation Ticket

Produce a Jira-ready task for Duc:

**Title**: `[Tracking] Instrument {feature} events`

**Description**:
```
Implement the following CleverTap events for {feature}:

Android (Kotlin):
// Event 1
val props = HashMap<String, Any>()
props["property_name"] = value
CleverTap.getDefaultInstance(context)?.event?.push("Event Name", props)

iOS (Swift):
// Event 1
CleverTap.sharedInstance()?.recordEvent("Event Name", withProps: [
    "property_name": value
])

QA: Verify in CleverTap Dashboard → Events → Live View
```

## Step 4 — Generate QA Checklist

Produce a QA task (assign to any available team member):
```
QA Checklist for {feature} tracking:
[ ] Verify event fires on Android (device: Pixel/Samsung)
[ ] Verify event fires on iOS (device: iPhone 14+)
[ ] All required properties present with correct types
[ ] No PII in event properties (except Identity)
[ ] Events visible in Live View within 2 minutes
[ ] Funnel analysis in CleverTap works as expected
```

## Step 5 — Update Events Reference

Remind user: "Once verified, add the new events to `knowledge/super-app-events.md` to keep the reference up to date."
