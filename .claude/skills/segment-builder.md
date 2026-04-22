# Skill: segment-builder

When the user invokes `/segment-builder` or asks to define/build an audience segment:

## Step 1 — Understand the Audience

Ask (if not already provided):
- Who are we targeting? (describe in plain language)
- Which vertical? (food / ride / both)
- Behavioral criteria? (events they did/didn't do, frequency)
- Recency? (last 7 days / 30 days / ever)
- Profile properties? (city, user type, payment method)

## Step 2 — Translate to CleverTap Filters

Build the segment definition using CleverTap's filter system:

### Event-Based Filters
```
Did event "Order Placed" at least 3 times in last 30 days
AND Did NOT do event "Order Placed" in last 7 days
```

### Property-Based Filters
```
User Property: custom_user_type = "food_only"
User Property: total_food_orders > 5
```

### Combined Example — Churned Food Power Users
```
Did "Order Placed" at least 5 times (ever)
AND Did NOT do "Order Placed" in last 30 days
AND User Property: total_food_orders > 5
```

## Step 3 — Estimate Segment Size

Advise user to check size in CleverTap dashboard:
Dashboard → Segments → Create → Apply filters → Check estimated count

Rule of thumb:
- < 1,000 users: Too small for statistical significance in A/B tests
- 1,000–10,000: Good for targeted campaigns
- 10,000+: Consider further segmentation for personalization

## Step 4 — Output the Segment Spec

Produce a segment specification block to include in the plan:

```yaml
segment:
  name: "Churned Food Power Users"
  description: "Users with 5+ past orders but inactive 30+ days"
  filters:
    - type: event
      event: "Order Placed"
      condition: did_at_least
      count: 5
      period: ever
    - type: event
      event: "Order Placed"
      condition: did_not_do
      period: last_30_days
    - type: property
      property: total_food_orders
      operator: greater_than
      value: 5
  estimated_size: ~50,000
```

## Step 5 — Suggest Personalization

Based on segment, recommend message personalization:
- Use `{{name}}` for greeting
- Reference last order: `{{last_order_restaurant}}`
- Use location-specific offers if geo property available
