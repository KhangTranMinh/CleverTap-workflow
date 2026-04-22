# Hướng Dẫn Triển Khai Event Tracking

## Cài Đặt SDK

### Android (Kotlin)
```kotlin
// Application.onCreate
CleverTapAPI.setDebugLevel(CleverTapAPI.LogLevel.DEBUG)
val cleverTap = CleverTapAPI.getDefaultInstance(context)

// Xác định user sau khi đăng nhập
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

// Xác định user
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

## Checklist QA Cho Event Tracking

Trước khi đưa vào production, kiểm tra từng event:

- [ ] Tên event khớp chính xác với spec (phân biệt chữ hoa/thường)
- [ ] Tất cả thuộc tính bắt buộc có mặt
- [ ] Kiểu dữ liệu thuộc tính đúng (string, number, boolean)
- [ ] Identity được set trước event đầu tiên (nếu không event sẽ là ẩn danh)
- [ ] Event hiển thị trong CleverTap dashboard trong vòng 5 phút
- [ ] Kiểm tra trên cả Android và iOS
- [ ] Xác minh trong CleverTap → Events → Live View

---

## Xác Minh Trên CleverTap Dashboard

**Live View**: Dashboard → Events → Live View
- Xem event đến theo thời gian thực
- Dùng để QA trong quá trình phát triển

**Event Explorer**: Dashboard → Events → Event Explorer
- Lịch sử khối lượng event
- Phân tích theo thuộc tính

**Funnel Analysis**: Dashboard → Analytics → Funnels
- Xây dựng: Home Viewed → Cart Viewed → Checkout Started → Order Placed

---

## Schema Deep Link

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

iOS: Cần cài đặt Universal Links + entitlement Associated Domains
Android: Cần intent-filter trong AndroidManifest.xml

---

## Cài Đặt Push Notification

### Android FCM
1. Tạo Firebase project → Tải `google-services.json`
2. Thêm vào CleverTap Dashboard: Settings → Mobile Push → Android
3. Dán FCM Server Key

### iOS APNs
1. Tạo APNs Auth Key (p8) trong Apple Developer portal
2. Upload lên CleverTap: Settings → Mobile Push → iOS
3. Thêm Push capability trong Xcode + bật background modes

### Kiểm Thử Push
- CleverTap Dashboard → Messages → Test Push
- Nhập CleverTap ID của thiết bị (tìm trong SDK debug log)

---

## Các Lỗi Tracking Thường Gặp Cần Tránh

1. **Gửi event trước khi set identity**: Luôn gọi `onUserLogin` trước
2. **Sai kiểu dữ liệu**: CleverTap phân biệt string `"150000"` với number `150000` — dùng number cho các chỉ số
3. **Thiếu timestamp**: Dùng epoch phía server cho event quá khứ; thời gian hiện tại cho event live
4. **Event trùng lặp**: Không bắn cả client lẫn server trừ khi có deduplication
5. **PII trong tên event**: Không bao giờ đặt dữ liệu user vào tên event; đặt vào thuộc tính
6. **Không flush**: Khi app vào nền, gọi `flush()` để đảm bảo event được gửi đi
