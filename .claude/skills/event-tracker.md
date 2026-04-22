# Skill: event-tracker

Khi người dùng gọi `/event-tracker` hoặc yêu cầu định nghĩa/thiết kế event tracking:

## Bước 1 — Hiểu Tính Năng

Hỏi:
- Tính năng hoặc luồng người dùng nào cần tracking?
- Nền tảng: Android / iOS / cả hai?
- Cần event phía server hay client?
- Dữ liệu này hỗ trợ quyết định gì? (phân đoạn, campaign trigger, funnel analysis)

## Bước 2 — Thiết Kế Schema Event

Với mỗi event trong luồng, định nghĩa:
```yaml
event:
  name: "Tên Event"  # Title Case, theo quy ước super-app-events.md
  trigger: "Khi người dùng thực hiện X"
  platform: android, ios
  type: client-side | server-side
  properties:
    - name: tên_thuộc_tính
      type: string | number | boolean
      required: true | false
      example: "giá_trị_ví_dụ"
      notes: "Ghi chú bổ sung"
```

Tham khảo `knowledge/super-app-events.md` — tái sử dụng event hiện có nếu có thể, chỉ tạo mới khi thực sự cần.

## Bước 3 — Tạo Ticket Triển Khai

Tạo task sẵn sàng cho Jira:

**Tiêu đề**: `[Tracking] Instrument event cho {tính năng}`

**Mô tả**:
```
Triển khai các CleverTap event sau cho {tính năng}:

Android (Kotlin):
// Event 1
val props = HashMap<String, Any>()
props["tên_thuộc_tính"] = giá_trị
CleverTap.getDefaultInstance(context)?.event?.push("Tên Event", props)

iOS (Swift):
// Event 1
CleverTap.sharedInstance()?.recordEvent("Tên Event", withProps: [
    "tên_thuộc_tính": giá_trị
])

QA: Xác minh trong CleverTap Dashboard → Events → Live View
```

## Bước 4 — Tạo Checklist QA

Tạo task QA (phân công cho thành viên có sẵn):
```
Checklist QA cho tracking {tính năng}:
[ ] Xác minh event kích hoạt trên Android (thiết bị: Pixel/Samsung)
[ ] Xác minh event kích hoạt trên iOS (thiết bị: iPhone 14+)
[ ] Tất cả thuộc tính bắt buộc có mặt với đúng kiểu dữ liệu
[ ] Không có PII trong thuộc tính event (trừ Identity)
[ ] Event hiển thị trong Live View trong vòng 2 phút
[ ] Funnel analysis trong CleverTap hoạt động đúng
```

## Bước 5 — Cập Nhật Tài Liệu Event

Nhắc người dùng: "Sau khi xác minh, hãy thêm event mới vào `knowledge/super-app-events.md` để cập nhật tài liệu tham khảo."
