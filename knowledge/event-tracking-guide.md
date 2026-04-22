# Event Tracking Implementation Guide

## SDK Setup

### Android (Kotlin)
```kotlin
// Application.onCreate
CleverTapAPI.setDebugLevel(CleverTapAPI.LogLevel.DEBUG)
val cleverTap = CleverTapAPI.getDefaultInstance(context)

// Identify user after login
val profile = HashMap<String, Any>()
profile["Identity"] = userId
profile["Name"] = userName
profile["Phone"] = "+84${phone}"
cleverTap?.onUserLogin(profile)

// Track event
val props = HashMap<String, Any>()
props["order_id"] = "ORD-001"
props["cart_total"] = 150000
cleverTap?.event?.push("Order Placed", props)
```

### iOS (Swift)
```swift
// AppDelegate.didFinishLaunching
CleverTap.autoIntegrate()

// Identify user
CleverTap.sharedInstance()?.onUserLogin([
    "Identity": userId,
    "Name": userName
])

// Track event
CleverTap.sharedInstance()?.recordEvent("Order Placed", withProps: [
    "order_id": "ORD-001",
    "cart_total": 150000
])
```

---

## QA Checklist for Event Tracking

Before going live, verify each event:

- [ ] Event name matches spec exactly (case-sensitive)
- [ ] All required properties present
- [ ] Property types correct (string vs number vs boolean)
- [ ] Identity set before first event (or events will be anonymous)
- [ ] Events appear in CleverTap dashboard within 5 minutes
- [ ] Test on both Android and iOS
- [ ] Verify in CleverTap → Events → Live View

---

## CleverTap Dashboard Verification

**Live View**: Dashboard → Events → Live View
- See real-time events coming in
- Use for QA during development

**Event Explorer**: Dashboard → Events → Event Explorer
- Historical event volume
- Property breakdown

**Funnel Analysis**: Dashboard → Analytics → Funnels
- Build: Home Viewed → Cart Viewed → Checkout Started → Order Placed

---

## Deep Link Schema

```
app://food/home
app://food/restaurant?id={restaurant_id}
app://food/orders/{order_id}
app://food/promo?code={code}
app://ride/home
app://ride/booking?id={booking_id}
app://wallet
app://profile
```

iOS: Requires Universal Links setup + Associated Domains entitlement
Android: Requires intent-filter in AndroidManifest.xml

---

## Push Notification Setup

### Android FCM
1. Create Firebase project → Download `google-services.json`
2. Add to CleverTap Dashboard: Settings → Mobile Push → Android
3. Paste FCM Server Key

### iOS APNs
1. Generate APNs Auth Key (p8) in Apple Developer portal
2. Upload to CleverTap: Settings → Mobile Push → iOS
3. Add Push capability in Xcode + enable background modes

### Testing Push
- CleverTap Dashboard → Messages → Test Push
- Enter device's CleverTap ID (found in SDK debug logs)

---

## Common Tracking Mistakes to Avoid

1. **Sending events before identity**: Always call `onUserLogin` first
2. **Wrong data types**: CleverTap distinguishes string `"150000"` from number `150000` — use numbers for metrics
3. **Missing timestamps**: Use server-side epoch for past events; current time for live events
4. **Duplicate events**: Don't double-fire on both client and server unless deduplicated
5. **PII in event names**: Never put user data in event name; put it in properties
6. **Not flushing**: On app backgrounding, call `flush()` to ensure events are sent
