# CleverTap REST API Reference

Base URL: `https://api.clevertap.com/1/`

## Authentication
All requests require two headers:
```
X-CleverTap-Account-Id: <your-account-id>
X-CleverTap-Passcode: <your-passcode>
Content-Type: application/json
```

Find credentials: CleverTap Dashboard → Settings → Integration → API Credentials

## Rate Limits
- Upload events: 1,000 events/request, 60 req/min
- Profile queries: 30 req/min
- Campaign triggers: 60 req/min

---

## Events API

### Upload Events
`POST /upload`

```json
{
  "d": [
    {
      "identity": "user123",
      "ts": 1700000000,
      "type": "event",
      "evtName": "Order Placed",
      "evtData": {
        "order_id": "ORD-001",
        "cart_total": 150000
      }
    }
  ]
}
```

### Get Event Stats
`POST /counts/events.json`

```json
{
  "event_name": "Order Placed",
  "from": 20240101,
  "to": 20240131
}
```

---

## Profile API

### Get Profile
`GET /profile.json?email=user@example.com`
Or by identity: `GET /profile.json?identity=user123`

### Upload Profile
`POST /upload`

```json
{
  "d": [
    {
      "identity": "user123",
      "ts": 1700000000,
      "type": "profile",
      "profileData": {
        "Name": "John",
        "Phone": "+84901234567",
        "total_food_orders": 15
      }
    }
  ]
}
```

---

## Segments / Lists API

### Create List (Static Segment)
`POST /lists/create.json`

```json
{
  "name": "Churned Food Users",
  "description": "Users with no food order in 30 days",
  "source": "manual",
  "users": [
    { "identity": "user1" },
    { "identity": "user2" }
  ]
}
```

Response: `{ "status": "success", "list_id": "abc123" }`

### Get List
`GET /lists/get.json?list_id=abc123`

---

## Campaigns API

### Create Campaign (One-Time Push)
`POST /targets/create.json`

```json
{
  "name": "Weekend Food Promo",
  "where": {
    "event_name": "App Launched",
    "from": 20240101,
    "to": 20240131
  },
  "when": "2024-01-20 10:00",
  "content": {
    "title": "Weekend Deal!",
    "body": "Get 30% off your next food order",
    "platform_specific": {
      "android": { "deep_link": "app://food/promo?code=WEEKEND30" },
      "ios": { "deep_link": "app://food/promo?code=WEEKEND30" }
    }
  },
  "channel": "push",
  "respect_frequency_caps": true,
  "respect_DND": true
}
```

### List Campaigns
`GET /targets/list.json?from=20240101&to=20240131`

### Get Campaign Stats
`GET /targets/<campaign_id>/result.json`

Response includes: `sent`, `delivered`, `opened`, `clicked`, `converted`

---

## Transactional Push (API-Triggered)
`POST /send/push.json`

```json
{
  "to": {
    "identity": ["user123"]
  },
  "tag_group": "default",
  "respect_frequency_caps": false,
  "content": {
    "title": "Your order is confirmed!",
    "body": "Order #ORD-001 is being prepared",
    "platform_specific": {
      "android": {
        "deep_link": "app://food/orders/ORD-001"
      }
    }
  }
}
```

---

## Webhooks (Outbound)
Configure in Dashboard → Settings → Integration → Webhooks

CleverTap will POST to your endpoint on campaign events (sent, delivered, clicked, converted).

Payload example:
```json
{
  "event": "push_delivered",
  "campaign_id": "123",
  "identity": "user123",
  "timestamp": 1700000000
}
```

---

## Common Response Codes
| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad request (check payload) |
| 401 | Auth failed (check headers) |
| 429 | Rate limit exceeded |
| 500 | CleverTap server error |
