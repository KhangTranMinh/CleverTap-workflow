# Tài Liệu Tham Khảo CleverTap REST API

Base URL: `https://api.clevertap.com/1/`

## Xác Thực
Tất cả request cần hai header:
```
X-CleverTap-Account-Id: <account-id-của-bạn>
X-CleverTap-Passcode: <passcode-của-bạn>
Content-Type: application/json
```

Tìm thông tin đăng nhập: CleverTap Dashboard → Settings → Integration → API Credentials

## Giới Hạn Tốc Độ
- Upload event: 1.000 event/request, 60 req/phút
- Truy vấn profile: 30 req/phút
- Kích hoạt campaign: 60 req/phút

---

## API Events

### Upload Event
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

### Lấy Thống Kê Event
`POST /counts/events.json`

```json
{
  "event_name": "Order Placed",
  "from": 20240101,
  "to": 20240131
}
```

---

## API Profile

### Lấy Profile
`GET /profile.json?email=user@example.com`
Hoặc theo identity: `GET /profile.json?identity=user123`

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

## API Segment / Danh Sách

### Tạo Danh Sách (Segment Tĩnh)
`POST /lists/create.json`

```json
{
  "name": "User Đồ Ăn Rời Bỏ",
  "description": "User chưa đặt đồ ăn trong 30 ngày",
  "source": "manual",
  "users": [
    { "identity": "user1" },
    { "identity": "user2" }
  ]
}
```

Kết quả: `{ "status": "success", "list_id": "abc123" }`

### Lấy Danh Sách
`GET /lists/get.json?list_id=abc123`

---

## API Campaign

### Tạo Campaign (Push Một Lần)
`POST /targets/create.json`

```json
{
  "name": "Khuyến Mãi Cuối Tuần",
  "where": {
    "event_name": "App Launched",
    "from": 20240101,
    "to": 20240131
  },
  "when": "2024-01-20 10:00",
  "content": {
    "title": "Deal Cuối Tuần!",
    "body": "Giảm 30% cho đơn đồ ăn tiếp theo của bạn",
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

### Danh Sách Campaign
`GET /targets/list.json?from=20240101&to=20240131`

### Lấy Thống Kê Campaign
`GET /targets/<campaign_id>/result.json`

Kết quả gồm: `sent`, `delivered`, `opened`, `clicked`, `converted`

---

## Push Giao Dịch (Kích Hoạt Qua API)
`POST /send/push.json`

```json
{
  "to": {
    "identity": ["user123"]
  },
  "tag_group": "default",
  "respect_frequency_caps": false,
  "content": {
    "title": "Đơn hàng của bạn đã được xác nhận!",
    "body": "Đơn #ORD-001 đang được chuẩn bị",
    "platform_specific": {
      "android": {
        "deep_link": "app://food/orders/ORD-001"
      }
    }
  }
}
```

---

## Webhook (Đầu Ra)
Cấu hình tại: Dashboard → Settings → Integration → Webhooks

CleverTap sẽ POST đến endpoint của bạn khi có event campaign (sent, delivered, clicked, converted).

Ví dụ payload:
```json
{
  "event": "push_delivered",
  "campaign_id": "123",
  "identity": "user123",
  "timestamp": 1700000000
}
```

---

## Mã Phản Hồi Phổ Biến
| Mã | Ý Nghĩa |
|----|---------|
| 200 | Thành công |
| 400 | Request không hợp lệ (kiểm tra payload) |
| 401 | Xác thực thất bại (kiểm tra header) |
| 429 | Vượt giới hạn tốc độ |
| 500 | Lỗi server CleverTap |
