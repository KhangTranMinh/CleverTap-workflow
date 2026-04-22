# Các Loại Campaign CleverTap

## Tổng Quan Kênh

| Kênh | Phù Hợp Nhất | Yêu Cầu |
|------|-------------|---------|
| Push Notification | Tái kích hoạt, cảnh báo thời gian thực | FCM/APNs setup, opt-in |
| In-App Message | Onboarding, giới thiệu tính năng, upsell | Event mở app |
| Email | Hoá đơn, bản tin, winback | Địa chỉ email |
| SMS | OTP, cảnh báo khẩn, tiếp cận rộng | Số điện thoại |
| Webhook | Trigger backend, hệ thống nội bộ | Endpoint URL |
| App Inbox | Tin nhắn lưu trữ không làm phiền | SDK 3.4+ |

## Chế Độ Campaign

### Một Lần (Blast)
- Gửi một lần đến một segment
- Dùng cho: Khuyến mãi, thông báo
- Cài đặt chính: Segment, giờ gửi, frequency cap

### Kích Hoạt (Journey)
- Gửi theo thời gian thực dựa trên event
- Dùng cho: Xác nhận sau đặt hàng, giỏ hàng bỏ dở, chuỗi chào mừng
- Cài đặt chính: Event kích hoạt, độ trễ, điều kiện thoát

### Định Kỳ
- Lên lịch theo cron interval
- Dùng cho: Bản tin hàng tuần, báo cáo hàng tháng, deal hàng ngày

### Giao Dịch
- Kích hoạt qua API 1:1 (dùng endpoint `/send`)
- Dùng cho: OTP, xác nhận đặt xe, hoá đơn
- Lưu ý: Không bị giới hạn DND / frequency cap

## Frequency Capping (Thực Hành Tốt Nhất)
- Push: tối đa 2/ngày, 5/tuần mỗi user
- In-App: tối đa 1 mỗi phiên
- SMS: tối đa 1/ngày
- Email: tối đa 1/ngày cho marketing (giao dịch không giới hạn)

## A/B Testing
- Tỷ lệ phân chia: tối đa 4 biến thể + nhóm kiểm soát
- Tiêu chí thắng: Tỷ lệ click, tỷ lệ chuyển đổi, hoặc goal event tuỳ chỉnh
- Mẫu tối thiểu: Khuyến nghị 1.000 user mỗi biến thể

## Campaign Đặc Thù Super App

### Ngành Dọc Đồ Ăn
- Giỏ hàng bỏ dở: kích hoạt trên `food_cart_abandoned` (trễ 15 phút)
- Nhắc đặt lại: kích hoạt trên `order_delivered` + 3 ngày
- Nhà hàng mới: push theo địa lý đến user trong bán kính giao hàng

### Ngành Dọc Xe
- Cầu cao: push đến user có `last_ride` < 7 ngày ở khu vực cầu cao
- Nhắc an toàn: in-app sau `ride_completed` với user mới
- Ưu đãi: SMS đến tài xế/khách rời bỏ (chưa đặt xe trong 30 ngày)
