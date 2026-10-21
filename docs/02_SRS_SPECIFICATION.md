# 📄 BẢNG ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS)
## DỰ ÁN: MÁY TÍNH BỎ TÚI SMARTCALC PRO (v1.0)

Tài liệu này quy định các yêu cầu chức năng (Functional Requirements - FR) và phi chức năng (Non-Functional Requirements - NFR) làm căn cứ đối chiếu để đội ngũ Kiểm thử (QA/QC) thiết kế Test Case và xác định lỗi (Defects/Bugs).

---

## 1. YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### 1.1. Nhập liệu và Hiển thị (Input & Display)
- **FR-01 (Mặc định ban đầu):** Khi vừa tải ứng dụng hoặc sau khi bấm `AC`, màn hình chính phải hiển thị số `0`.
- **FR-02 (Nhập chữ số):** Người dùng có thể nhấn các phím số từ `0` đến `9`.
- **FR-03 (Chặn số 0 vô nghĩa ở đầu):** Không được cho phép tồn tại nhiều số `0` ở đầu số nguyên (ví dụ: bấm `0` nhiều lần rồi bấm `8` thì màn hình chỉ hiển thị số `8`, tuyệt đối không hiển thị `0008` hoặc `008`).
- **FR-04 (Dấu thập phân):** Trong cùng một số, chỉ cho phép xuất hiện **tối đa một** dấu chấm thập phân (`.`). Nếu số đã có dấu `.`, các lần bấm `.` tiếp theo phải bị vô hiệu hóa.
- **FR-05 (Giới hạn hiển thị):** Màn hình hiển thị số tối đa 14-16 ký tự. Khi kết quả hoặc số nhập vượt quá giới hạn này, ứng dụng phải tự động co chữ hoặc chuyển sang định dạng khoa học e-notation (ví dụ: `1.234e+18`), không được để tràn ra ngoài viền khung.
- **FR-06 (Phím Backspace - ⌫):** 
  - Xóa ký tự cuối cùng của số đang nhập.
  - Khi xóa đến chữ số duy nhất cuối cùng, màn hình phải quay về giá trị mặc định là `0`, không được để màn hình trống rỗng (`""`).

### 1.2. Phép tính số học cơ bản (Basic Operations)
- **FR-07 (Độ chính xác phép tính):** Các phép tính số học (+, -, ×, ÷) phải cho kết quả chính xác theo chuẩn số học. Các phép tính với số thực phải được làm tròn hợp lý (tối đa 10-12 chữ số thập phân, ví dụ `0.1 + 0.2` phải hiển thị chính xác là `0.3`, không được hiển thị sai số nhị phân `0.30000000000000004`).
- **FR-08 (Thứ tự ưu tiên toán học - BODMAS):** 
  - Phép nhân (×) và phép chia (÷) có độ ưu tiên cao hơn phép cộng (+) và trừ (-).
  - Biểu thức `2 + 3 × 4` phải cho kết quả đúng là `14`.
- **FR-09 (Chia cho 0 - Division by Zero):**
  - Khi mẫu số bằng `0` trong phép chia, ứng dụng phải hiển thị thông báo lỗi thân thiện (ví dụ: `Cannot divide by zero` hoặc `Lỗi chia cho 0`).
  - Hệ thống không được hiển thị `Infinity` và phải khóa thao tác tính tiếp cho đến khi người dùng nhấn `C` hoặc `AC`.
- **FR-10 (Thay thế toán tử liên tiếp):** Nếu người dùng nhấn một toán tử (ví dụ `+`) sau đó đổi ý nhấn ngay toán tử khác (ví dụ `×`) trước khi nhập số tiếp theo, toán tử sau phải tự động thay thế toán tử trước (không bị lỗi ghép chuỗi biểu thức).

### 1.3. Các hàm tính năng mở rộng (Advanced Functions)
- **FR-11 (Căn bậc hai - √):** 
  - Tính căn bậc hai của số dương: `√9 = 3`.
  - Nếu người dùng bấm `√` trên một số âm (ví dụ: `-9`), ứng dụng phải hiển thị thông báo lỗi `Invalid Input`, không được hiển thị `NaN`.
- **FR-12 (Bình phương - x²):** Tính bình phương của số hiện tại: `5² = 25`.
- **FR-13 (Đổi dấu - ±):** 
  - Đảo dấu dương thành âm và ngược lại.
  - Ngoại lệ: Nếu màn hình đang là số `0`, bấm `±` thì giá trị vẫn phải giữ nguyên là `0`, tuyệt đối không hiển thị `-0`.
- **FR-14 (Phép tính phần trăm - %):**
  - Khi thực hiện trong ngữ cảnh cộng/trừ: `100 + 10%` phải tính là `100 + (100 × 10%) = 110`.

### 1.4. Quản lý Bộ nhớ tạm (Memory Operations)
- **FR-15 (Chức năng các phím nhớ):**
  - `MS` (Memory Store): Lưu giá trị hiện tại trên màn hình vào bộ nhớ.
  - `MR` (Memory Recall): Gọi giá trị đang lưu trong bộ nhớ ra màn hình.
  - `M+` (Memory Add): Cộng thêm giá trị màn hình vào bộ nhớ hiện tại.
  - `M-` (Memory Subtract): Lấy bộ nhớ hiện tại trừ đi giá trị màn hình.
  - `MC` (Memory Clear): Xóa trắng bộ nhớ về 0 và tắt biểu tượng `M`.
- **FR-16 (Độc lập bộ nhớ):** Phím `C` (Clear Entry) chỉ xóa giá trị hiển thị đang nhập dở, **tuyệt đối không được xóa bộ nhớ Memory**.

### 1.5. Lịch sử tính toán (History Log)
- **FR-17 (Ghi nhận lịch sử):** Mỗi khi nhấn `=`, biểu thức và kết quả tương ứng phải được lưu vào danh sách nhật ký bên phải.
- **FR-18 (Tái sử dụng kết quả):** Khi nhấp chuột vào một mục trong lịch sử, kết quả đó phải được nạp lại vào màn hình máy tính.
- **FR-19 (Xóa lịch sử):** Nhấn "Xóa lịch sử" phải làm sạch toàn bộ dữ liệu cả trên giao diện và trong bộ nhớ RAM (không được rò rỉ dữ liệu).

---

## 2. YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS)
- **NFR-01 (Hiệu năng):** Phản hồi tức thì (< 50ms) sau mỗi lần click phím.
- **NFR-02 (Tương thích):** Hoạt động mượt mà trên tất cả các trình duyệt hiện đại (Chrome, Edge, Firefox, Safari).
- **NFR-03 (Bàn phím vật lý):** Hỗ trợ đầy đủ các phím số `0-9`, dấu `.`, các phím `+`, `-`, `*`, `/`, `Enter` (`=`), `Backspace` (`⌫`), `Escape` (`AC`).
- **NFR-04 (Giao diện):** Giao diện hiện đại, trực quan, độ tương phản màu chuẩn WCAG 2.1 AA.
