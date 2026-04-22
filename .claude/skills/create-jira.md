# Skill: create-jira

Khi người dùng gọi `/create-jira` hoặc xác nhận plan và yêu cầu tạo ticket:

## Bước 1 — Đọc Kế Hoạch

Đọc `plan.md` trong thư mục plan mà người dùng đã xác nhận. Nếu không chỉ định thư mục nào, liệt kê các thư mục trong `plans/` và hỏi.

## Bước 2 — Trích Xuất Công Việc

Từ phần Công việc trong plan, trích xuất mỗi task với:
- Tiêu đề
- Mô tả (từ nội dung plan)
- Người thực hiện (Minh / Linh / Đức)
- Story point
- Label: `clevertap`, `crm`, và một trong `campaign` / `tracking` / `engineering`
- Epic link (dùng tên plan làm epic)
- Ngày deadline (từ timeline plan)

## Bước 3 — Tạo Ticket

Chạy script tạo Jira:
```bash
cd /Users/khangtran/Documents/CleverTap-workflow
python3 scripts/create_jira_tickets.py --plan plans/<tên-thư-mục>/plan.md
```

Nếu script chưa được cấu hình (thiếu `.env`), thông báo cho người dùng:

> Để tạo Jira ticket, tôi cần thông tin đăng nhập Jira. Vui lòng điền vào `scripts/.env`:
> ```
> JIRA_URL=https://yourcompany.atlassian.net
> JIRA_EMAIL=your@email.com
> JIRA_API_TOKEN=your-api-token
> JIRA_PROJECT_KEY=CRM
> ```
> Sau đó chạy: `python3 scripts/create_jira_tickets.py --plan plans/<thư-mục>/plan.md`

## Bước 4 — Ghi jira_tickets.md và Cập Nhật history.md

Tạo file `jira_tickets.md` trong thư mục plan:

```markdown
# Jira Tickets — [Tên Campaign]

**Epic**: [key]
**Ngày tạo**: YYYY-MM-DD HH:MM

| Ticket | Tiêu đề | Người thực hiện | Điểm | Deadline | Trạng thái |
|--------|---------|-----------------|------|----------|------------|
| CRM-XX | ... | Minh | 2 | YYYY-MM-DD | To Do |
```

Cập nhật dòng tương ứng trong `history.md` với Jira Epic key và đổi trạng thái thành `Đã xác nhận`.

## Bước 5 — Báo Cáo & Đề Xuất Tự Động

Hiển thị bảng tóm tắt ticket, rồi hỏi:

> Bạn có muốn tôi setup campaign trên CleverTap tự động qua API script không? Tôi có thể tạo segment và campaign dựa trên kế hoạch này.

Nếu có → dùng `/campaign-setup`
Nếu không → nhắc người dùng kế hoạch ở `plans/<thư-mục>/plan.md` và ticket đã được tạo
