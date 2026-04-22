# Skill: campaign-setup

Khi người dùng gọi `/campaign-setup` hoặc yêu cầu setup campaign qua CleverTap API:

## Bước 1 — Xác Nhận Thông Tin Đăng Nhập

Kiểm tra `scripts/.env` có tồn tại và có thông tin CleverTap không:
```
CLEVERTAP_ACCOUNT_ID=...
CLEVERTAP_PASSCODE=...
```

Nếu thiếu, yêu cầu người dùng điền vào trước khi tiếp tục.

## Bước 2 — Xác Định Cần Setup Gì

Hỏi người dùng muốn thực thi kế hoạch nào, hoặc đọc plan đã xác nhận gần nhất từ `plans/`.

Xác định cần tạo gì:
- **Segment** — nếu plan định nghĩa audience filter
- **Campaign** — push notification, in-app message, v.v.
- **Cả hai**

## Bước 3 — Chạy Script Setup

Tạo segment:
```bash
python3 scripts/campaign_setup.py --plan plans/<thư-mục>/plan.md --action create-segment
```

Tạo campaign:
```bash
python3 scripts/campaign_setup.py --plan plans/<thư-mục>/plan.md --action create-campaign
```

Tạo cả hai:
```bash
python3 scripts/campaign_setup.py --plan plans/<thư-mục>/plan.md --action all
```

## Bước 4 — Xác Minh và Báo Cáo

Sau khi setup, chạy:
```bash
python3 scripts/campaign_setup.py --action verify --campaign-id <id>
```

Báo cáo lại với ID tài nguyên đã tạo và link đến CleverTap dashboard.

## Bước 5 — Lên Lịch Theo Dõi

Hỏi: "Bạn có muốn tôi kiểm tra hiệu quả campaign sau khi launch không? Tôi có thể kéo số liệu bằng `/campaign-report`."

## Lưu Ý
- Luôn tạo segment trước, rồi mới tạo campaign
- Với campaign lặp lại, kiểm tra cron expression trước khi submit
- Campaign transactional bỏ qua frequency cap — xác nhận với người dùng trước khi dùng
