# 🐞 BIỂU MẪU BÁO CÁO LỖI (BUG REPORT TEMPLATE)

Tài liệu này cung cấp biểu mẫu chuẩn quốc tế (IEEE 829 / Jira / GitHub Issues) để tester báo cáo các lỗi phát hiện được trong quá trình kiểm thử phần mềm.

---

## 1. MẪU BÁO CÁO TRỐNG (BLANK TEMPLATE)
*Tester sao chép khung dưới đây để tạo từng báo cáo lỗi:*

```markdown
### [BUG-ID]: [Module] Tiêu đề lỗi ngắn gọn, súc tích

- **Mức độ nghiêm trọng (Severity):** [Critical / Major / Medium / Minor]
- **Độ ưu tiên xử lý (Priority):** [High / Medium / Low]
- **Người báo cáo (Reporter):** [Họ và tên sinh viên / Tester]
- **Ngày báo cáo (Date):** [DD/MM/YYYY]
- **Môi trường thử nghiệm (Environment):** [Ví dụ: Google Chrome v122, macOS Sonoma / Windows 11]

#### 1. Điều kiện tiên quyết (Pre-conditions):
- [Mô tả trạng thái ban đầu của ứng dụng, ví dụ: Ứng dụng ở trạng thái ban đầu, màn hình hiển thị 0]

#### 2. Các bước tái hiện (Steps to Reproduce):
1. Bước 1...
2. Bước 2...
3. Bước 3...

#### 3. Kết quả thực tế (Actual Result):
- [Mô tả chính xác những gì ứng dụng đang làm sai]

#### 4. Kết quả kỳ vọng (Expected Result):
- [Mô tả những gì hệ thống PHẢI làm đúng theo tài liệu SRS]

#### 5. Bằng chứng đính kèm (Evidence/Screenshots):
- [Dán ảnh chụp màn hình lỗi hoặc chuỗi log console]

#### 6. Đánh giá tác động (Impact Analysis):
- [Lỗi này ảnh hưởng như thế nào đến người dùng hoặc độ tin cậy của ứng dụng?]
```

---

## 2. VÍ DỤ MẪU BÁO CÁO THỰC TẾ (SAMPLE FILLED REPORT)

### [BUG-001]: [Logic] Sai số phép tính cộng số thực (0.1 + 0.2 ra 0.30000000000000004)

- **Mức độ nghiêm trọng (Severity):** Critical
- **Độ ưu tiên xử lý (Priority):** High
- **Người báo cáo (Reporter):** Phạm Văn Quang (23110342)
- **Ngày báo cáo (Date):** 21/10/2026
- **Môi trường thử nghiệm (Environment):** Google Chrome Version 128.0 (macOS)

#### 1. Điều kiện tiên quyết:
- Ứng dụng ở trạng thái mở mới, màn hình hiển thị `0`.

#### 2. Các bước tái hiện:
1. Nhập số `0.1` trên bàn phím hoặc nhấn nút trên màn hình.
2. Nhấn nút toán tử `+`.
3. Nhập số `0.2`.
4. Nhấn nút `=`.

#### 3. Kết quả thực tế:
- Màn hình kết quả hiển thị chuỗi: `0.30000000000000004`.

#### 4. Kết quả kỳ vọng:
- Theo mục **FR-07 (SRS)**: Kết quả tính toán số học phải được làm tròn chính xác, màn hình phải hiển thị đúng là `0.3`.

#### 5. Bằng chứng đính kèm:
- Ảnh chụp màn hình: `assets/evidence_bug01.png` hiển thị kết quả tràn số thập phân.

#### 6. Đánh giá tác động:
- Gây mất uy tín nghiêm trọng cho ứng dụng máy tính tài chính/học tập. Sai số này sẽ tích lũy lớn dần trong các phép tính chuỗi tiếp theo.
