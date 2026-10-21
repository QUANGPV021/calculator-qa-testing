# 📋 KẾ HOẠCH KIỂM THỬ (TEST PLAN)
## DỰ ÁN: SMARTCALC PRO (MÔN HỌC KIỂM THỬ PHẦN MỀM)

---

## 1. GIỚI THIỆU (INTRODUCTION)
### 1.1. Mục đích
Tài liệu Kế hoạch kiểm thử này xác định phạm vi, chiến lược, môi trường, tiêu chí dừng và các tài liệu bàn giao cho việc kiểm thử ứng dụng máy tính bỏ túi **SmartCalc Pro v1.0**.

### 1.2. Mục tiêu chất lượng
- Đảm bảo các phép toán cơ bản và nâng cao hoạt động đúng chuẩn số học.
- Đảm bảo xử lý lỗi đầu vào (Input validation) và các trường hợp ngoại lệ (Edge cases).
- Đảm bảo trải nghiệm người dùng (UX) và tính toàn vẹn dữ liệu bộ nhớ/lịch sử.

---

## 2. PHẠM VI KIỂM THỬ (TEST SCOPE)

### 2.1. Trong phạm vi (In-Scope)
- **Kiểm thử chức năng (Functional Testing):**
  - Các phép tính: Cộng (+), Trừ (-), Nhân (×), Chia (÷), Căn bậc hai (√), Bình phương (x²), Phần trăm (%), Đổi dấu (±).
  - Thứ tự ưu tiên toán học (Operator Precedence / BODMAS).
  - Các nút xóa: Xóa tất cả (AC), Xóa giá trị hiện tại (C), Xóa ký tự lùi (⌫).
  - Các thao tác bộ nhớ tạm: MC, MR, M+, M-, MS.
  - Quản lý nhật ký tính toán (History Log).
- **Kiểm thử giao diện & Trải nghiệm (UI/UX Testing):**
  - Màn hình hiển thị, tràn số (Overflow), hiển thị biểu tượng bộ nhớ (M).
  - Hỗ trợ phím tắt bàn phím cứng (Physical Keyboard).
- **Kiểm thử các trường hợp biên & Ngoại lệ (Boundary & Negative Testing):**
  - Chia cho 0 (Division by Zero).
  - Căn bậc hai số âm (Square root of negative numbers).
  - Nhập nhiều số 0 ở đầu (Leading zeros), nhiều dấu chấm thập phân liên tiếp.
  - Nhấn phím `=` liên tiếp nhiều lần.

### 2.2. Ngoài phạm vi (Out-of-Scope)
- Kiểm thử tải / chịu tải lớn hàng triệu user (Load/Stress Testing).
- Kiểm thử bảo mật cơ sở dữ liệu (ứng dụng thuần client-side không có backend/database).

---

## 3. CHIẾN LƯỢC KIỂM THỬ (TEST STRATEGY & TECHNIQUES)

Đội ngũ tester sẽ áp dụng phối hợp 4 kỹ thuật thiết kế test case chuẩn quốc tế:
1. **Phân vùng tương đương (Equivalence Partitioning - EP):**
   - Phân chia tập dữ liệu đầu vào thành các lớp hợp lệ (Valid partitions) và không hợp lệ (Invalid partitions).
2. **Phân tích giá trị biên (Boundary Value Analysis - BVA):**
   - Kiểm tra các giá trị tại ngưỡng ranh giới: Số 0, số âm nhỏ nhất, số thực thập phân 0.000001, giới hạn ký tự màn hình (14, 15, 16, 25 ký tự).
3. **Kiểm thử chuyển trạng thái (State Transition Testing):**
   - Kiểm tra chuỗi thao tác liên tục giữa các trạng thái nhớ: `MS` -> `C` -> `MR` hoặc thực hiện tính toán nối tiếp `5 + 2 = 7 = 9 = 11`.
4. **Kỹ thuật đoán lỗi (Error Guessing):**
   - Dựa trên kinh nghiệm của tester để dự đoán các lỗi lập trình viên hay mắc phải: quên làm tròn float IEEE 754 (`0.1 + 0.2`), rò rỉ dữ liệu khi bấm xóa lịch sử, nhập toán tử liên tiếp `5 + * 2`.

---

## 4. MÔI TRƯỜNG KIỂM THỬ (TEST ENVIRONMENT)
- **Trình duyệt:** Google Chrome (v120+), Mozilla Firefox, Microsoft Edge, Safari.
- **Hệ điều hành:** macOS, Windows 10/11, Linux, Thiết bị di động (Responsive mode).
- **Độ phân giải màn hình:** Desktop (1920x1080, 1366x768), Tablet (768x1024), Mobile (375x812).

---

## 5. TIÊU CHÍ ĐÁNH GIÁ MỨC ĐỘ LỖI (BUG SEVERITY LEVELS)

| Mức độ | Định nghĩa | Ví dụ trong dự án |
| :--- | :--- | :--- |
| **Critical** | Lỗi nghiêm trọng làm sai lệch hoàn toàn kết quả tính toán cơ bản hoặc gây crash hệ thống. | Phép chia cho 0 ra `Infinity`; `0.1 + 0.2` tính sai float. |
| **Major** | Lỗi ảnh hưởng lớn đến tính năng chính hoặc tính sai logic toán học. | Thứ tự ưu tiên `2+3*4` tính ra 20; nút `M-` lại cộng thêm tiền/số; rò rỉ dữ liệu lịch sử. |
| **Medium** | Lỗi ảnh hưởng đến trải nghiệm hoặc tính năng phụ. | Tràn màn hình khi nhập số quá dài; nút Backspace để lại chuỗi rỗng rác. |
| **Minor** | Lỗi hiển thị nhỏ, không ảnh hưởng đến kết quả cuối cùng. | Đổi dấu số 0 biến thành `-0`; cho phép nhập nhiều số 0 đầu (`0008`). |

---

## 6. SẢN PHẨM BÀN GIAO (DELIVERABLES)
1. **Bảng Kịch bản kiểm thử (Test Cases Document)** đã điền trạng thái Pass/Fail.
2. **Danh sách các Báo cáo lỗi (Bug Reports)** chi tiết từng lỗi phát hiện được.
3. **Báo cáo tổng kết kiểm thử (Test Summary Report)** thống kê số lượng bug theo mức độ nghiêm trọng và tỷ lệ đạt yêu cầu.
