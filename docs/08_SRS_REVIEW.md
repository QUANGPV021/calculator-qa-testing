# 🔍 PHIẾU REVIEW TÀI LIỆU ĐẶC TẢ SRS
## HỌC PHẦN: ĐÁNH GIÁ HIỆU NĂNG CSE3066
**Vai trò:** Phần B - Tester (Tiêu chí B1: 0,5 điểm)  
**Người thực hiện Review (Tester):** Phạm Văn Quang - MSSV: 23110342  
**Hệ thống được Review:** SmartCalc Pro (v1.0)

---

## 1. THÔNG TIN ĐỢT REVIEW
- **Mục tiêu:** Đánh giá tính đầy đủ, tính nhất quán, tính khả thi và khả năng kiểm thử được (Testability) của các yêu cầu đặc tả chức năng (FR) và phi chức năng (NFR).
- **Phương pháp thực hiện:** Đối chiếu trực tiếp giữa tài liệu SRS và khả năng thiết kế kịch bản kiểm thử (Test Case Design).

---

## 2. BẢNG GHI NHẬN KẾT QUẢ REVIEW & ĐỀ XUẤT CẢI TIẾN

| Mục Review | Hiện trạng trong tài liệu | Đánh giá của Tester | Vấn đề phát hiện | Đề xuất cải tiến (Action Item) |
| :--- | :--- | :---: | :--- | :--- |
| **FR-04 (Dấu chấm)** | Chỉ ghi chung chung: *"Cho phép nhập số thập phân."* | **Chưa rõ ràng (Ambiguous)** | Không nêu rõ cách xử lý khi người dùng nhấn 2 hoặc nhiều dấu chấm liên tiếp (`5.2.3`). | Bổ sung quy định: Chặn triệt để dấu chấm thứ hai trong cùng một toán hạng. |
| **FR-07 (Độ chính xác)** | Ghi: *"Thực hiện tính toán các phép toán số học."* | **Khó kiểm thử (Not Testable)** | Chưa quy định thuật toán làm tròn số thực, dễ sinh sai số dấu phẩy động IEEE-754 (`0.1 + 0.2 = 0.30000000000000004`). | Quy định rõ: Kết quả phải được làm tròn `toFixed(12)` để bảo đảm độ chính xác. |
| **FR-09 (Chia cho 0)** | Ghi: *"Xử lý ngoại lệ khi chia cho số 0."* | **Thiếu đặc tả giao diện** | Chưa quy định rõ thông báo lỗi xuất hiện ở đâu, có khóa tính tiếp hay không. | Quy định: Hiển thị chuỗi `'Cannot divide by 0'` và khóa tính tiếp cho đến khi bấm `AC`. |
| **NFR Hiệu năng** | Ghi: *"Hệ thống chạy nhanh, phản hồi tốt."* | **Không có con số định lượng** | Tester không có căn cứ số liệu đo lường cụ thể để đánh giá Pass/Fail. | Bổ sung chỉ số định lượng: Thời gian phản hồi phải dưới 50ms cho mọi thao tác bấm phím. |

---

## 3. KẾT LUẬN CỦA TESTER
- Tài liệu SRS đã được Chủ hệ thống tiếp thu và bổ sung đầy đủ các chỉ số định lượng cụ thể.
- Tester thông qua tài liệu đặc tả sau khi các đề xuất trên đã được cập nhật hoàn chỉnh.

