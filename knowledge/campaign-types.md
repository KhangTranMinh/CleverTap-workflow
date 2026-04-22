# CleverTap Campaign Types

## Channel Overview

| Channel | Best For | Requires |
|---------|----------|----------|
| Push Notification | Re-engagement, time-sensitive alerts | FCM/APNs setup, opt-in |
| In-App Message | Onboarding, feature discovery, upsell | App open event |
| Email | Receipts, newsletters, winback | Email address |
| SMS | OTP, urgent alerts, high-reach | Phone number |
| Webhook | Backend triggers, internal systems | Endpoint URL |
| App Inbox | Non-intrusive persistent messages | SDK 3.4+ |

## Campaign Modes

### One-Time (Blast)
- Single send to a segment
- Use for: Promotions, announcements
- Key settings: Segment, schedule time, frequency cap

### Triggered (Journey)
- Event-based real-time delivery
- Use for: Post-order confirmations, abandoned cart, welcome series
- Key settings: Trigger event, delay, exit conditions

### Recurring
- Scheduled on a cron interval
- Use for: Weekly digests, monthly reports, daily deals

### Transactional
- 1:1 API-triggered (via `/send` endpoint)
- Use for: OTP, booking confirmations, receipts
- Note: Not subject to DND / frequency caps

## Frequency Capping (Best Practices)
- Push: max 2/day, 5/week per user
- In-App: max 1 per session
- SMS: max 1/day
- Email: max 1/day for marketing (transactional unlimited)

## A/B Testing
- Variant split: up to 4 variants + control
- Winning criteria: Click rate, conversion rate, or custom goal event
- Min sample: 1,000 users per variant recommended

## Super App Specific Campaigns

### Food Vertical
- Abandoned cart: trigger on `food_cart_abandoned` (15 min delay)
- Reorder nudge: trigger on `order_delivered` + 3 days
- New restaurant: geo-targeted push to users in delivery radius

### Ride Vertical
- Demand surge: push to users with `last_ride` < 7 days in high-demand area
- Safety reminder: in-app after `ride_completed` for new users
- Promo offer: SMS to churned riders (no ride in 30 days)
