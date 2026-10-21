# 📝 BẢNG KỊCH BẢN KIỂM THỬ (TEST CASES SPECIFICATION)
## DỰ ÁN: SMARTCALC PRO (v1.0)

Bảng này chứa 25 kịch bản kiểm thử mẫu được thiết kế để kiểm thử toàn diện ứng dụng máy tính và bắt trọn 15 lỗi cài cắm.

---

| Test Case ID | Module / Chức năng | Mô tả kịch bản kiểm thử | Điều kiện tiên quyết (Pre-conditions) | Các bước thực hiện (Test Steps) | Dữ liệu kiểm thử (Test Data) | Kết quả kỳ vọng (Expected Result) | Trạng thái (Thực tế) | Ghi chú Bug ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Phép cộng cơ bản | Kiểm tra phép cộng hai số nguyên dương | Màn hình là 0 | 1. Nhập '15'<br>2. Bấm '+'<br>3. Nhập '25'<br>4. Bấm '=' | `15 + 25` | Màn hình hiển thị `40` | **PASS** | - |
| **TC-02** | Phép cộng số thực | Kiểm tra cộng hai số thập phân 0.1 và 0.2 | Màn hình là 0 | 1. Nhập '0.1'<br>2. Bấm '+'<br>3. Nhập '0.2'<br>4. Bấm '=' | `0.1 + 0.2` | Màn hình hiển thị chính xác `0.3` | **FAIL** | **BUG-01** (Hiển thị 0.30000000000000004) |
| **TC-03** | Dấu thập phân | Kiểm tra nhập nhiều dấu chấm trong cùng một số | Màn hình là 0 | 1. Nhập '5'<br>2. Bấm '.'<br>3. Nhập '2'<br>4. Bấm '.'<br>5. Nhập '3' | `5.2.3` | Ứng dụng chặn dấu chấm thứ hai, chỉ cho phép `5.23` | **FAIL** | **BUG-02** (Cho phép nhập 5.2.3) |
| **TC-04** | Phép chia | Kiểm tra phép chia cho số 0 | Màn hình là 0 | 1. Nhập '9'<br>2. Bấm '÷'<br>3. Nhập '0'<br>4. Bấm '=' | `9 ÷ 0` | Hiển thị thông báo lỗi 'Cannot divide by zero' | **FAIL** | **BUG-03** (Hiển thị Infinity) |
| **TC-05** | Thứ tự ưu tiên | Kiểm tra biểu thức kết hợp nhân và cộng (BODMAS) | Màn hình là 0 | 1. Nhập '2'<br>2. Bấm '+'<br>3. Nhập '3'<br>4. Bấm '×'<br>5. Nhập '4'<br>6. Bấm '=' | `2 + 3 × 4` | Kết quả phải là `14` (nhân trước cộng sau) | **FAIL** | **BUG-04** (Bị tính tuần tự ra 20) |
| **TC-06** | Căn bậc hai | Kiểm tra tính căn bậc hai của số dương | Màn hình là 0 | 1. Nhập '16'<br>2. Bấm '√' | `√16` | Màn hình hiển thị `4` | **PASS** | - |
| **TC-07** | Căn bậc hai | Kiểm tra tính căn bậc hai của số âm | Màn hình là 0 | 1. Nhập '9'<br>2. Bấm '±' (thành -9)<br>3. Bấm '√' | `√(-9)` | Báo lỗi hợp lệ 'Invalid Input', không crash | **FAIL** | **BUG-05** (Hiển thị NaN) |
| **TC-08** | Nhập liệu số 0 | Kiểm tra nhập nhiều số 0 vô nghĩa ở đầu | Màn hình là 0 | 1. Bấm '0' 3 lần<br>2. Bấm '8' | `0008` | Màn hình chuẩn hóa thành `8` | **FAIL** | **BUG-06** (Hiển thị 0008) |
| **TC-09** | Độ dài chuỗi | Kiểm tra nhập chuỗi số vượt quá 16 chữ số | Màn hình là 0 | 1. Bấm phím '9' liên tục 25 lần | `9999...` (25 số) | Giới hạn 15-16 số hoặc tự co chữ/chuyển dạng scientific | **FAIL** | **BUG-07** (Tràn vỡ khung hiển thị) |
| **TC-10** | Phím Backspace | Kiểm tra bấm Backspace khi màn hình chỉ còn 1 số | Màn hình có số '5' | 1. Bấm phím '⌫' (Backspace) | `5` | Màn hình phải chuyển về giá trị mặc định là `0` | **FAIL** | **BUG-08** (Để lại chuỗi rỗng '') |
| **TC-11** | Nhập toán tử liên tiếp | Kiểm tra thay đổi toán tử giữa chừng | Màn hình là 0 | 1. Nhập '5'<br>2. Bấm '+'<br>3. Đổi ý bấm '×'<br>4. Nhập '2'<br>5. Bấm '=' | `5 + × 2` | Toán tử '×' thay thế '+', kết quả ra `10` | **FAIL** | **BUG-09** (Nối chuỗi biểu thức lỗi) |
| **TC-12** | Phép tính % | Kiểm tra tính phần trăm trong phép cộng | Màn hình là 0 | 1. Nhập '100'<br>2. Bấm '+'<br>3. Nhập '10'<br>4. Bấm '%'<br>5. Bấm '=' | `100 + 10%` | Kết quả phải bằng `110` | **FAIL** | **BUG-10** (Tính ra 100.1) |
| **TC-13** | Bộ nhớ tạm (Memory) | Kiểm tra chức năng nút C không được xóa Memory | Bộ nhớ đang lưu 50 | 1. Nhập '50'<br>2. Bấm 'MS'<br>3. Nhập '99'<br>4. Bấm 'C'<br>5. Bấm 'MR' | `MS: 50, C, MR` | `MR` phải phục hồi lại được giá trị `50` | **FAIL** | **BUG-11** (Bị nút C xóa về 0) |
| **TC-14** | Bộ nhớ tạm (Memory) | Kiểm tra chức năng nút M- (Memory Subtract) | Bộ nhớ đang lưu 100 | 1. Nhập '100', bấm 'MS'<br>2. Nhập '30', bấm 'M-'<br>3. Bấm 'MR' | `100 - 30` | `MR` phải hiển thị `70` | **FAIL** | **BUG-12** (Bị tính cộng dồn ra 130) |
| **TC-15** | Đổi dấu (±) | Kiểm tra đổi dấu trên số 0 | Màn hình là 0 | 1. Màn hình đang là '0'<br>2. Bấm phím '±' | `±(0)` | Màn hình vẫn phải giữ nguyên là `0` | **FAIL** | **BUG-13** (Hiển thị -0) |
| **TC-16** | Phím Bằng (=) | Kiểm tra bấm phím '=' lặp lại nhiều lần | Màn hình là 0 | 1. Nhập '5 + 2 = ' (kết quả 7)<br>2. Bấm tiếp phím '=' | `5 + 2 = =` | Lặp lại phép cộng cuối, kết quả ra `9` | **FAIL** | **BUG-14** (Bị reset về 0) |
| **TC-17** | Lịch sử (History) | Kiểm tra chức năng Xóa lịch sử và thêm phép tính mới | Có 1 phép tính trong lịch sử | 1. Thực hiện '1 + 1 = 2'<br>2. Bấm 'Xóa lịch sử'<br>3. Thực hiện '2 + 2 = 4' | `Clear History` | Lịch sử chỉ hiển thị duy nhất `2 + 2 = 4` | **FAIL** | **BUG-15** (Phép tính cũ 1+1=2 bị hiện lại) |
| **TC-18** | Bình phương (x²) | Kiểm tra hàm tính bình phương | Màn hình là 0 | 1. Nhập '8'<br>2. Bấm 'x²' | `8²` | Màn hình hiển thị `64` | **PASS** | - |
| **TC-19** | Phép trừ | Kiểm tra phép trừ cho kết quả số âm | Màn hình là 0 | 1. Nhập '10'<br>2. Bấm '-'<br>3. Nhập '25'<br>4. Bấm '=' | `10 - 25` | Màn hình hiển thị `-15` | **PASS** | - |
| **TC-20** | Phím AC | Kiểm tra xóa toàn bộ trạng thái | Màn hình có phép tính dở | 1. Nhập '123 + 45'<br>2. Bấm 'AC' | `AC` | Màn hình quay về `0`, reset mọi phép tính dở | **PASS** | - |
| **TC-21** | Tái sử dụng lịch sử | Nhấp vào mục trong lịch sử để nạp lại số | Có mục lịch sử | 1. Nhấp chuột vào thẻ lịch sử `15 + 25 = 40` | Click History item | Màn hình máy tính nạp lại số `40` | **PASS** | - |
| **TC-22** | Bàn phím số | Nhập bằng bàn phím máy tính thật | Màn hình là 0 | 1. Gõ phím cứng '1', '2', '3' trên bàn phím | Keyboard typing | Màn hình hiển thị `123` | **PASS** | - |
| **TC-23** | Bàn phím Enter | Bấm Enter trên bàn phím để tính toán | Đã nhập '4 + 6' | 1. Nhấn phím `Enter` trên bàn phím | Keyboard Enter | Màn hình hiển thị kết quả `10` | **PASS** | - |
| **TC-24** | Bàn phím Escape | Bấm Esc trên bàn phím để xóa tất cả | Đang có số trên màn hình | 1. Nhấn phím `Escape` trên bàn phím | Keyboard Esc | Tương đương nút `AC`, màn hình về `0` | **PASS** | - |
| **TC-25** | Bộ nhớ M+ | Kiểm tra chức năng nút M+ cộng dồn | Bộ nhớ là 0 | 1. Nhập '50', bấm 'M+'<br>2. Nhập '20', bấm 'M+'<br>3. Bấm 'MR' | `50 + 20` trong mem | `MR` hiển thị `70`, có biểu tượng chữ `M` trên màn hình | **PASS** | - |
