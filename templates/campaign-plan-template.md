# [Tên Campaign]

## Tổng Quan
[Tóm tắt một đoạn về campaign, mục tiêu và tác động kỳ vọng]

---

## Mục Tiêu & KPI

| Mục Tiêu | Chỉ Tiêu | Đo Lường |
|----------|----------|---------|
| [ví dụ: Kéo lại user đồ ăn rời bỏ] | [ví dụ: Tỷ lệ chuyển đổi 5%] | [ví dụ: Event "Order Placed"] |

**Event Thành Công**: [Tên event để theo dõi chuyển đổi]
**Baseline**: [Chỉ số hiện tại trước campaign]

---

## Audience Segment

**Tên Segment**: [Tên trong CleverTap]
**Ước Tính Kích Thước**: [~X user]

```yaml
filters:
  - type: event
    event: "[Tên Event]"
    condition: did_not_do
    period: last_30_days
  - type: property
    property: [tên_thuộc_tính]
    operator: greater_than
    value: [giá trị]
```

---

## Chi Tiết Campaign

**Kênh**: [Push / In-App / Email / SMS]
**Lịch Gửi**: [YYYY-MM-DD HH:MM hoặc "Kích hoạt khi [event]"]
**Frequency Cap**: [ví dụ: 1 lần/user]
**Respect DND**: [Có / Không]

**Tiêu Đề**: [Tiêu đề push hoặc chủ đề email]
**Nội Dung**: [Nội dung message]
**CTA**: [Văn bản nút nếu có]
**Deep Link**: [app://...]

### Biến Thể (A/B Test)
| Biến Thể | Tiêu Đề | Nội Dung | CTR Kỳ Vọng |
|----------|---------|---------|------------|
| A (Kiểm soát) | | | |
| B | | | |

---

## Tracking Events

| Event | Trạng Thái | Người Phụ Trách |
|-------|-----------|----------------|
| [Tên event mới] | Mới (cần instrument) | Đức |
| [Event hiện có] | Đã có | — |

---

## Công Việc

| Công Việc | Mô Tả | Người Thực Hiện | Điểm | Deadline |
|-----------|-------|-----------------|------|----------|
| Tạo segment trong CleverTap | Xây dựng audience filter theo spec trên | Minh | 1 | YYYY-MM-DD |
| Setup campaign trong CleverTap | Cấu hình push với nội dung, lịch, A/B | Linh | 2 | YYYY-MM-DD |
| Instrument [event] trên Android/iOS | Thêm SDK call theo tracking spec | Đức | 3 | YYYY-MM-DD |
| QA event tracking | Xác minh event trong Live View trên cả hai nền tảng | Minh | 2 | YYYY-MM-DD |
| Theo dõi sau launch | Kéo số liệu 48h, báo cáo bất thường | Linh | 1 | YYYY-MM-DD |

---

## Timeline

| Mốc | Ngày |
|-----|------|
| Xác nhận kế hoạch | YYYY-MM-DD |
| Instrument tracking event xong | YYYY-MM-DD |
| Cấu hình campaign xong | YYYY-MM-DD |
| QA sign-off | YYYY-MM-DD |
| Launch | YYYY-MM-DD |
| Review hiệu quả lần đầu | YYYY-MM-DD (48h sau launch) |

---

## Rủi Ro & Ghi Chú

- **Rủi ro**: [ví dụ: Tỷ lệ opt-in push thấp trong segment này — cân nhắc SMS dự phòng]
- **Phụ thuộc**: [ví dụ: Cần deep link route mới từ Đức trước]
- **Ghi chú**: [ví dụ: Phối hợp với product team về landing page]
