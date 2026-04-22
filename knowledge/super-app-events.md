# Danh Sách Event Chuẩn Super App

Tất cả event theo định dạng CleverTap: tên event + map thuộc tính.

## Event Chung / Xác Thực

| Event | Thuộc Tính Chính | Ghi Chú |
|-------|-----------------|---------|
| `App Installed` | `platform`, `version` | Tự động track bởi SDK |
| `App Launched` | `platform`, `version`, `session_id` | Tự động track |
| `User Signed Up` | `method` (phone/google/fb), `referral_code` | |
| `User Logged In` | `method` | |
| `User Logged Out` | | |
| `Profile Updated` | `fields_changed[]` | |
| `Permission Granted` | `permission` (location/notification) | |
| `Permission Denied` | `permission` | |

## Event Đặt Đồ Ăn

| Event | Thuộc Tính Chính | Ghi Chú |
|-------|-----------------|---------|
| `Food Home Viewed` | `location`, `lat`, `lng` | |
| `Restaurant Viewed` | `restaurant_id`, `restaurant_name`, `cuisine[]`, `rating`, `delivery_time_min` | |
| `Menu Item Viewed` | `restaurant_id`, `item_id`, `item_name`, `price`, `category` | |
| `Item Added to Cart` | `restaurant_id`, `item_id`, `item_name`, `quantity`, `price`, `cart_total` | |
| `Item Removed from Cart` | `restaurant_id`, `item_id`, `quantity`, `cart_total` | |
| `Cart Viewed` | `restaurant_id`, `cart_total`, `item_count` | |
| `Checkout Started` | `restaurant_id`, `cart_total`, `item_count`, `payment_method` | |
| `Order Placed` | `order_id`, `restaurant_id`, `cart_total`, `payment_method`, `delivery_address_type` | Event chuyển đổi |
| `Order Confirmed` | `order_id`, `estimated_delivery_min` | |
| `Order Picked Up` | `order_id` | |
| `Order Delivered` | `order_id`, `actual_delivery_min`, `rating_shown` | |
| `Order Cancelled` | `order_id`, `cancelled_by`, `reason` | |
| `Order Rated` | `order_id`, `rating`, `comment_given` | |
| `Reorder Tapped` | `order_id`, `restaurant_id` | |
| `Food Cart Abandoned` | `restaurant_id`, `cart_total`, `time_in_cart_min` | Phía server hoặc timer |

## Event Gọi Xe

| Event | Thuộc Tính Chính | Ghi Chú |
|-------|-----------------|---------|
| `Ride Home Viewed` | `location`, `lat`, `lng` | |
| `Destination Entered` | `origin_lat`, `origin_lng`, `dest_lat`, `dest_lng` | |
| `Ride Options Viewed` | `origin`, `destination`, `options[]` (bike/car/premium) | |
| `Ride Fare Estimated` | `vehicle_type`, `estimated_fare`, `estimated_time_min`, `distance_km` | |
| `Ride Requested` | `ride_id`, `vehicle_type`, `estimated_fare`, `payment_method` | Event chuyển đổi |
| `Driver Assigned` | `ride_id`, `driver_id`, `eta_min` | |
| `Ride Started` | `ride_id`, `driver_id` | |
| `Ride Completed` | `ride_id`, `actual_fare`, `duration_min`, `distance_km`, `rating_shown` | |
| `Ride Cancelled` | `ride_id`, `cancelled_by`, `reason`, `stage` (before/after driver assigned) | |
| `Ride Rated` | `ride_id`, `rating`, `tip_given` | |

## Event Ví / Thanh Toán

| Event | Thuộc Tính Chính | Ghi Chú |
|-------|-----------------|---------|
| `Wallet Viewed` | `balance` | |
| `Wallet Topped Up` | `amount`, `method` | |
| `Voucher Applied` | `voucher_code`, `discount_amount`, `order_type` | |
| `Voucher Failed` | `voucher_code`, `reason` | |

## Thuộc Tính Profile User (CleverTap Identity)

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

## Quy Ước Đặt Tên
- Tên event: Title Case có dấu cách (chuẩn CleverTap)
- Thuộc tính: snake_case
- Thuộc tính boolean: tiền tố `is_*`
- Thuộc tính ID: hậu tố `*_id`
- Mảng: hậu tố `*[]` trong tài liệu này nghĩa là multi-value property của CleverTap
