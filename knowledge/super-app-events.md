# Super App Standard Events

All events follow CleverTap's format: event name + property map.

## Global / Auth Events

| Event | Key Properties | Notes |
|-------|---------------|-------|
| `App Installed` | `platform`, `version` | Auto-tracked by SDK |
| `App Launched` | `platform`, `version`, `session_id` | Auto-tracked |
| `User Signed Up` | `method` (phone/google/fb), `referral_code` | |
| `User Logged In` | `method` | |
| `User Logged Out` | | |
| `Profile Updated` | `fields_changed[]` | |
| `Permission Granted` | `permission` (location/notification) | |
| `Permission Denied` | `permission` | |

## Food Ordering Events

| Event | Key Properties | Notes |
|-------|---------------|-------|
| `Food Home Viewed` | `location`, `lat`, `lng` | |
| `Restaurant Viewed` | `restaurant_id`, `restaurant_name`, `cuisine[]`, `rating`, `delivery_time_min` | |
| `Menu Item Viewed` | `restaurant_id`, `item_id`, `item_name`, `price`, `category` | |
| `Item Added to Cart` | `restaurant_id`, `item_id`, `item_name`, `quantity`, `price`, `cart_total` | |
| `Item Removed from Cart` | `restaurant_id`, `item_id`, `quantity`, `cart_total` | |
| `Cart Viewed` | `restaurant_id`, `cart_total`, `item_count` | |
| `Checkout Started` | `restaurant_id`, `cart_total`, `item_count`, `payment_method` | |
| `Order Placed` | `order_id`, `restaurant_id`, `cart_total`, `payment_method`, `delivery_address_type` | Conversion event |
| `Order Confirmed` | `order_id`, `estimated_delivery_min` | |
| `Order Picked Up` | `order_id` | |
| `Order Delivered` | `order_id`, `actual_delivery_min`, `rating_shown` | |
| `Order Cancelled` | `order_id`, `cancelled_by`, `reason` | |
| `Order Rated` | `order_id`, `rating`, `comment_given` | |
| `Reorder Tapped` | `order_id`, `restaurant_id` | |
| `Food Cart Abandoned` | `restaurant_id`, `cart_total`, `time_in_cart_min` | Server-side or timer |

## Ride Hailing Events

| Event | Key Properties | Notes |
|-------|---------------|-------|
| `Ride Home Viewed` | `location`, `lat`, `lng` | |
| `Destination Entered` | `origin_lat`, `origin_lng`, `dest_lat`, `dest_lng` | |
| `Ride Options Viewed` | `origin`, `destination`, `options[]` (bike/car/premium) | |
| `Ride Fare Estimated` | `vehicle_type`, `estimated_fare`, `estimated_time_min`, `distance_km` | |
| `Ride Requested` | `ride_id`, `vehicle_type`, `estimated_fare`, `payment_method` | Conversion event |
| `Driver Assigned` | `ride_id`, `driver_id`, `eta_min` | |
| `Ride Started` | `ride_id`, `driver_id` | |
| `Ride Completed` | `ride_id`, `actual_fare`, `duration_min`, `distance_km`, `rating_shown` | |
| `Ride Cancelled` | `ride_id`, `cancelled_by`, `reason`, `stage` (before/after driver assigned) | |
| `Ride Rated` | `ride_id`, `rating`, `tip_given` | |

## Wallet / Payment Events

| Event | Key Properties | Notes |
|-------|---------------|-------|
| `Wallet Viewed` | `balance` | |
| `Wallet Topped Up` | `amount`, `method` | |
| `Voucher Applied` | `voucher_code`, `discount_amount`, `order_type` | |
| `Voucher Failed` | `voucher_code`, `reason` | |

## User Profile Properties (CleverTap Identity)

```json
{
  "Name": "string",
  "Phone": "+84xxxxxxxxx",
  "Email": "string",
  "Identity": "user_id",
  "DOB": "YYYYMMDD",
  "Gender": "M|F|O",
  "City": "string",
  "Country": "VN",
  "custom_user_type": "food_only|ride_only|both",
  "total_food_orders": "number",
  "total_rides": "number",
  "last_order_date": "epoch",
  "last_ride_date": "epoch",
  "preferred_payment": "string",
  "home_lat": "number",
  "home_lng": "number",
  "work_lat": "number",
  "work_lng": "number"
}
```

## Naming Conventions
- Event names: Title Case with spaces (CleverTap standard)
- Properties: snake_case
- Boolean properties: `is_*` prefix
- ID properties: `*_id` suffix
- Arrays: `*[]` suffix in this doc means CleverTap multi-value property
