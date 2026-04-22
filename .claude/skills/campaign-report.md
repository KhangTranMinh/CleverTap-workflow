# Skill: campaign-report

Khi người dùng gọi `/campaign-report` hoặc hỏi về kết quả/số liệu campaign:

## Bước 1 — Xác Định Campaign

Hỏi campaign nào cần báo cáo nếu chưa chỉ định. Các lựa chọn:
- Theo tên campaign (tìm campaign ID trong `plans/`)
- Theo CleverTap campaign ID trực tiếp
- Tất cả campaign trong một khoảng thời gian

## Bước 2 — Kéo Số Liệu

Chạy script báo cáo:
```bash
python3 scripts/campaign_report.py --campaign-id <id>
```

Hoặc theo khoảng thời gian:
```bash
python3 scripts/campaign_report.py --from 2024-01-01 --to 2024-01-31
```

## Bước 3 — Trình Bày Báo Cáo

Trình bày kết quả theo định dạng:

### Campaign: {Tên}
**Giai đoạn**: {khoảng thời gian}
**Kênh**: {push/email/sms/in-app}

| Chỉ số | Số lượng | Tỷ lệ |
|--------|----------|-------|
| Đã gửi | X | 100% |
| Đã nhận | X | X% |
| Đã mở | X | X% |
| Đã click | X | X% |
| Đã chuyển đổi | X | X% |

**Event mục tiêu**: {tên event} — {số lượng} chuyển đổi
**Tác động doanh thu**: {nếu có}

### Phân Tích
- So sánh CTR/chuyển đổi với chuẩn benchmark (Push: CTR 3–5%, Email: open 20%)
- Đánh dấu chỉ số kém hiệu quả
- Đề xuất hành động tiếp theo (A/B test nội dung, điều chỉnh giờ gửi, tinh chỉnh segment)

## Bước 4 — Khuyến Nghị

Dựa trên hiệu quả:
- Nếu CTR < 2% trên push: Đề xuất A/B test nội dung hoặc tinh chỉnh segment
- Nếu tỷ lệ nhận < 70%: Kiểm tra push token có hợp lệ không / email bounce
- Nếu chuyển đổi < mục tiêu: Kiểm tra deep link, landing page, độ phù hợp của ưu đãi

Luôn kết thúc bằng: "Bạn có muốn tôi tạo campaign tiếp theo hoặc kế hoạch tinh chỉnh segment không?"

## Benchmark (Super App)
| Kênh | Tỷ lệ mở | CTR | Chuyển đổi |
|------|----------|-----|------------|
| Push | 15–25% | 3–5% | 1–3% |
| In-App | 80–90% | 10–15% | 5–10% |
| Email | 20–30% | 2–4% | 0.5–2% |
| SMS | 90–95% | 5–8% | 2–5% |
