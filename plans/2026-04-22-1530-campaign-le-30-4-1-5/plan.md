# Campaign Dịp Lễ 30/4 - 1/5

## Tổng Quan
Gửi 3 đợt push notification đến toàn bộ user đang hoạt động trong dịp lễ 30/4 - 1/5. Không có voucher — tập trung vào việc nhắc nhở và tạo cảm hứng đặt đồ ăn tại nhà (30/4) và di chuyển vui chơi (1/5). Mỗi đợt push có thông điệp riêng phù hợp với hành vi ngày đó.

---

## Mục Tiêu & KPI

| Mục Tiêu | Chỉ Tiêu | Đo Lường |
|----------|----------|---------|
| Tăng đơn đồ ăn ngày 30/4 | Tăng 20% so với thứ Tư thông thường | Event `Order Placed` trong ngày 30/4 |
| Tăng chuyến xe ngày 1/5 | Tăng 20% so với thứ Năm thông thường | Event `Ride Requested` trong ngày 1/5 |
| CTR push tổng thể | ≥ 4% trên cả 3 đợt | Tỷ lệ click / delivered |

**Event Thành Công**: `Order Placed` (30/4), `Ride Requested` (1/5)
**Baseline**: Số đơn/chuyến trung bình thứ Tư-Năm trong tháng 4/2026

---

## Audience Segment

**Tên Segment**: `User Hoạt Động Tháng 4/2026`
**Ước Tính Kích Thước**: Toàn bộ user hoạt động

```yaml
filters:
  - type: event
    event: "App Launched"
    condition: did_at_least
    count: 1
    period: last_30_days
```

> Dùng một segment duy nhất cho cả 3 đợt push. Không phân tách theo ngành dọc vì đây là super app — mỗi push sẽ nhắc cả hai tính năng.

---

## Chi Tiết Campaign — 3 Đợt Push

### Đợt 1: 29/4 20:00 — Nhắc Trước Lễ
**Tiêu Đề**: `Ngày mai nghỉ lễ rồi! 🎉`
**Nội Dung**: `Đặt đồ ăn tối nay hoặc lên kế hoạch di chuyển dịp lễ ngay trên app nhé!`
**CTA**: Mở App
**Deep Link**: `app://food/home`
**Mục đích**: Tạo nhận thức, kéo user mở app trước kỳ nghỉ

### Đợt 2: 30/4 09:00 — Ngày Giải Phóng
**Tiêu Đề**: `Chúc mừng ngày 30/4! 🇻🇳`
**Nội Dung**: `Nghỉ lễ ở nhà cùng gia đình — đặt đồ ăn ngon giao tận nơi, không cần ra ngoài!`
**CTA**: Đặt Đồ Ăn
**Deep Link**: `app://food/home`
**Mục đích**: Tập trung đồ ăn — ngày 30/4 người dùng thường ở nhà tụ họp gia đình

### Đợt 3: 01/5 09:00 — Ngày Quốc Tế Lao Động
**Tiêu Đề**: `Chúc mừng ngày Quốc tế Lao động! 🌟`
**Nội Dung**: `Ngày nghỉ hiếm hoi — ra ngoài vui chơi đi! Đặt xe nhanh, đến nơi đúng giờ.`
**CTA**: Đặt Xe
**Deep Link**: `app://ride/home`
**Mục đích**: Tập trung xe — ngày 1/5 người dùng thường đi chơi, du lịch ngắn ngày

| Đợt | Ngày Giờ | Tiêu Đề | Focus | Deep Link |
|-----|---------|---------|-------|-----------|
| 1 | 29/4 20:00 | Ngày mai nghỉ lễ rồi! | Chung | `app://food/home` |
| 2 | 30/4 09:00 | Chúc mừng ngày 30/4! | Đồ ăn | `app://food/home` |
| 3 | 01/5 09:00 | Chúc mừng ngày Quốc tế LĐ! | Xe | `app://ride/home` |

**Frequency Cap**: 1 push/ngày/user
**Respect DND**: Có

---

## Tracking Events

| Event | Trạng Thái | Ghi Chú |
|-------|-----------|---------|
| `Order Placed` | Đã có | Đo chuyển đổi đồ ăn ngày 30/4 |
| `Ride Requested` | Đã có | Đo chuyển đổi xe ngày 1/5 |
| `App Launched` | Đã có | Dùng làm filter segment |

Không cần event mới cho campaign này.

---

## Công Việc

| Công Việc | Mô Tả | Người Thực Hiện | Điểm | Deadline |
|-----------|-------|-----------------|------|----------|
| Tạo segment user hoạt động | Filter: đã mở app ít nhất 1 lần trong 30 ngày qua | Minh | 1 | 2026-04-25 |
| Setup đợt push 1 (29/4 20:00) | Cấu hình push nhắc trước lễ, deep link app://food/home | Linh | 1 | 2026-04-27 |
| Setup đợt push 2 (30/4 09:00) | Cấu hình push ngày 30/4, deep link đồ ăn | Đức | 1 | 2026-04-27 |
| Setup đợt push 3 (01/5 09:00) | Cấu hình push ngày 1/5, deep link đặt xe | Minh | 1 | 2026-04-27 |
| QA 3 đợt push | Kiểm tra nội dung, deep link, giờ gửi đúng trên staging | Linh | 2 | 2026-04-28 |
| Theo dõi và báo cáo kết quả | Kéo số liệu sau từng đợt, tổng hợp báo cáo sau 1/5 | Đức | 1 | 2026-05-02 |

---

## Timeline

| Mốc | Ngày |
|-----|------|
| Xác nhận kế hoạch | 2026-04-22 |
| Tạo segment xong | 2026-04-25 |
| Setup 3 campaign xong | 2026-04-27 |
| QA sign-off | 2026-04-28 |
| Đợt push 1 — Nhắc trước lễ | 2026-04-29 20:00 |
| Đợt push 2 — Ngày 30/4 | 2026-04-30 09:00 |
| Đợt push 3 — Ngày 1/5 | 2026-05-01 09:00 |
| Tổng hợp báo cáo | 2026-05-02 |

---

## Rủi Ro & Ghi Chú

- **Rủi ro**: Nếu gửi cả 3 đợt trong 3 ngày liên tiếp, user có thể cảm thấy spam — frequency cap 1/ngày là bắt buộc
- **Rủi ro**: Deep link đặt xe (`app://ride/home`) cần đảm bảo hoạt động đúng trên cả Android và iOS trước ngày 28/4
- **Ghi chú**: Giờ gửi 09:00 sáng là tối ưu cho ngày nghỉ — user thức dậy muộn hơn ngày thường
- **Ghi chú**: Đợt 1 (29/4 tối) cần gửi sau 19:00 để không bị DND nhưng trước khi user ngủ
- **Ghi chú**: Không dùng ưu đãi giảm giá để tránh tạo kỳ vọng cho các dịp lễ sau
