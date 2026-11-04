# 🧮 SmartCalc Pro - Buggy Calculator for Software Testing & QA Project

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Testing: QA Project](https://img.shields.io/badge/Testing-Academic_QA_Project-emerald.svg)]()
[![Platform: Web](https://img.shields.io/badge/Platform-HTML%20%7C%20CSS%20%7C%20JS-orange.svg)]()
[![Course: CSE3066](https://img.shields.io/badge/Course-CSE3066_Performance_Evaluation-blueviolet.svg)]()

> **Dự án thực hành môn Kiểm thử Phần mềm & Đánh giá Hiệu năng (CSE3066).**  
> Ứng dụng máy tính bỏ túi đa năng được xây dựng bằng HTML/CSS/JavaScript thuần với **16 lỗi logic, giao diện, nội dung, hiệu năng và sập ứng dụng (Crash)** chuẩn 5 nhóm theo đúng Đề bài và Rubric chấm điểm của Giảng viên.

---

## 🌐 Đường Dẫn Triển Khai & Báo Cáo
- **Repository GitHub:** [https://github.com/QUANGPV021/calculator-qa-testing](https://github.com/QUANGPV021/calculator-qa-testing)
- **Website Live (GitHub Pages):** [https://quangpv021.github.io/calculator-qa-testing/](https://quangpv021.github.io/calculator-qa-testing/)
- **Thư mục Google Drive Nộp Bài:** [Drive Tài liệu_23110342](https://drive.google.com/drive/folders/1HGf_vFhYGt4W0uj3pWTIkBWyw_jsNvjv)

---

## 🌟 Tính Năng Ứng Dụng
- **Giao diện Dark Glassmorphism:** Thiết kế cao cấp, hiệu ứng kính mờ, ánh sáng neon, độ tương phản chuẩn WCAG 2.1 AA.
- **Đa dạng phép toán:**
  - Phép tính cơ bản: `+`, `−`, `×`, `÷`
  - Hàm nâng cao: Căn bậc hai (`√`), Bình phương (`x²`), Phần trăm (`%`), Đổi dấu (`±`)
  - Chức năng bộ nhớ: `MC`, `MR`, `M+`, `M-`, `MS`
  - Chế độ xóa: `AC` (All Clear), `C` (Clear Entry), `⌫` (Backspace)
- **Nhật ký tính toán (History Log):** Tự động lưu phép tính, nhấp vào thẻ để nạp lại kết quả, đếm tổng số phép tính.
- **Hỗ trợ bàn phím vật lý:** Nhập trực tiếp các phím `0-9`, `+`, `-`, `*`, `/`, `Enter`, `Esc`, `Backspace`.
- **Tích hợp bộ công cụ QA Inspector:**
  - Tra cứu tài liệu SRS và hướng dẫn test ngay trên ứng dụng.
  - Phân loại lỗi theo đúng **5 nhóm quy chuẩn của Đề bài**: *Functional, Visual, Content, Performance, Crash*.
  - Nút **"Tự động tái hiện lỗi" (Auto-reproduce)** chỉ với 1 click để giảng viên và tester kiểm tra tức thì.

---

## 🐞 Danh Mục 16 Lỗi Cài Sẵn (Chuẩn 5 Nhóm CSE3066)

| Mã lỗi | Nhóm lỗi | Mức độ | Phạm vi | Mô tả ngắn gọn lỗi |
| :---: | :---: | :---: | :---: | :--- |
| **SEED-01** | `Functional` | **Critical** | Trong đặc tả | Sai số dấu phẩy động IEEE-754: `0.1 + 0.2 = 0.30000000000000004` |
| **SEED-02** | `Functional` | **Major** | Trong đặc tả | Cho phép nhập nhiều dấu chấm thập phân trong 1 số (`5.2.3`) |
| **SEED-03** | `Functional` | **Critical** | Trong đặc tả | Phép chia cho 0 xuất hiện `Infinity` thay vì báo lỗi thân thiện |
| **SEED-04** | `Functional` | **Major** | Trong đặc tả | Vi phạm thứ tự BODMAS: `2 + 3 * 4 = 20` thay vì `14` |
| **SEED-05** | `Functional` | **Major** | Trong đặc tả | Căn bậc hai số âm xuất hiện chuỗi `NaN` |
| **SEED-06** | `Visual` | Medium | Trong đặc tả | Tràn số (Layout Overflow) ra ngoài khung máy tính khi nhập quá 16 số |
| **SEED-07** | `Visual` | Minor | Trong đặc tả | Đổi dấu số 0 biến thành `-0` và nhảy lệch sang lề trái |
| **SEED-08** | `Visual` | Minor | Trong đặc tả | Thẻ lịch sử bị vỡ khung và tràn thanh cuộn ngang khi biểu thức dài |
| **SEED-09** | `Content` | Minor | Trong đặc tả | Cho phép nhập nhiều số 0 vô nghĩa ở đầu (`0008`) |
| **SEED-10** | `Content` | **Major** | Trong đặc tả | Sai nội dung công thức %: `100 + 10% = 100.1` thay vì `110` |
| **SEED-11** | `Content` | Minor | Ngoài đặc tả | Tooltip nút C ghi sai lệch thành *"Clear All Data & Memory"* |
| **SEED-12** | `Performance`| **Major** | Ngoài đặc tả | **Đơ lag giao diện > 3 giây** khi tính bình phương do vòng lặp Main Thread nặng |
| **SEED-13** | `Performance`| **Major** | Ngoài đặc tả | **Rò rỉ bộ nhớ RAM (Memory Leak)** khi bấm Xóa lịch sử (mảng RAM không được giải phóng) |
| **SEED-14** | `Crash` | **Critical** | Ngoài đặc tả | **Sập ứng dụng (Fatal Crash)** khi bấm Backspace xóa rỗng rồi bấm tính toán |
| **SEED-15** | `Crash` | **Critical** | Ngoài đặc tả | **Trắng màn hình (White Screen 500)** khi bấm chuỗi toán tử bất thường |
| **SEED-16** | `Functional` | **Major** | Ngoài đặc tả | Nút `M-` (Memory Subtract) tính ngược thành cộng dồn vào bộ nhớ |

---

## 📁 Trọn Bộ Hồ Sơ Kiểm Thử (Khớp 100% Tiêu Chí Chấm Điểm Rubric)

### 1. Trọn bộ file nộp bài cho Giảng viên (Trong thư mục `/NOP_BAI_DRIVE`)

| STT | Tên file biểu mẫu | Tiêu chí trong Rubric | Điểm số |
| :---: | :--- | :---: | :---: |
| 1 | 📄 [`Tai_lieu_URD.docx`](NOP_BAI_DRIVE/Tai_lieu_URD.docx) | **A1. URD** (Bối cảnh, 3 vai trò, 3 luồng, User Stories + Acceptance Criteria) | **1,0 điểm** |
| 2 | 📄 [`Tai_lieu_SRS.docx`](NOP_BAI_DRIVE/Tai_lieu_SRS.docx) | **A2. SRS** (14 FR, 3 luồng hoàn chỉnh, 8 NFR, Bảng quyết định, Sơ đồ trạng thái) | **1,5 điểm** |
| 3 | 📄 [`Mau_01_Tai_lieu_API.docx`](NOP_BAI_DRIVE/Mau_01_Tai_lieu_API.docx) | **A3. Tài liệu API + Sản phẩm** | **0,5 điểm** |
| 4 | 📊 [`Mau_02_Bug_Manifest.xlsx`](NOP_BAI_DRIVE/Mau_02_Bug_Manifest.xlsx) | **A4. Bug Manifest** (16 lỗi chuẩn 13 cột và 5 nhóm) | **1,0 điểm** |
| 5 | 📄 [`Phieu_review_SRS.docx`](NOP_BAI_DRIVE/Phieu_review_SRS.docx) | **B1. Review SRS** (Phiếu phản biện SRS) | **0,5 điểm** |
| 6 | 📄 [`Mau_04_Test_Plan.docx`](NOP_BAI_DRIVE/Mau_04_Test_Plan.docx) | **B1. Test Plan** (Kế hoạch kiểm thử IEEE 829) | Đầy đủ |
| 7 | 📊 [`Mau_03_Bo_bieu_mau_Kiem_thu.xlsx`](NOP_BAI_DRIVE/Mau_03_Bo_bieu_mau_Kiem_thu.xlsx) | **B2 + B3. Test Cases & Bug Report** | **3,0 điểm** |
| 8 | 📄 [`Mau_05_Test_Summary_Report.docx`](NOP_BAI_DRIVE/Mau_05_Test_Summary_Report.docx) | **B3. Báo cáo tổng kết nghiệm thu kiểm thử** | Đầy đủ |
| 9 | 📄 [`Mau_06_Bien_ban_ban_giao.docx`](NOP_BAI_DRIVE/Mau_06_Bien_ban_ban_giao.docx) | **Biên bản bàn giao sản phẩm & tài liệu** | Đầy đủ |
| 10 | 📄 [`Checklist_truoc_khi_nop.docx`](NOP_BAI_DRIVE/Checklist_truoc_khi_nop.docx) | **Bảng kiểm tra rà soát toàn bộ tiêu chí** | Đầy đủ |

### 2. Tài liệu dạng Markdown tra cứu trực tuyến trên GitHub (Trong thư mục `/docs`)
- [00_URD_USER_REQUIREMENTS.md](docs/00_URD_USER_REQUIREMENTS.md): Đặc tả yêu cầu người dùng URD.
- [01_PROJECT_OVERVIEW.md](docs/01_PROJECT_OVERVIEW.md): Giới thiệu dự án và hướng dẫn chạy.
- [02_SRS_SPECIFICATION.md](docs/02_SRS_SPECIFICATION.md): Bảng đặc tả yêu cầu phần mềm SRS.
- [03_TEST_PLAN.md](docs/03_TEST_PLAN.md): Kế hoạch kiểm thử mẫu chuẩn IEEE 829.
- [04_TEST_CASES.md](docs/04_TEST_CASES.md) & [04_TEST_CASES.csv](docs/04_TEST_CASES.csv): 20 Test Cases chi tiết.
- [05_BUG_REPORT_TEMPLATE.md](docs/05_BUG_REPORT_TEMPLATE.md): Biểu mẫu báo cáo lỗi chuẩn.
- [06_BUG_CATALOG_SECRET.md](docs/06_BUG_CATALOG_SECRET.md): Đáp án bí mật 16 lỗi và vị trí mã nguồn trong `app.js`.
- [07_ASSIGNMENT_GUIDE.md](docs/07_ASSIGNMENT_GUIDE.md): Hướng dẫn nộp bài & Barem chấm điểm.
- [08_SRS_REVIEW.md](docs/08_SRS_REVIEW.md): Phiếu review tài liệu đặc tả SRS.

---

## 🚀 Hướng Dẫn Khởi Chạy
```bash
# Clone repository về máy tính:
git clone https://github.com/QUANGPV021/calculator-qa-testing.git
cd calculator-qa-testing

# Mở ứng dụng trên trình duyệt:
open index.html
```

---

## 👨‍💻 Tác Giả
- **Sinh viên:** Phạm Văn Quang
- **MSSV:** 23110342
- **Lớp / Học phần:** Đánh giá hiệu năng CSE3066
- **Trường:** Trường Đại học Việt Nhật - ĐHQGHN (VJU)
