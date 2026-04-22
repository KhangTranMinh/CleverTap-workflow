# Skill: create-plan

Khi người dùng gọi `/create-plan` hoặc yêu cầu tạo/lập kế hoạch, thực hiện các bước sau:

## Bước 1 — Thu Thập Yêu Cầu

Nếu người dùng chưa cung cấp đủ thông tin, hỏi tất cả cùng một lúc (không hỏi từng câu):
- **Mục tiêu**: Mục tiêu kinh doanh là gì? (ví dụ: kéo lại user rời bỏ, tăng đơn đồ ăn, tăng tần suất đặt xe)
- **Đối tượng**: Ai là mục tiêu? (ví dụ: user không hoạt động 30 ngày, user mới, user chỉ dùng đồ ăn)
- **Kênh**: Push, in-app, email, SMS, hay đa kênh?
- **Thời gian**: Khi nào launch? Có deadline không?
- **Chỉ số thành công**: Đo lường thành công bằng gì? (conversion event, CTR, doanh thu)

Nếu yêu cầu đã trả lời rõ các câu trên, bỏ qua và đi thẳng vào Bước 2.

## Bước 2 — Lưu Yêu Cầu

Tạo thư mục tại `plans/YYYY-MM-DD-HHMM-{slug}/` với ngày hôm nay, giờ hiện tại (24h HHMM), và slug ngắn (chữ thường, dấu gạch ngang).

Bên trong thư mục tạo `request.md` ghi lại nguyên văn yêu cầu và các làm rõ:

```markdown
# Yêu Cầu

**Ngày**: YYYY-MM-DD HH:MM
**Người yêu cầu**: (người dùng)

## Yêu Cầu Ban Đầu
<dán nguyên văn lời của người dùng vào đây>

## Làm Rõ
<các câu hỏi và trả lời tiếp theo, hoặc "Không có" nếu yêu cầu đã rõ>
```

## Bước 3 — Lập Kế Hoạch

Trong cùng thư mục, tạo `plan.md` dùng `templates/campaign-plan-template.md` điền đầy đủ.

Kế hoạch phải bao gồm:
1. **Tổng quan** — Tóm tắt một đoạn
2. **Mục tiêu & KPI** — Mục tiêu kinh doanh + chỉ tiêu đo lường
3. **Audience Segment** — Logic filter CleverTap (theo event hoặc property)
4. **Chi tiết Campaign** — Kênh, nội dung message, lịch gửi, frequency cap
5. **Tracking Events** — Event mới cần instrument (nếu có)
6. **Công việc** — Phân chia cho từng thành viên (Minh/Linh/Đức) kèm ước tính story point
7. **Timeline** — Các mốc ngày
8. **Rủi ro & Ghi chú** — Edge case, dependencies

## Bước 4 — Cập Nhật history.md

Thêm một dòng vào `history.md` ở thư mục gốc (tạo file nếu chưa có):

```
| YYYY-MM-DD HH:MM | [Tên Campaign](plans/YYYY-MM-DD-HHMM-{slug}/plan.md) | — | Đang lập kế hoạch |
```

Cột: `Ngày | Sáng kiến | Jira Epic | Trạng thái`
Tiến trình: `Đang lập kế hoạch` → `Đã xác nhận` → `Đang thực hiện` → `Đã launch` → `Đã báo cáo`

## Bước 5 — Xác Nhận Với Người Dùng

Sau khi ghi file, thông báo:

> Kế hoạch đã lưu tại `plans/YYYY-MM-DD-HHMM-{slug}/plan.md`. Vui lòng xem và chỉnh sửa file, sau đó xác nhận để tôi tạo Jira ticket.

KHÔNG tự động tạo Jira ticket. Chờ người dùng xác nhận rõ ràng.

## Hướng Dẫn

- Tham khảo `knowledge/campaign-types.md` để gợi ý kênh phù hợp
- Tham khảo `knowledge/super-app-events.md` để dùng đúng tên event
- Tham khảo `knowledge/team-config.md` để phân công công việc
- Story point: 1 = 1–2 giờ, 2 = nửa ngày, 3 = cả ngày, 5 = 2–3 ngày
- Phân bổ đều công việc cho Minh, Linh và Đức — cả 3 đều là CRM specialist
- Luôn có task QA/kiểm thử trước khi launch
