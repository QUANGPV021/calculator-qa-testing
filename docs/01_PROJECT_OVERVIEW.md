# 📱 SmartCalc Pro - Dự Án Máy Tính & Kiểm Thử Phần Mềm (QA/QC)

Chào mừng bạn đến với **SmartCalc Pro**! Đây là dự án ứng dụng máy tính bỏ túi đa năng được xây dựng nhằm phục vụ công tác đào tạo, thực hành và làm bài tập lớn môn **Kiểm thử Phần mềm (Software Testing & Quality Assurance)**.

---

## 🎯 1. Mục Tiêu Dự Án
- **Mục tiêu học thuật:** Giúp sinh viên nắm vững quy trình kiểm thử phần mềm từ việc đọc hiểu tài liệu đặc tả (SRS), lập kế hoạch test (Test Plan), thiết kế các bộ kịch bản kiểm thử (Test Cases), thực thi kiểm thử và lập báo cáo lỗi (Bug Report).
- **Mục tiêu kỹ thuật:** Cung cấp một ứng dụng máy tính trực quan, chạy trực tiếp trên trình duyệt hoặc GitHub Pages không cần cài đặt môi trường phức tạp. Ứng dụng đã được cố ý cài cắm **15 lỗi (Bugs)** thuộc nhiều cấp độ khác nhau để tester săn tìm.

---

## 📂 2. Cấu Trúc Dự Án
```text
calculator-qa-testing/
├── index.html                 # Giao diện chính của ứng dụng máy tính
├── style.css                  # Thiết kế giao diện hiện đại (Dark Glassmorphism)
├── app.js                     # Bộ xử lý logic tính toán & 15 lỗi cài cắm
├── docs/                      # Trọn bộ hồ sơ tài liệu kiểm thử dự án
│   ├── 01_PROJECT_OVERVIEW.md # Tổng quan dự án (file này)
│   ├── 02_SRS_SPECIFICATION.md# Đặc tả yêu cầu phần mềm (SRS)
│   ├── 03_TEST_PLAN.md        # Kế hoạch kiểm thử mẫu (Test Plan)
│   ├── 04_TEST_CASES.md       # Bảng Test Cases chi tiết (25+ kịch bản)
│   ├── 05_BUG_REPORT_TEMPLATE.md # Biểu mẫu báo cáo lỗi chuẩn công nghiệp
│   ├── 06_BUG_CATALOG_SECRET.md  # ĐÁP ÁN: Danh mục 15 lỗi cài cắm & Vị trí code
│   └── 07_ASSIGNMENT_GUIDE.md # Hướng dẫn làm bài & Barem chấm điểm
└── README.md                  # Hướng dẫn khởi chạy & Giới thiệu
```

---

## 🚀 3. Hướng Dẫn Khởi Chạy
### Cách 1: Chạy trực tiếp trên trình duyệt (Local)
Không cần cài đặt bất kỳ công cụ hoặc server nào:
1. Tải hoặc clone thư mục dự án về máy.
2. Nhấp đúp chuột vào file `index.html` hoặc mở bằng trình duyệt (Chrome, Edge, Firefox, Safari).

### Cách 2: Sử dụng VS Code Live Server
1. Mở thư mục dự án trong VS Code.
2. Cài extension **Live Server**.
3. Nhấp chuột phải vào `index.html` và chọn **Open with Live Server**.

### Cách 3: Bật GitHub Pages (Dành cho tester làm online)
1. Vào repository trên GitHub -> **Settings** -> **Pages**.
2. Chọn branch `main` và folder `/root`, nhấn **Save**.
3. Sau 1 phút, bạn sẽ có đường link online (ví dụ: `https://quangpv021.github.io/calculator-qa-testing/`) để gửi cho bất kỳ ai test trực tiếp.

---

## 🔍 4. Công Cụ Hỗ Trợ "QA Inspector" Dành Cho Giảng Viên / Leader
Trên giao diện ứng dụng có tích hợp sẵn thanh công cụ **"QA Inspector (Đáp án)"**:
- Cho phép xem nhanh danh sách toàn bộ 15 lỗi cài cắm.
- Bộ lọc lỗi theo mức độ nghiêm trọng (*Critical, Major, Medium, Minor*).
- Tính năng **"Tự động tái hiện lỗi này (Auto-reproduce)"**: Chỉ với 1 click, máy tính sẽ tự động mô phỏng thao tác bấm phím để kích hoạt lỗi ngay lập tức mà không cần bấm thủ công.
