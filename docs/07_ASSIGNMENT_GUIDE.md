# 🎓 HƯỚNG DẪN LÀM BÀI TẬP DỰ ÁN & BAREM CHẤM ĐIỂM
## MÔN HỌC: KIỂM THỬ PHẦN MỀM (SOFTWARE TESTING & QA)

Tài liệu này hướng dẫn sinh viên / nhóm thực hiện bài tập lớn và barem điểm chi tiết dành cho Giảng viên.

---

## 1. YÊU CẦU ĐỐI VỚI SINH VIÊN / NHÓM HỌC TẬP
Mỗi sinh viên hoặc nhóm (2-3 bạn) đóng vai trò là một **Đội ngũ QA/QC độc lập**. Nhiệm vụ:
1. Đọc và phân tích tài liệu đặc tả [02_SRS_SPECIFICATION.md](file:///Users/phamquang/Projects/calculator-qa-testing/docs/02_SRS_SPECIFICATION.md).
2. Xây dựng Kế hoạch kiểm thử (Test Plan) và thiết kế bộ kịch bản kiểm thử (Test Cases).
3. Thực hiện kiểm thử trên ứng dụng SmartCalc Pro để phát hiện các lỗi sai lệch so với đặc tả.
4. Viết Báo cáo lỗi (Bug Report) theo mẫu chuẩn [05_BUG_REPORT_TEMPLATE.md](file:///Users/phamquang/Projects/calculator-qa-testing/docs/05_BUG_REPORT_TEMPLATE.md).
5. Viết Báo cáo tổng kết kiểm thử (Test Summary Report).

---

## 2. BAREM CHẤM ĐIỂM CHI TIẾT (THANG ĐIỂM 10)

| STT | Nội dung đánh giá | Tiêu chí chi tiết | Điểm tối đa |
| :---: | :--- | :--- | :---: |
| **1** | **Thiết kế Test Cases (Kịch bản kiểm thử)** | - Áp dụng đúng các kỹ thuật: Phân vùng tương đương (EP), Giá trị biên (BVA), Đoán lỗi.<br>- Có đầy đủ các trường hợp Positive, Negative, Boundary, UI.<br>- Định dạng chuẩn, rõ ràng, dễ hiểu. | **3.0 điểm** |
| **2** | **Số lượng & Chất lượng lỗi tìm được** | - Tìm được ≥ 12/15 lỗi: **3.0 điểm**<br>- Tìm được 9 - 11 lỗi: **2.0 điểm**<br>- Tìm được 6 - 8 lỗi: **1.5 điểm**<br>- Tìm được < 6 lỗi: **1.0 điểm** | **3.0 điểm** |
| **3** | **Kỹ năng viết Bug Report** | - Mô tả các bước tái hiện (Steps to Reproduce) rõ ràng, 100% tái hiện được.<br>- Phân loại đúng Severity (Critical, Major, Medium, Minor).<br>- Có bằng chứng (Screenshot, kết quả thực tế vs kỳ vọng). | **2.0 điểm** |
| **4** | **Báo cáo tổng kết & Đánh giá chất lượng** | - Thống kê được tỷ lệ Pass/Fail.<br>- Biểu đồ phân bổ lỗi theo Severity và Module.<br>- Đưa ra nhận xét, đánh giá rủi ro trước khi phát hành. | **1.0 điểm** |
| **5** | **Đề xuất giải pháp sửa lỗi (Bonus / Điểm cộng)** | - Đọc code [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js) và chỉ ra đúng dòng code gây lỗi.<br>- Đề xuất đoạn code sửa chữa (Patch) thành công. | **1.0 điểm** |
| **TỔNG CỘNG** | | | **10.0 điểm** |

---

## 3. HƯỚNG DẪN NỘP BÀI
Sinh viên nén thư mục bài làm gồm:
- File Word/PDF báo cáo tổng hợp dự án.
- File Excel/Markdown chứa bảng Test Cases và danh sách Bug Reports.
- Đường link GitHub repository cá nhân (nếu có push lên repo riêng).
