# 🕵️‍♂️ BẢNG ĐÁP ÁN BÍ MẬT: DANH MỤC 15 LỖI CÀI CẮM (BUG CATALOG)
> ⚠️ **LƯU Ý BẢO MẬT:** Tài liệu này là **ĐÁP ÁN CHẤM ĐIỂM** dành riêng cho Giảng viên / Trưởng nhóm QA. Không công khai tài liệu này cho sinh viên/tester trước khi họ hoàn thành bài test!

---

## TỔNG HỢP THỐNG KÊ LỖI THEO SEVERITY
- **Critical (2 lỗi):** BUG-01, BUG-03
- **Major (6 lỗi):** BUG-02, BUG-04, BUG-05, BUG-09, BUG-10, BUG-12, BUG-15
- **Medium (4 lỗi):** BUG-07, BUG-08, BUG-11, BUG-14
- **Minor (2 lỗi):** BUG-06, BUG-13

---

## CHI TIẾT 15 LỖI & NGUYÊN NHÂN MÃ NGUỒN (ROOT CAUSE)

### 🔴 BUG-01: Lỗi độ chính xác số thực (Floating-Point Precision)
- **Mức độ:** `Critical` | **Module:** Core Arithmetic Calculation
- **Các bước tái hiện:** Bấm `0.1` -> `+` -> `0.2` -> `=`
- **Kết quả thực tế:** `0.30000000000000004` (kỳ vọng: `0.3`)
- **Vị trí code:** Trong hàm `performRawCalculation()` tại file [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  case '+':
    return firstVal + secondVal; // LỖI: Sử dụng trực tiếp phép cộng float của JS
  ```
- **Cách fix chuẩn:**
  ```javascript
  case '+':
    return parseFloat((firstVal + secondVal).toFixed(12));
  ```

---

### 🟠 BUG-02: Cho phép nhập nhiều dấu chấm thập phân trong cùng 1 số
- **Mức độ:** `Major` | **Module:** Input Validation
- **Các bước tái hiện:** Bấm `5` -> `.` -> `2` -> `.` -> `3`
- **Kết quả thực tế:** Màn hình cho phép `5.2.3`
- **Vị trí code:** Trong hàm `inputDecimal()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  if (state.currentInput.endsWith('.')) return; // LỖI: Chỉ kiểm tra ký tự liền trước
  ```
- **Cách fix chuẩn:**
  ```javascript
  if (state.currentInput.includes('.')) return; // Chặn nếu số hiện tại đã có dấu chấm
  ```

---

### 🔴 BUG-03: Phép chia cho 0 trả về 'Infinity'
- **Mức độ:** `Critical` | **Module:** Core Arithmetic / Error Handling
- **Các bước tái hiện:** Bấm `9` -> `÷` -> `0` -> `=`
- **Kết quả thực tế:** Màn hình hiển thị `Infinity`
- **Vị trí code:** Trong hàm `performRawCalculation()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  if (secondVal === 0) return Infinity; // LỖI: Trả về Infinity thay vì ném lỗi
  ```
- **Cách fix chuẩn:**
  ```javascript
  if (secondVal === 0) return "Cannot divide by 0";
  ```

---

### 🟠 BUG-04: Vi phạm thứ tự ưu tiên toán học (Operator Precedence)
- **Mức độ:** `Major` | **Module:** Expression Parsing
- **Các bước tái hiện:** Bấm `2` -> `+` -> `3` -> `×` -> `4` -> `=`
- **Kết quả thực tế:** Tính ra `20` (tính tuần tự (2+3)*4) thay vì `14` (BODMAS)
- **Vị trí code:** Trong hàm `handleOperator()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  // LỖI: Tính gộp ngay khi gặp toán tử tiếp theo không xét độ ưu tiên * và /
  const result = performRawCalculation(state.operation, parseFloat(state.previousInput), inputValue);
  ```
- **Cách fix chuẩn:** Sử dụng thuật toán Shunting-yard hoặc cây biểu thức Abstract Syntax Tree để parse toán tử theo đúng trọng số ưu tiên.

---

### 🟠 BUG-05: Căn bậc hai số âm xuất 'NaN'
- **Mức độ:** `Major` | **Module:** Advanced Functions
- **Các bước tái hiện:** Bấm `9` -> `±` (thành -9) -> `√`
- **Kết quả thực tế:** Màn hình xuất hiện chuỗi `NaN`
- **Vị trí code:** Trong hàm `calcSquareRoot()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  const result = Math.sqrt(val); // LỖI: Không kiểm tra val < 0
  ```
- **Cách fix chuẩn:**
  ```javascript
  if (val < 0) { state.currentInput = "Invalid Input"; return; }
  ```

---

### 🔵 BUG-06: Cho phép nhập nhiều số 0 vô nghĩa ở đầu (Leading Zeros)
- **Mức độ:** `Minor` | **Module:** Input Formatter
- **Các bước tái hiện:** Bấm `0` ba lần rồi bấm `8`
- **Kết quả thực tế:** Màn hình thành `0008`
- **Vị trí code:** Trong hàm `inputDigit()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  if (state.currentInput === '0' && digit === '0') state.currentInput = '00';
  ```
- **Cách fix chuẩn:** Chuẩn hóa: nếu đang là `'0'` và bấm số khác thì thay thế hoàn toàn: `state.currentInput = digit`.

---

### 🟡 BUG-07: Tràn giao diện màn hình khi nhập quá 16 số
- **Mức độ:** `Medium` | **Module:** UI/UX & Layout Boundary
- **Các bước tái hiện:** Nhập liên tục 25 phím `9`
- **Kết quả thực tế:** Chữ số dài quá tràn ra khỏi khung viền máy tính
- **Vị trí code:** `inputDigit()` thiếu giới hạn `if (state.currentInput.length >= 15) return;` và CSS màn hình để `overflow: visible`.
- **Cách fix chuẩn:** Giới hạn 15 ký tự hoặc co fontsize động, chuyển định dạng `toExponential()`.

---

### 🟡 BUG-08: Nút Backspace (⌫) xóa hết số để lại chuỗi rỗng
- **Mức độ:** `Medium` | **Module:** Input Editing
- **Các bước tái hiện:** Khi màn hình có số `5`, bấm `⌫` rồi bấm `+`
- **Kết quả thực tế:** Màn hình trống trơn `""`, bấm `+` bị lỗi cú pháp `NaN`
- **Vị trí code:** Trong hàm `backspace()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  if (state.currentInput.length <= 1) { state.currentInput = ''; }
  ```
- **Cách fix chuẩn:** Phải gán lại về chuỗi mặc định `'0'`.

---

### 🟠 BUG-09: Nhấn liên tiếp các toán tử gây nối chuỗi lỗi
- **Mức độ:** `Major` | **Module:** Operator State Handling
- **Các bước tái hiện:** Bấm `5` -> `+` -> `×` -> `2` -> `=`
- **Kết quả thực tế:** Biểu thức bị nối chuỗi thành `5 + ×`
- **Vị trí code:** Trong hàm `handleOperator()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  state.operation = state.operation + ' ' + nextOp; // LỖI: Nối chuỗi thay vì ghi đè toán tử mới
  ```
- **Cách fix chuẩn:** `state.operation = nextOp;`

---

### 🟠 BUG-10: Lỗi tính phần trăm (%) trong phép cộng/trừ
- **Mức độ:** `Major` | **Module:** Arithmetic Logic
- **Các bước tái hiện:** `100` -> `+` -> `10` -> `%` -> `=`
- **Kết quả thực tế:** `100.1` (kỳ vọng thực tế của máy tính là `110`)
- **Vị trí code:** Hàm `calcPercent()` chỉ chia đơn thuần `val / 100` mà không nhân với cơ số ban đầu.

---

### 🟡 BUG-11: Nút 'C' (Clear Entry) xóa luôn bộ nhớ tạm Memory
- **Mức độ:** `Medium` | **Module:** Memory State Management
- **Các bước tái hiện:** Lưu số `50` vào `MS`, nhập `99`, bấm `C`, bấm `MR`
- **Kết quả thực tế:** `MR` trả về `0` (mất luôn dữ liệu bộ nhớ)
- **Vị trí code:** Trong hàm `clearEntry()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  state.memoryValue = 0; // LỖI: Xóa nhầm biến bộ nhớ
  ```
- **Cách fix chuẩn:** Xóa dòng này đi, chỉ reset `state.currentInput = '0'`.

---

### 🟠 BUG-12: Nút 'M-' (Memory Subtract) tính ngược thành cộng
- **Mức độ:** `Major` | **Module:** Memory Operations
- **Các bước tái hiện:** Lưu `100` vào `MS`, nhập `30`, bấm `M-`, bấm `MR`
- **Kết quả thực tế:** Ra `130` (kỳ vọng: `70`)
- **Vị trí code:** Trong hàm `memorySubtract()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  state.memoryValue += parseFloat(state.currentInput) || 0; // LỖI: Nhầm dấu += thay vì -=
  ```
- **Cách fix chuẩn:** Đổi thành `-=`.

---

### 🔵 BUG-13: Đổi dấu số 0 biến thành '-0'
- **Mức độ:** `Minor` | **Module:** Sign Toggle
- **Các bước tái hiện:** Khi màn hình là `0`, bấm `±`
- **Kết quả thực tế:** Hiển thị `-0`
- **Vị trí code:** Trong hàm `toggleSign()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  if (state.currentInput === '0') { state.currentInput = '-0'; return; }
  ```
- **Cách fix chuẩn:** Nếu là `'0'` thì giữ nguyên không làm gì cả.

---

### 🟡 BUG-14: Nhấn phím '=' lần 2 bị reset kết quả về 0
- **Mức độ:** `Medium` | **Module:** State Continuity
- **Các bước tái hiện:** Bấm `5 + 2 =` (ra 7), bấm tiếp `=`
- **Kết quả thực tế:** Màn hình biến thành `0`
- **Vị trí code:** Trong hàm `calculate()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js) khi `!state.operation`.
- **Cách fix chuẩn:** Lưu `lastOperation` và `lastOperand` để lặp lại thao tác `7 + 2 = 9`.

---

### 🟠 BUG-15: Xóa lịch sử (Clear History) bị rò rỉ dữ liệu (Memory Leak)
- **Mức độ:** `Major` | **Module:** Data Persistence & UI Sync
- **Các bước tái hiện:** Bấm phép tính `1+1=2` -> Bấm "Xóa lịch sử" (màn hình trắng) -> Bấm phép tính `2+2=4`
- **Kết quả thực tế:** Phép tính `1+1=2` cũ bất ngờ hiện lại cùng `2+2=4`
- **Vị trí code:** Trong hàm `clearHistory()` tại [app.js](file:///Users/phamquang/Projects/calculator-qa-testing/app.js)
  ```javascript
  // state.historyData = []; // LỖI: Lập trình viên quên giải phóng mảng dữ liệu trong code!
  ```
- **Cách fix chuẩn:** Bỏ comment dòng gán `state.historyData = []`.
