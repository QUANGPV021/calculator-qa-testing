# 📋 TÀI LIỆU YÊU CẦU NGƯỜI DÙNG (URD)
## DỰ ÁN: SMARTCALC PRO (v1.0-QA)
**Học phần:** Đánh giá hiệu năng CSE3066  
**Sinh viên thực hiện:** Phạm Văn Quang - MSSV: 23110342  
**Tiêu chí chấm điểm:** A1. URD (1,0 điểm)

---

## 1. BỐI CẢNH, MỤC TIÊU VÀ PHẠM VI (CONTEXT, OBJECTIVES & SCOPE)

### 1.1. Bối cảnh
Trong môi trường giáo dục số và thực hành kỹ thuật phần mềm, nhu cầu sử dụng các công cụ tính toán số học trực quan, ổn định và có khả năng tương tác nhanh trên nền tảng web là rất cấp thiết. Đồng thời, học phần CSE3066 yêu cầu một hệ thống web application chuẩn để sinh viên thực hành kiểm thử chức năng, phi chức năng và phát hiện lỗi.

### 1.2. Mục tiêu
Xây dựng ứng dụng máy tính đa năng **SmartCalc Pro** hoạt động trực tiếp trên trình duyệt, hỗ trợ người dùng thực hiện tính toán số học, lưu trữ bộ nhớ tạm và tra cứu lịch sử thao tác với thời gian phản hồi dưới 50ms.

### 1.3. Phạm vi
Hệ thống phục vụ người dùng cá nhân (học sinh, sinh viên, kế toán) và môi trường đào tạo kiểm thử phần mềm. Bao gồm giao diện tính toán, bộ nhớ tạm thời, nhật ký lịch sử và bảng công cụ thanh tra chất lượng (QA Inspector).

---

## 2. CÁC VAI TRÒ NGƯỜI DÙNG VÀ NHU CẦU (>= 3 VAI TRÒ)

| STT | Vai trò (User Role) | Đặc điểm người dùng | Nhu cầu & Kỳ vọng chính |
| :---: | :--- | :--- | :--- |
| **1** | **Học sinh / Sinh viên (Standard User)** | Người dùng thực hiện các phép toán phục vụ học tập, bài tập số học hàng ngày. | Thao tác phím bấm nhanh, tính toán cơ bản chính xác, hỗ trợ phím cứng bàn phím, lưu nhật ký phép tính để kiểm tra lại. |
| **2** | **Kế toán / Giảng viên (Advanced User)** | Người dùng chuyên môn cần tính toán số thực, phần trăm lũy kế và lưu giá trị bộ nhớ. | Cần chức năng bộ nhớ tạm (`MS`, `MR`, `M+`, `M-`), tính phần trăm chính xác, độ chuẩn xác số thực cao không bị sai số. |
| **3** | **Chuyên viên QA / Tester (Inspector)** | Người kiểm thử phần mềm đánh giá chất lượng và tìm kiếm các khiếm khuyết hệ thống. | Cần giao diện trực quan, bảng tra cứu danh mục lỗi, khả năng tái hiện lỗi nhanh chóng để đối chiếu với tài liệu đặc tả. |

---

## 3. CÁC LUỒNG NGHIỆP VỤ Ở MỨC NGƯỜI DÙNG (>= 3 LUỒNG)

### Luồng nghiệp vụ 1: Tính toán số học cơ bản & Lưu trữ bộ nhớ tạm
1. Người dùng nhập số hạng thứ nhất (A).
2. Người dùng chọn toán tử (`+`, `-`, `×`, `÷`).
3. Người dùng nhập số hạng thứ hai (B).
4. Người dùng bấm phím `=` để xem kết quả.
5. Người dùng bấm nút `MS` để lưu kết quả vào bộ nhớ tạm (biểu tượng `M` sáng lên).
6. Người dùng bấm `C` để xóa màn hình và bấm `MR` để gọi lại giá trị bộ nhớ phục vụ phép tính tiếp theo.

