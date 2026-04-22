# Campaign Kéo Lại User Đồ Ăn Rời Bỏ

## Tổng Quan
Kéo lại những user đồ ăn đã đặt ít nhất 3 đơn trong quá khứ nhưng không hoạt động trong 30 ngày qua. Chúng ta sẽ gửi push notification cá nhân hóa kèm voucher giảm giá để kéo họ quay lại. A/B test hai mức ưu đãi (giảm 20% vs 30%) để tìm mức khuyến khích hiệu quả nhất về chi phí.

---

## Mục Tiêu & KPI

| Mục Tiêu | Chỉ Tiêu | Đo Lường |
|----------|----------|---------|
| Kéo lại user đồ ăn rời bỏ | Tỷ lệ chuyển đổi 8% | Event `Order Placed` trong vòng 7 ngày sau push |
| Tối thiểu chi phí giảm giá | Dùng mức ưu đãi thấp nhất có hiệu quả | So sánh chuyển đổi giữa biến thể A và B |

**Event Thành Công**: `Order Placed`
**Baseline**: 0 đơn hàng trong 30 ngày qua

---

## Audience Segment

**Tên Segment**: `User Đồ Ăn Tích Cực Đã Rời Bỏ - Tháng 4/2026`
**Ước Tính Kích Thước**: ~45.000 user

```yaml
filters:
  - type: event
    event: "Order Placed"
    condition: did_at_least
    count: 3
    period: ever
  - type: event
    event: "Order Placed"
    condition: did_not_do
    period: last_30_days
  - type: property
    property: custom_user_type
    operator: contains
    value: food
```

---

## Chi Tiết Campaign

**Kênh**: Push Notification
**Lịch Gửi**: 2026-04-28 11:00 (giờ địa phương)
**Frequency Cap**: 1 lần/user
**Respect DND**: Có

### Biến Thể A (Kiểm soát — Giảm 20%)
**Tiêu Đề**: `Chúng tôi nhớ bạn, {{name}}! 🍔`
**Nội Dung**: `Đã lâu rồi nhỉ. Quay lại và nhận ngay ưu đãi giảm 20% cho đơn đồ ăn tiếp theo hôm nay.`
**CTA**: Đặt Ngay
**Deep Link**: `app://food/promo?code=BACK20`

### Biến Thể B (Giảm 30%)
**Tiêu Đề**: `Chúng tôi nhớ bạn, {{name}}! 🍔`
**Nội Dung**: `Ưu đãi đặc biệt chỉ dành cho bạn — Giảm 30% đơn đồ ăn tiếp theo. Hôm nay thôi!`
**CTA**: Nhận Ưu Đãi
**Deep Link**: `app://food/promo?code=BACK30`

| Biến Thể | Ưu Đãi | CTR Kỳ Vọng | Chuyển Đổi Kỳ Vọng |
|----------|--------|------------|-------------------|
| A | Giảm 20% | 4% | 7% |
| B | Giảm 30% | 5% | 10% |

---

## Tracking Events

| Event | Trạng Thái | Ghi Chú |
|-------|-----------|---------|
| `Order Placed` | Đã có | Event chuyển đổi chính |
| `Voucher Applied` | Đã có | Theo dõi việc dùng mã BACK20 / BACK30 |
| `Voucher Failed` | Đã có | Theo dõi lỗi voucher lúc thanh toán |

Không cần event mới cho campaign này.

---

## Công Việc

| Công Việc | Mô Tả | Người Thực Hiện | Điểm | Deadline |
|-----------|-------|-----------------|------|----------|
| Tạo segment trong CleverTap | Xây dựng audience filter: 3+ đơn tất cả thời gian, không đặt trong 30 ngày, loại user đồ ăn | Minh | 1 | 2026-04-25 |
| Setup A/B push campaign | Cấu hình 2 biến thể với nội dung, mã voucher, deep link, lịch gửi 11:00 | Linh | 2 | 2026-04-27 |
| Xác nhận mã voucher với product team | Xác nhận BACK20 và BACK30 đang hoạt động và có giới hạn sử dụng | Đức | 1 | 2026-04-25 |
| QA campaign trên staging | Gửi test push đến thiết bị nội bộ, xác minh deep link và voucher hoạt động đúng | Minh | 2 | 2026-04-27 |
| Theo dõi 48h sau launch | Kéo số liệu delivery, CTR, chuyển đổi; đánh dấu bất thường | Linh | 1 | 2026-04-30 |

---

## Timeline

| Mốc | Ngày |
|-----|------|
| Xác nhận kế hoạch | 2026-04-22 |
| Xác nhận mã voucher | 2026-04-25 |
| Tạo segment xong | 2026-04-25 |
| Cấu hình campaign xong | 2026-04-27 |
| QA sign-off | 2026-04-27 |
| Launch | 2026-04-28 11:00 |
| Review hiệu quả lần đầu | 2026-04-30 (48h sau launch) |

---

## Rủi Ro & Ghi Chú

- **Rủi ro**: Tỷ lệ opt-in push của user rời bỏ có thể thấp hơn trung bình — dự kiến deliverability ~60%
- **Rủi ro**: Gộp voucher — đảm bảo BACK20/BACK30 không thể kết hợp với các promo đang chạy
- **Phụ thuộc**: Product team phải xác nhận mã voucher đang hoạt động trước khi campaign chạy
- **Ghi chú**: Nếu CTR biến thể B > 2 lần biến thể A, cân nhắc rollout ưu đãi 30% cho toàn bộ segment
