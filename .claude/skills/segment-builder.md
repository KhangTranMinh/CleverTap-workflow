# Skill: segment-builder

Khi người dùng gọi `/segment-builder` hoặc yêu cầu định nghĩa/xây dựng audience segment:

## Bước 1 — Hiểu Đối Tượng

Hỏi (nếu chưa được cung cấp):
- Chúng ta nhắm đến ai? (mô tả bằng ngôn ngữ thông thường)
- Ngành dọc nào? (đồ ăn / xe / cả hai)
- Tiêu chí hành vi? (event đã làm/chưa làm, tần suất)
- Gần đây? (7 ngày / 30 ngày / tất cả thời gian)
- Thuộc tính profile? (thành phố, loại user, phương thức thanh toán)

## Bước 2 — Chuyển Đổi Sang CleverTap Filter

Xây dựng định nghĩa segment bằng hệ thống filter của CleverTap:

### Filter Theo Event
```
Đã thực hiện event "Order Placed" ít nhất 3 lần trong 30 ngày qua
VÀ Chưa thực hiện event "Order Placed" trong 7 ngày qua
```

### Filter Theo Property
```
User Property: custom_user_type = "food_only"
User Property: total_food_orders > 5
```

### Ví Dụ Kết Hợp — User Đồ Ăn Tích Cực Đã Rời Bỏ
```
Đã thực hiện "Order Placed" ít nhất 5 lần (tất cả thời gian)
VÀ Chưa thực hiện "Order Placed" trong 30 ngày qua
VÀ User Property: total_food_orders > 5
```

## Bước 3 — Ước Tính Kích Thước Segment

Hướng dẫn người dùng kiểm tra kích thước trên CleverTap dashboard:
Dashboard → Segments → Create → Áp dụng filter → Xem ước tính số lượng

Quy tắc chung:
- < 1.000 user: Quá nhỏ để có ý nghĩa thống kê trong A/B test
- 1.000–10.000: Tốt cho campaign nhắm mục tiêu
- 10.000+: Cân nhắc phân đoạn thêm để cá nhân hóa

## Bước 4 — Xuất Đặc Tả Segment

Tạo khối đặc tả segment để đưa vào kế hoạch:

```yaml
segment:
  name: "User Đồ Ăn Tích Cực Đã Rời Bỏ"
  description: "User có 5+ đơn hàng nhưng không hoạt động 30+ ngày"
  filters:
    - type: event
      event: "Order Placed"
      condition: did_at_least
      count: 5
      period: ever
    - type: event
      event: "Order Placed"
      condition: did_not_do
      period: last_30_days
    - type: property
      property: total_food_orders
      operator: greater_than
      value: 5
  estimated_size: ~50.000
```

## Bước 5 — Gợi Ý Cá Nhân Hóa

Dựa trên segment, đề xuất cá nhân hóa nội dung message:
- Dùng `{{name}}` cho lời chào
- Tham chiếu đơn hàng gần nhất: `{{last_order_restaurant}}`
- Dùng ưu đãi theo vị trí nếu có thuộc tính địa lý