### Luồng nghiệp vụ 2: Tính toán nâng cao (Căn bậc hai, Bình phương, Phần trăm)
1. Người dùng nhập một giá trị số trên màn hình.
2. Người dùng bấm phím căn bậc hai `√` hoặc bình phương `x²` $\rightarrow$ hệ thống lập tức tính toán và cập nhật màn hình hiển thị.
3. Hoặc người dùng nhập phép tính dạng `A + B%` để tính toán giá trị phần trăm tương ứng của A.

### Luồng nghiệp vụ 3: Quản lý và tái sử dụng lịch sử tính toán
1. Mỗi khi hoàn thành một phép tính bằng phím `=`, biểu thức và kết quả được tự động ghi nhận vào thanh nhật ký bên phải.
2. Người dùng có thể nhấp chuột vào một mục bất kỳ trong lịch sử để nạp lại kết quả đó vào màn hình tính toán.
3. Người dùng bấm nút "Xóa lịch sử" để làm sạch toàn bộ danh sách khi cần bảo mật dữ liệu.

---

## 4. DANH MỤC USER STORIES & TIÊU CHÍ NGHIỆM THU (ACCEPTANCE CRITERIA)

| Mã US | Nội dung User Story (Là... Tôi muốn... Để...) | Độ ưu tiên | Tiêu chí nghiệm thu (Acceptance Criteria) | Mã SRS tương ứng |
| :---: | :--- | :---: | :--- | :---: |
| **US-01** | Là một **Học sinh**, tôi muốn nhập các chữ số và phép tính (`+`, `-`, `×`, `÷`) để nhận được kết quả chính xác. | **High** | - Cho phép nhập chữ số 0-9.<br>- Tính đúng số nguyên và số thực.<br>- Hiển thị kết quả tức thì khi nhấn `=`. | `FR-01, FR-02, FR-07` |
| **US-02** | Là một **Sinh viên**, tôi muốn sử dụng bàn phím máy tính thật để nhập liệu nhanh chóng mà không cần click chuột. | **Medium** | - Hỗ trợ các phím số 0-9, dấu chấm `.`.<br>- Hỗ trợ phím `+`, `-`, `*`, `/`, `Enter`, `Backspace`, `Escape`. | `NFR-03` |
| **US-03** | Là một **Kế toán**, tôi muốn lưu giá trị vào bộ nhớ (`MS/MR/M+/M-`) để cộng dồn nhiều khoản tiền tính toán. | **High** | - `MS` lưu giá trị; `MR` gọi lại giá trị.<br>- `M+` cộng thêm; `M-` trừ đi.<br>- Hiển thị biểu tượng `M` khi có dữ liệu trong nhớ. | `FR-15, FR-16` |
| **US-04** | Là một **Người dùng**, tôi muốn xem lại danh sách các phép tính đã làm để kiểm tra sai sót. | **Medium** | - Tự động ghi nhận biểu thức và kết quả vào panel bên phải.<br>- Nhấp chuột nạp lại số vào màn hình. | `FR-17, FR-18, FR-19` |
| **US-05** | Là một **Người dùng**, tôi muốn hệ thống báo lỗi rõ ràng khi chia cho 0 hoặc căn số âm để không hiểu nhầm kết quả. | **High** | - Không hiển thị chuỗi `Infinity` hay `NaN`.<br>- Đưa ra thông báo lỗi thân thiện (`Cannot divide by 0`, `Invalid Input`). | `FR-09, FR-11` |
| **US-06** | Là một **Chuyên viên QA**, tôi muốn có bảng kiểm tra lỗi trực quan để đối chiếu kết quả kiểm thử phần mềm. | **Low** | - Có bảng QA Inspector phân loại theo 5 nhóm.<br>- Hỗ trợ nút tự động mô phỏng phím bấm tái hiện lỗi. | `FR-20` |

