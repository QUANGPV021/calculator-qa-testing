# 🧮 SmartCalc Pro - Buggy Calculator for Software Testing & QA Project

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Testing: QA Project](https://img.shields.io/badge/Testing-Academic_QA_Project-emerald.svg)]()
[![Platform: Web](https://img.shields.io/badge/Platform-HTML%20%7C%20CSS%20%7C%20JS-orange.svg)]()

> **Dự án thực hành môn Kiểm thử Phần mềm (Software Testing & Quality Assurance).**  
> Ứng dụng máy tính bỏ túi đa năng được xây dựng bằng HTML/CSS/JavaScript thuần với **15 lỗi logic, giao diện và validation có chủ đích** phục vụ sinh viên, giảng viên và tester thực hành viết kịch bản test và lập báo cáo lỗi.

---

## 🌟 Tính Năng Ứng Dụng
- **Giao diện hiện đại (Modern UI):** Thiết kế phong cách Dark mode cao cấp, hiệu ứng ánh sáng gradient, kính mờ (Glassmorphism), phông chữ kỹ thuật số sắc nét.
- **Đa dạng phép toán:**
  - Phép tính số học cơ bản: `+`, `−`, `×`, `÷`
  - Hàm tính toán nâng cao: Căn bậc hai (`√`), Bình phương (`x²`), Phần trăm (`%`), Đổi dấu (`±`)
  - Chức năng bộ nhớ: `MC`, `MR`, `M+`, `M-`, `MS`
  - Các chế độ xóa: `AC` (All Clear), `C` (Clear Entry), `⌫` (Backspace)
- **Nhật ký tính toán (History Log):** Lưu trữ danh sách phép tính, nhấp để nạp lại kết quả, đếm số lượng phép tính.
- **Hỗ trợ phím cứng:** Nhập trực tiếp từ bàn phím máy tính (`0-9`, `+`, `-`, `*`, `/`, `Enter`, `Esc`, `Backspace`).
- **Tích hợp bộ công cụ QA Inspector:**
  - Tra cứu tài liệu SRS và hướng dẫn test ngay trên ứng dụng.
  - Bảng danh mục 15 lỗi cài cắm với tính năng **"Tự động tái hiện lỗi" (Auto-reproduce)** chỉ với 1 click.

---

## 📁 Cấu Trúc Bộ Tài Liệu Kiểm Thử (Trong thư mục `/docs`)

Dự án cung cấp trọn gói bộ hồ sơ kiểm thử phần mềm chuẩn công nghiệp:

| STT | Tài liệu | Mô tả |
| :---: | :--- | :--- |
| 1 | [01_PROJECT_OVERVIEW.md](docs/01_PROJECT_OVERVIEW.md) | Tổng quan dự án, mục tiêu môn học và hướng dẫn chạy. |
| 2 | [02_SRS_SPECIFICATION.md](docs/02_SRS_SPECIFICATION.md) | Bảng đặc tả yêu cầu phần mềm (SRS) chuẩn căn cứ để đối chiếu lỗi. |
| 3 | [03_TEST_PLAN.md](docs/03_TEST_PLAN.md) | Kế hoạch kiểm thử (Test Plan IEEE 829 style). |
| 4 | [04_TEST_CASES.md](docs/04_TEST_CASES.md) | Bảng 25 kịch bản kiểm thử mẫu (Test Cases) chi tiết. |
| 5 | [05_BUG_REPORT_TEMPLATE.md](docs/05_BUG_REPORT_TEMPLATE.md) | Biểu mẫu chuẩn báo cáo lỗi (Jira / GitHub Issues format). |
| 6 | [06_BUG_CATALOG_SECRET.md](docs/06_BUG_CATALOG_SECRET.md) | **ĐÁP ÁN BÍ MẬT:** Danh mục chi tiết 15 lỗi cài cắm & Vị trí code trong `app.js`. |
| 7 | [07_ASSIGNMENT_GUIDE.md](docs/07_ASSIGNMENT_GUIDE.md) | Hướng dẫn làm bài tập lớn & Barem chấm điểm thang điểm 10. |

---

## 🚀 Hướng Dẫn Cài Đặt & Sử Dụng

### 1. Chạy trực tiếp (Không cần cài đặt)
Clone repository về máy tính và mở file `index.html` trong bất kỳ trình duyệt nào:
```bash
git clone https://github.com/QUANGPV021/calculator-qa-testing.git
cd calculator-qa-testing
open index.html # Hoặc mở đúp chuột vào file index.html
```

### 2. Triển khai lên GitHub Pages
1. Truy cập vào kho lưu trữ GitHub: **Settings** -> **Pages**.
2. Tại mục **Branch**, chọn `main` và thư mục `/ (root)`.
3. Bấm **Save**. Ứng dụng sẽ có đường dẫn trực tuyến để tester kiểm thử mọi lúc, mọi nơi!

---

## 👨‍💻 Tác Giả & Bản Quyền
- **Sinh viên thực hiện:** Phạm Văn Quang (MSSV: 23110342)
- **Môn học:** Kiểm thử Phần mềm & Lập trình nâng cao
- **Giấy phép:** MIT License
