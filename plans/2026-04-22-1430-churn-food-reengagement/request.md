# Yêu Cầu

**Ngày**: 2026-04-22 14:30
**Người yêu cầu**: Khang

## Yêu Cầu Ban Đầu
Tôi muốn kéo lại những user đồ ăn đã lâu không đặt hàng. Họ từng đặt thường xuyên nhưng đã im lặng trong tháng qua. Muốn gửi cho họ thứ gì đó để kéo họ quay lại — có thể là giảm giá.

## Làm Rõ
- **Đối tượng**: User có 3+ đơn hàng trong quá khứ, không đặt hàng trong 30 ngày qua
- **Kênh**: Push notification
- **Ưu đãi**: A/B test giảm 20% vs 30% để tìm mức chi phí hiệu quả nhất
- **Thời gian**: Launch 2026-04-28, xem kết quả sau 48h
- **Chỉ số thành công**: Event `Order Placed` trong vòng 7 ngày sau push
