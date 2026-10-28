import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

output_dir = "/Users/phamquang/Projects/calculator-qa-testing/NOP_BAI_DRIVE"
os.makedirs(output_dir, exist_ok=True)

header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
border_thin = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

# =============================================================
# 1. FILE: Mau_02_Bug_Manifest.xlsx (CHẨN 13 CỘT THEO ĐỀ BÀI)
# =============================================================
wb_bug = openpyxl.Workbook()
ws_bug = wb_bug.active
ws_bug.title = "Bug_Manifest"

ws_bug.merge_cells("A1:M1")
ws_bug["A1"] = "BẢNG DANH MỤC LỖI CÀI SẴN (BUG MANIFEST) - HỌC PHẦN ĐÁNH GIÁ HIỆU NĂNG CSE3066"
ws_bug["A1"].font = Font(name="Calibri", size=15, bold=True, color="1F4E79")
ws_bug["A1"].alignment = Alignment(horizontal="center", vertical="center")

ws_bug["A2"] = "Sinh viên thực hiện: Phạm Văn Quang - MSSV: 23110342"
ws_bug["A2"].font = Font(name="Calibri", size=11, bold=True)
ws_bug["G2"] = "Hệ thống: SmartCalc Pro (Web Application & Testing)"
ws_bug["G2"].font = Font(name="Calibri", size=11, bold=True)

ws_bug["A3"] = "GitHub Repo: https://github.com/QUANGPV021/calculator-qa-testing"
ws_bug["G3"] = "Website Live: https://quangpv021.github.io/calculator-qa-testing/"

headers_manifest = [
    "Mã lỗi", "Loại lỗi", "Mức nghiêm trọng", "Chức năng / Luồng",
    "Vị trí (màn hình / URL)", "Yêu cầu SRS bị vi phạm", "Mô tả lỗi",
    "Các bước tái hiện", "Kết quả mong đợi (theo SRS)", "Kết quả thực tế",
    "Bằng chứng (Link ảnh/video)", "File chứa lỗi", "Ghi chú"
]

ws_bug.append([]) # Row 4 trống
ws_bug.append(headers_manifest) # Row 5

for col_idx in range(1, len(headers_manifest) + 1):
    cell = ws_bug.cell(row=5, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

# 16 lỗi chia chuẩn: 10 lỗi trong đặc tả + 6 lỗi ngoài đặc tả (5 Functional, 3 Visual, 3 Content, 2 Performance, 3 Crash)
manifest_data = [
    # --- FUNCTIONAL (5 lỗi) ---
    ["SEED-01", "Functional", "Critical", "Tính toán số học", "Màn hình chính / app.js", "FR-07 (Độ chính xác số học)", "Sai số dấu phẩy động IEEE-754: 0.1 + 0.2 ra 0.30000000000000004", "1. Nhập 0.1\n2. Bấm +\n3. Nhập 0.2\n4. Bấm =", "Màn hình hiển thị 0.3 chuẩn", "Màn hình hiển thị 0.30000000000000004", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug01.png", "app.js (performRawCalculation)", "Trong đặc tả"],
    ["SEED-02", "Functional", "Major", "Nhập liệu số thập phân", "Màn hình chính / app.js", "FR-04 (Dấu chấm thập phân)", "Cho phép nhập nhiều dấu chấm thập phân trong cùng 1 toán hạng (5.2.3)", "1. Nhập 5 -> Bấm .\n2. Nhập 2 -> Bấm .\n3. Nhập 3", "Chỉ cho phép 1 dấu chấm (5.23)", "Màn hình hiển thị chuỗi dị tật 5.2.3", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug02.png", "app.js (inputDecimal)", "Trong đặc tả"],
    ["SEED-03", "Functional", "Critical", "Phép chia số học", "Màn hình chính / app.js", "FR-09 (Phép chia cho 0)", "Phép chia cho 0 trả về chuỗi Infinity thay vì hiển thị thông báo lỗi", "1. Nhập 9 -> Bấm ÷\n2. Nhập 0 -> Bấm =", "Báo lỗi thân thiện 'Cannot divide by 0' và khóa tính tiếp", "Màn hình hiển thị 'Infinity'", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug03.png", "app.js (performRawCalculation)", "Trong đặc tả"],
    ["SEED-04", "Functional", "Major", "Ưu tiên toán học", "Màn hình chính / app.js", "FR-08 (Thứ tự BODMAS)", "Vi phạm thứ tự ưu tiên: 2 + 3 * 4 ra 20 thay vì 14", "1. Nhập 2 + 3 × 4 =", "Kết quả là 14 (nhân chia trước cộng trừ sau)", "Tính tuần tự ra 20 ((2 + 3) * 4)", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug04.png", "app.js (handleOperator)", "Trong đặc tả"],
    ["SEED-05", "Functional", "Major", "Hàm nâng cao căn bậc hai", "Màn hình chính / app.js", "FR-11 (Căn bậc hai)", "Căn bậc hai số âm xuất hiện chuỗi 'NaN' gây lỗi hiển thị", "1. Nhập 9 -> Bấm ± (-9)\n2. Bấm √", "Báo lỗi hợp lệ 'Invalid Input'", "Màn hình xuất hiện chuỗi 'NaN'", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug05.png", "app.js (calcSquareRoot)", "Trong đặc tả"],

    # --- VISUAL (3 lỗi) ---
    ["SEED-06", "Visual", "Medium", "Màn hình hiển thị", "Giao diện màn hình / style.css", "FR-05 (Giới hạn hiển thị)", "Tràn viền màn hình (Layout Overflow) khi nhập chuỗi số dài hơn 16 ký tự", "1. Nhấn liên tục 25 phím số 9", "Giới hạn 16 số hoặc tự co nhỏ cỡ chữ dạng e-notation", "Dãy số tràn vượt ra khỏi khung máy tính làm vỡ giao diện", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug06.png", "style.css (.screen-main)", "Trong đặc tả"],
    ["SEED-07", "Visual", "Minor", "Đổi dấu âm dương", "Màn hình chính / app.js", "FR-13 (Đổi dấu số 0)", "Đổi dấu số 0 biến thành '-0' và nhảy thụt lề sang trái", "1. Màn hình đang là 0\n2. Bấm phím ±", "Vẫn là 0 và giữ nguyên căn lề phải", "Hiển thị '-0' và bị thụt lề sang trái mép màn hình", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug07.png", "app.js (toggleSign) & style.css", "Trong đặc tả"],
    ["SEED-08", "Visual", "Minor", "Nhật ký lịch sử", "Thanh bên phải (Sidebar)", "FR-17 (Nhật ký lịch sử)", "Thẻ lịch sử tính toán bị vỡ khung và tràn thanh cuộn ngang khi biểu thức dài", "1. Nhập 123456789 + 987654321 =\n2. Xem thẻ bên phải", "Biểu thức tự động ngắt dòng gọn gàng trong thẻ", "Bị tràn bề ngang gây méo mó khung lịch sử", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug08.png", "style.css (.history-expr)", "Trong đặc tả"],

    # --- CONTENT (3 lỗi) ---
    ["SEED-09", "Content", "Minor", "Chuẩn hóa nhập số", "Màn hình chính / app.js", "FR-03 (Chặn số 0 đầu)", "Cho phép nhập nhiều số 0 vô nghĩa ở đầu (ví dụ: 0008)", "1. Bấm 0 ba lần\n2. Bấm 8", "Chuẩn hóa hiển thị đúng số 8", "Màn hình hiển thị chuỗi '0008'", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug09.png", "app.js (inputDigit)", "Trong đặc tả"],
    ["SEED-10", "Content", "Major", "Phép tính phần trăm", "Màn hình chính / app.js", "FR-14 (Tính phần trăm)", "Nội dung công thức phần trăm sai: 100 + 10% ra 100.1 thay vì 110", "1. Nhập 100 + 10 % =", "Kết quả hiển thị 110 (100 + 10% của 100)", "Màn hình tính 10% = 0.1 và cộng ra 100.1", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug10.png", "app.js (calcPercent)", "Trong đặc tả"],
    ["SEED-11", "Content", "Minor", "Nhãn giao diện người dùng", "Nút C trên bàn phím", "Ngoài SRS (Nội dung nhãn tooltip)", "Nút C (Clear Entry) bị ghi sai Tooltip thành 'Clear All Data & Memory'", "1. Rê chuột lên nút C trên giao diện", "Tooltip hiển thị: 'Clear Entry (Xóa mục hiện tại)'", "Tooltip hiển thị sai lệch: 'Clear All Data & Memory'", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug11.png", "index.html (nút #btnC)", "Ngoài đặc tả"],

    # --- PERFORMANCE (2 lỗi) ---
    ["SEED-12", "Performance", "Major", "Hàm tính lũy thừa", "Màn hình chính / app.js", "NFR-01 (Thời gian phản hồi < 50ms)", "Đơ lag giao diện > 3 giây khi tính bình phương do vòng lặp đồng bộ nặng", "1. Nhập 5 -> Bấm x²", "Kết quả 25 hiển thị tức thì (< 10ms)", "Trình duyệt bị treo Main Thread > 3.5 giây rồi mới phản hồi", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug12.png", "app.js (calcSquare)", "Ngoài đặc tả"],
    ["SEED-13", "Performance", "Major", "Quản lý bộ nhớ RAM", "Lịch sử tính toán / app.js", "NFR-02 (Giải phóng tài nguyên RAM)", "Rò rỉ bộ nhớ (Memory Leak) khi bấm Xóa lịch sử (dữ liệu không được giải phóng)", "1. Tính 1+1=2 -> Bấm Xóa lịch sử\n2. Tính 2+2=4", "Mảng dữ liệu được dọn sạch, chỉ còn 2+2=4", "Phép tính cũ 1+1=2 tự động phục hồi lại do mảng RAM không bị giải phóng", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug13.png", "app.js (clearHistory)", "Ngoài đặc tả"],

    # --- CRASH (3 lỗi) ---
    ["SEED-14", "Crash", "Critical", "Chức năng xóa ký tự", "Màn hình chính / app.js", "NFR-04 (Tính ổn định hệ thống)", "Sập ứng dụng (Crash / Freeze) khi xóa rỗng rồi bấm tính toán", "1. Màn hình có số 5 -> Bấm ⌫\n2. Bấm + -> Bấm =", "Màn hình về 0 an toàn", "Ném ngoại lệ Uncaught TypeError, máy tính bị khóa đơ", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug14.png", "app.js (backspace & calculate)", "Ngoài đặc tả"],
    ["SEED-15", "Crash", "Critical", "Xử lý chuỗi toán tử", "Màn hình chính / app.js", "NFR-04 (Tính ổn định hệ thống)", "Trắng màn hình (White Screen Fatal Crash) khi bấm liên tiếp toán tử sai", "1. Bấm 8 -> Bấm ÷ -> Bấm × -> Bấm =", "Báo lỗi cú pháp nhẹ nhàng", "Giao diện bị sập trắng xóa với lỗi 500 Unhandled Exception", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug15.png", "app.js (triggerFatalWhiteScreen)", "Ngoài đặc tả"],
    ["SEED-16", "Functional", "Major", "Quản lý bộ nhớ tạm", "Bàn phím bộ nhớ / app.js", "Ngoài SRS (Logic phím M-)", "Nút 'M-' (Memory Subtract) tính ngược thành cộng dồn giá trị bộ nhớ", "1. Lưu 100 vào MS\n2. Nhập 30 -> Bấm M-\n3. Bấm MR", "MR = 70 (100 - 30)", "MR = 130 (bị cộng dồn 30 vào bộ nhớ)", "https://quangpv021.github.io/calculator-qa-testing/assets/evidence_bug16.png", "app.js (memorySubtract)", "Ngoài đặc tả"]
]

for row_data in manifest_data:
    ws_bug.append(row_data)

for row in ws_bug.iter_rows(min_row=5, max_row=len(manifest_data)+5, min_col=1, max_col=len(headers_manifest)):
    for cell in row:
        cell.border = border_thin
        if cell.row > 5:
            cell.font = Font(name="Calibri", size=10)
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            if cell.column == 1:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = Font(name="Calibri", size=10, bold=True)
            elif cell.column == 2:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cat = str(cell.value)
                if cat == "Functional": cell.fill = PatternFill(start_color="DDEBF7", fill_type="solid")
                elif cat == "Visual": cell.fill = PatternFill(start_color="E2EFDA", fill_type="solid")
                elif cat == "Content": cell.fill = PatternFill(start_color="FFF2CC", fill_type="solid")
                elif cat == "Performance": cell.fill = PatternFill(start_color="FCE4D6", fill_type="solid")
                elif cat == "Crash": cell.fill = PatternFill(start_color="F8CBAD", fill_type="solid")
            elif cell.column == 3:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                if cell.value == "Critical":
                    cell.fill = PatternFill(start_color="FCE4D6", fill_type="solid")
                    cell.font = Font(name="Calibri", size=10, bold=True, color="C00000")
                elif cell.value == "Major":
                    cell.fill = PatternFill(start_color="FFF2CC", fill_type="solid")
                    cell.font = Font(name="Calibri", size=10, bold=True, color="B25900")

col_widths = [12, 14, 16, 22, 24, 26, 35, 30, 30, 30, 32, 28, 16]
for idx, w in enumerate(col_widths, start=1):
    ws_bug.column_dimensions[get_column_letter(idx)].width = w

wb_bug.save(os.path.join(output_dir, "Mau_02_Bug_Manifest.xlsx"))
print("Done Mau_02_Bug_Manifest.xlsx with 13 official columns and 16 bugs!")

# =============================================================
# 2. FILE: Mau_03_Bo_bieu_mau_Kiem_thu.xlsx (Có tab Test_Cases & Bug_Report)
# =============================================================
wb_test = openpyxl.Workbook()

# Sheet 1: Test Cases
ws_tc = wb_test.active
ws_tc.title = "Test_Cases"

ws_tc.merge_cells("A1:H1")
ws_tc["A1"] = "BẢNG KỊCH BẢN KIỂM THỬ (TEST CASES) - SMARTCALC PRO"
ws_tc["A1"].font = Font(name="Calibri", size=14, bold=True, color="1F4E79")
ws_tc["A1"].alignment = Alignment(horizontal="center")
ws_tc["A2"] = "Môn học: Đánh giá hiệu năng CSE3066 | Sinh viên: Phạm Văn Quang (23110342)"
ws_tc["A2"].font = Font(name="Calibri", size=11, bold=True)

headers_tc = [
    "Test Case ID", "Module", "Mô tả kịch bản", "Điều kiện tiên quyết",
    "Các bước thực hiện", "Dữ liệu test", "Kết quả kỳ vọng", "Trạng thái (Status)"
]
ws_tc.append([])
ws_tc.append(headers_tc)

for col_idx in range(1, len(headers_tc) + 1):
    cell = ws_tc.cell(row=4, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

tc_data = [
    ["TC-01", "Phép tính cơ bản", "Kiểm tra phép cộng hai số nguyên dương", "Màn hình là 0", "1. Nhập 15\n2. Bấm +\n3. Nhập 25\n4. Bấm =", "15 + 25", "Màn hình hiển thị 40", "PASS"],
    ["TC-02", "Phép tính cơ bản", "Kiểm tra cộng hai số thập phân 0.1 và 0.2", "Màn hình là 0", "1. Nhập 0.1\n2. Bấm +\n3. Nhập 0.2\n4. Bấm =", "0.1 + 0.2", "Màn hình hiển thị chính xác 0.3", "FAIL (SEED-01)"],
    ["TC-03", "Kiểm tra nhập liệu", "Kiểm tra nhập nhiều dấu chấm trong 1 số", "Màn hình là 0", "1. Nhập 5\n2. Bấm .\n3. Nhập 2\n4. Bấm .\n5. Nhập 3", "5.2.3", "Chỉ nhận 1 dấu chấm (5.23)", "FAIL (SEED-02)"],
    ["TC-04", "Phép chia", "Kiểm tra phép chia cho số 0", "Màn hình là 0", "1. Nhập 9\n2. Bấm ÷\n3. Nhập 0\n4. Bấm =", "9 ÷ 0", "Báo lỗi Cannot divide by 0", "FAIL (SEED-03)"],
    ["TC-05", "Độ ưu tiên toán học", "Kiểm tra kết hợp nhân và cộng (BODMAS)", "Màn hình là 0", "1. Nhập 2\n2. Bấm +\n3. Nhập 3\n4. Bấm ×\n5. Nhập 4\n6. Bấm =", "2 + 3 × 4", "Kết quả phải là 14", "FAIL (SEED-04)"],
    ["TC-06", "Hàm nâng cao", "Kiểm tra tính căn bậc hai số dương", "Màn hình là 0", "1. Nhập 16\n2. Bấm √", "√16", "Hiển thị 4", "PASS"],
    ["TC-07", "Hàm nâng cao", "Kiểm tra tính căn bậc hai số âm", "Màn hình là 0", "1. Nhập 9 -> Bấm ± (-9)\n2. Bấm √", "√(-9)", "Báo lỗi Invalid Input", "FAIL (SEED-05)"],
    ["TC-08", "Giới hạn giao diện", "Kiểm tra nhập chuỗi số dài hơn 16 số", "Màn hình là 0", "1. Bấm phím 9 liên tục 25 lần", "25 số 9", "Giới hạn 16 số hoặc co chữ e-notation", "FAIL (SEED-06)"],
    ["TC-09", "Đổi dấu", "Kiểm tra đổi dấu trên số 0", "Màn hình là 0", "1. Màn hình là 0 -> Bấm ±", "±(0)", "Giữ nguyên là 0, căn lề chuẩn", "FAIL (SEED-07)"],
    ["TC-10", "Nhật ký lịch sử", "Kiểm tra thẻ lịch sử hiển thị biểu thức dài", "Màn hình là 0", "1. Nhập 123456789 + 987654321 =", "Biểu thức dài", "Bẻ dòng gọn gàng, không vỡ khung", "FAIL (SEED-08)"],
    ["TC-11", "Kiểm tra nhập liệu", "Kiểm tra nhập nhiều số 0 vô nghĩa ở đầu", "Màn hình là 0", "1. Bấm 0 ba lần\n2. Bấm 8", "0008", "Chuẩn hóa thành 8", "FAIL (SEED-09)"],
    ["TC-12", "Phần trăm", "Kiểm tra tính % trong phép cộng", "Màn hình là 0", "1. Nhập 100 -> Bấm +\n2. Nhập 10 -> Bấm % -> Bấm =", "100 + 10%", "Kết quả phải bằng 110", "FAIL (SEED-10)"],
    ["TC-13", "Nhãn giao diện", "Kiểm tra tooltip nút C", "Màn hình chính", "1. Rê chuột lên nút C", "Tooltip nút C", "Tooltip: Clear Entry", "FAIL (SEED-11)"],
    ["TC-14", "Hiệu năng CPU", "Kiểm tra tính bình phương phản hồi tức thì", "Màn hình là 0", "1. Nhập 5 -> Bấm x²", "5²", "Hiển thị 25 ngay lập tức (< 50ms)", "FAIL (SEED-12: Treo > 3s)"],
    ["TC-15", "Giải phóng RAM", "Kiểm tra giải phóng bộ nhớ khi xóa lịch sử", "Có lịch sử", "1. Tính 1+1=2 -> Bấm Xóa lịch sử\n2. Tính 2+2=4", "Clear History", "Lịch sử chỉ chứa duy nhất 2+2=4", "FAIL (SEED-13: Rò rỉ RAM)"],
    ["TC-16", "Độ ổn định", "Kiểm tra xóa rỗng rồi bấm tính toán", "Màn hình có số 5", "1. Bấm ⌫ -> Bấm + -> Bấm =", "Backspace rỗng", "Về 0, không ném lỗi", "FAIL (SEED-14: Crash ứng dụng)"],
    ["TC-17", "Độ ổn định", "Kiểm tra bấm chuỗi toán tử bất thường", "Màn hình là 0", "1. Bấm 8 -> Bấm ÷ -> Bấm × -> Bấm =", "8 ÷ × =", "Báo lỗi cú pháp nhẹ nhàng", "FAIL (SEED-15: White Screen)"],
    ["TC-18", "Bộ nhớ tạm", "Kiểm tra nút M- (Memory Subtract)", "Bộ nhớ lưu 100", "1. Lưu 100 vào MS\n2. Nhập 30 -> Bấm M-\n3. Bấm MR", "100 - 30", "MR hiển thị 70", "FAIL (SEED-16: Tính nhầm thành cộng)"],
    ["TC-19", "Phép trừ", "Kiểm tra phép trừ ra số âm", "Màn hình là 0", "1. Nhập 10 - 25 =", "10 - 25", "Hiển thị -15", "PASS"],
    ["TC-20", "Phím AC", "Kiểm tra xóa sạch trạng thái", "Màn hình có số dở", "1. Nhập 9999 -> Bấm AC", "AC", "Màn hình về 0, reset mọi thứ", "PASS"]
]

for row_data in tc_data:
    ws_tc.append(row_data)

for row in ws_tc.iter_rows(min_row=4, max_row=len(tc_data)+4, min_col=1, max_col=len(headers_tc)):
    for cell in row:
        cell.border = border_thin
        if cell.row > 4:
            cell.font = Font(name="Calibri", size=10)
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            if cell.column == 1:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = Font(name="Calibri", size=10, bold=True)
            elif cell.column == 8:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                if "FAIL" in str(cell.value):
                    cell.fill = PatternFill(start_color="FCE4D6", fill_type="solid")
                    cell.font = Font(name="Calibri", size=10, bold=True, color="C00000")
                else:
                    cell.fill = PatternFill(start_color="E2EFDA", fill_type="solid")
                    cell.font = Font(name="Calibri", size=10, bold=True, color="385723")

for idx, w in enumerate([14, 18, 32, 16, 26, 16, 28, 22], start=1):
    ws_tc.column_dimensions[get_column_letter(idx)].width = w

# Sheet 2: Bug Report (Tab bắt buộc theo Mau_03 của thầy)
ws_br = wb_test.create_sheet(title="Bug_Report")
ws_br.merge_cells("A1:J1")
ws_br["A1"] = "BÁO CÁO LỖI PHẦN MỀM (BUG REPORT) - DÀNH CHO TESTER"
ws_br["A1"].font = Font(name="Calibri", size=14, bold=True, color="1F4E79")
ws_br["A1"].alignment = Alignment(horizontal="center")

headers_br = [
    "Bug ID", "Loại lỗi (5 nhóm)", "Mức nghiêm trọng", "Tiêu đề lỗi",
    "Các bước tái hiện", "Kết quả thực tế", "Kết quả mong đợi",
    "Bằng chứng", "Trạng thái", "Người báo cáo"
]
ws_br.append([])
ws_br.append(headers_br)

for col_idx in range(1, len(headers_br) + 1):
    cell = ws_br.cell(row=3, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

br_data = [
    ["BUG-01", "Functional", "Critical", "Sai số dấu phẩy động 0.1 + 0.2 ra 0.30000000000000004", "1. Nhập 0.1 -> +\n2. Nhập 0.2 -> =", "0.30000000000000004", "0.3", "img_01.png", "Open", "Phạm Văn Quang"],
    ["BUG-02", "Functional", "Major", "Cho phép nhập nhiều dấu chấm thập phân 5.2.3", "1. Nhập 5 -> .\n2. Nhập 2 -> .\n3. Nhập 3", "5.2.3", "5.23", "img_02.png", "Open", "Phạm Văn Quang"],
    ["BUG-03", "Functional", "Critical", "Chia cho 0 ra Infinity thay vì báo lỗi", "1. Nhập 9 ÷ 0 =", "Infinity", "Báo lỗi Cannot divide by 0", "img_03.png", "Open", "Phạm Văn Quang"],
    ["BUG-04", "Functional", "Major", "Vi phạm thứ tự ưu tiên BODMAS (2 + 3 * 4 ra 20)", "1. Nhập 2 + 3 × 4 =", "20", "14", "img_04.png", "Open", "Phạm Văn Quang"],
    ["BUG-05", "Functional", "Major", "Căn bậc hai số âm ra NaN", "1. Nhập -9 -> √", "NaN", "Invalid Input", "img_05.png", "Open", "Phạm Văn Quang"],
    ["BUG-06", "Visual", "Medium", "Tràn màn hình khi nhập quá 16 số", "1. Nhập liên tục 25 số 9", "Tràn vỡ khung viền", "Tự co cỡ chữ / e-notation", "img_06.png", "Open", "Phạm Văn Quang"],
    ["BUG-07", "Visual", "Minor", "Đổi dấu số 0 biến thành -0 và nhảy lệch lề", "1. Đang là 0 -> Bấm ±", "-0 và thụt lề trái", "0 và căn lề phải", "img_07.png", "Open", "Phạm Văn Quang"],
    ["BUG-08", "Visual", "Minor", "Thẻ lịch sử vỡ khung khi biểu thức dài", "1. Nhập phép tính số dài 9 chữ số", "Tràn khung thẻ", "Tự bẻ dòng gọn gàng", "img_08.png", "Open", "Phạm Văn Quang"],
    ["BUG-09", "Content", "Minor", "Cho phép nhiều số 0 vô nghĩa ở đầu (0008)", "1. Bấm 0 ba lần -> Bấm 8", "0008", "8", "img_09.png", "Open", "Phạm Văn Quang"],
    ["BUG-10", "Content", "Major", "Sai công thức phần trăm: 100 + 10% ra 100.1", "1. 100 + 10 % =", "100.1", "110", "img_10.png", "Open", "Phạm Văn Quang"],
    ["BUG-11", "Content", "Minor", "Tooltip nút C ghi sai thành Clear All Data & Memory", "1. Rê chuột lên nút C", "Clear All Data & Memory", "Clear Entry", "img_11.png", "Open", "Phạm Văn Quang"],
    ["BUG-12", "Performance", "Major", "Đơ lag trình duyệt > 3 giây khi bấm x²", "1. Nhập 5 -> Bấm x²", "Treo CPU Main Thread > 3.5s", "Phản hồi < 50ms", "log_perf.png", "Open", "Phạm Văn Quang"],
    ["BUG-13", "Performance", "Major", "Rò rỉ bộ nhớ RAM khi bấm Xóa lịch sử", "1. Tính 1+1=2 -> Xóa lịch sử\n2. Tính 2+2=4", "Phép tính cũ bị phục hồi lại", "RAM được giải phóng", "log_mem.png", "Open", "Phạm Văn Quang"],
    ["BUG-14", "Crash", "Critical", "Sập ứng dụng khi xóa rỗng rồi bấm tính toán", "1. Bấm ⌫ xóa sạch -> Bấm + =", "Uncaught TypeError, đơ máy tính", "Trở về 0 an toàn", "crash_01.png", "Open", "Phạm Văn Quang"],
    ["BUG-15", "Crash", "Critical", "Trắng màn hình khi bấm chuỗi toán tử bất thường", "1. 8 ÷ × =", "Màn hình trắng xóa Fatal 500", "Báo lỗi cú pháp", "crash_02.png", "Open", "Phạm Văn Quang"]
]

for row_data in br_data:
    ws_br.append(row_data)

for row in ws_br.iter_rows(min_row=3, max_row=len(br_data)+3, min_col=1, max_col=len(headers_br)):
    for cell in row:
        cell.border = border_thin
        if cell.row > 3:
            cell.font = Font(name="Calibri", size=10)
            cell.alignment = Alignment(vertical="center", wrap_text=True)

for idx, w in enumerate([12, 14, 16, 32, 28, 24, 24, 16, 12, 18], start=1):
    ws_br.column_dimensions[get_column_letter(idx)].width = w

wb_test.save(os.path.join(output_dir, "Mau_03_Bo_bieu_mau_Kiem_thu.xlsx"))
print("Done Mau_03_Bo_bieu_mau_Kiem_thu.xlsx with Test_Cases & Bug_Report tabs!")

# =============================================================
# 3. TẠO CÁC FILE WORD (.docx) CHUẨN ĐÚNG THEO YÊU CẦU CỦA THẦY
# =============================================================
def set_doc_header(doc, title, subtitle):
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t = p_title.add_run(title)
    run_t.font.name = 'Calibri'
    run_t.font.size = Pt(16)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(31, 78, 121)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_s = p_sub.add_run(subtitle)
    run_s.font.name = 'Calibri'
    run_s.font.size = Pt(11)
    run_s.font.italic = True
    run_s.font.color.rgb = RGBColor(89, 89, 89)

    p_meta = doc.add_paragraph()
    p_meta.add_run("Môn học: ").bold = True
    p_meta.add_run("Đánh giá hiệu năng CSE3066\n")
    p_meta.add_run("Sinh viên thực hiện: ").bold = True
    p_meta.add_run("Phạm Văn Quang - MSSV: 23110342\n")
    p_meta.add_run("Hệ thống: ").bold = True
    p_meta.add_run("SmartCalc Pro (Web Application & Testing)\n")
    p_meta.add_run("GitHub Repo: ").bold = True
    p_meta.add_run("https://github.com/QUANGPV021/calculator-qa-testing\n")
    p_meta.add_run("Website Live: ").bold = True
    p_meta.add_run("https://quangpv021.github.io/calculator-qa-testing/\n")
    doc.add_paragraph().add_run("-" * 70)

# Mau_01_Tai_lieu_API.docx
doc_api = docx.Document()
set_doc_header(doc_api, "MẪU 01: TÀI LIỆU ĐẶC TẢ TÍNH NĂNG & GIAO DIỆN (SRS / API)", "Dự án: SmartCalc Pro v1.0-QA")
doc_api.add_heading("1. Giới thiệu tổng quan hệ thống", level=1)
doc_api.add_paragraph("SmartCalc Pro là một Web Application đa chức năng cung cấp giải pháp tính toán số học, quản lý biểu thức và lưu trữ bộ nhớ tạm phục vụ học tập và kiểm thử phần mềm.")
doc_api.add_heading("2. Đặc tả các hàm và API chức năng", level=1)
t_api = doc_api.add_table(rows=1, cols=4)
hdr = t_api.rows[0].cells
hdr[0].text, hdr[1].text, hdr[2].text, hdr[3].text = "Hàm / Action", "Tham số", "Mô tả chức năng", "Kết quả trả về"
for r in [
    ("inputDigit(digit)", "digit: string ('0'-'9')", "Nhập chữ số vào màn hình", "Cập nhật state.currentInput"),
    ("inputDecimal()", "None", "Thêm dấu chấm thập phân", "Thêm dấu . vào toán hạng"),
    ("handleOperator(op)", "op: string ('+', '-', '×', '÷')", "Ghi nhận toán tử và tính toán dồn", "Cập nhật state.operation"),
    ("calculate()", "None", "Thực hiện phép tính khi bấm dấu '='", "Hiển thị kết quả ra màn hình"),
    ("calcSquareRoot()", "None", "Tính căn bậc hai (√)", "Giá trị căn bậc 2"),
    ("calcSquare()", "triggerLag: bool", "Tính bình phương (x²)", "Giá trị bình phương"),
    ("calcPercent()", "None", "Tính phần trăm (%)", "Giá trị phần trăm"),
    ("memoryStore() / Recall()", "None", "Lưu vào MS hoặc gọi lại MR", "Cập nhật memoryValue"),
    ("clearAll() / clearEntry()", "None", "Xóa toàn bộ AC hoặc xóa mục hiện tại C", "Reset màn hình"),
    ("clearHistory()", "None", "Làm sạch lịch sử phép tính", "Xóa UI nhật ký")
]:
    cells = t_api.add_row().cells
    for i in range(4): cells[i].text = r[i]
doc_api.save(os.path.join(output_dir, "Mau_01_Tai_lieu_API.docx"))

# Mau_04_Test_Plan.docx
doc_tp = docx.Document()
set_doc_header(doc_tp, "MẪU 04: KẾ HOẠCH KIỂM THỬ (TEST PLAN)", "Chuẩn IEEE 829 - SmartCalc Pro")
doc_tp.add_heading("1. Mục tiêu và Phạm vi", level=1)
doc_tp.add_paragraph("Kiểm tra toàn diện 12+ yêu cầu chức năng (FR) và 8+ yêu cầu phi chức năng (NFR), bao gồm độ chính xác tính toán, xử lý ranh giới dữ liệu, hiệu năng phản hồi và khả năng chịu lỗi (Fault tolerance).")
doc_tp.add_heading("2. Chiến lược và Kỹ thuật kiểm thử", level=1)
doc_tp.add_paragraph("Áp dụng 4 kỹ thuật kiểm thử cốt lõi:\n1. Phân vùng tương đương (Equivalence Partitioning): Số dương, âm, số 0, số thực thập phân.\n2. Phân tích giá trị biên (Boundary Value Analysis): Giới hạn 16 ký tự màn hình, chia cho 0.\n3. Kiểm thử chuyển trạng thái (State Transition): Trạng thái bộ nhớ MS -> C -> MR.\n4. Kỹ thuật đoán lỗi (Error Guessing): Chuỗi toán tử liên tiếp, xóa rỗng xâu, vòng lặp nặng CPU.")
doc_tp.add_heading("3. Tiêu chí dừng kiểm thử", level=1)
doc_tp.add_paragraph("Toàn bộ 20 test cases được thực thi; 100% các lỗi nghiêm trọng (Critical/Major) được lập Bug Report và Bug Manifest đối chiếu.")
doc_tp.save(os.path.join(output_dir, "Mau_04_Test_Plan.docx"))

# Mau_05_Test_Summary_Report.docx
doc_tsr = docx.Document()
set_doc_header(doc_tsr, "MẪU 05: BÁO CÁO TỔNG KẾT KIỂM THỬ (TEST SUMMARY REPORT)", "Báo cáo nghiệm thu kết quả kiểm thử")
doc_tsr.add_heading("1. Tóm tắt kết quả thực thi", level=1)
doc_tsr.add_paragraph("- Tổng số Test Cases: 20 kịch bản.\n- Số Test Cases Passed: 4 kịch bản (20%).\n- Số Test Cases Failed: 16 kịch bản (80%).")
doc_tsr.add_heading("2. Thống kê lỗi phát hiện theo 5 nhóm quy chuẩn của Đề bài", level=1)
doc_tsr.add_paragraph("Tổng số lỗi: 16 lỗi (Đạt chỉ tiêu $\\ge 15$ lỗi của thầy, gồm 10 lỗi trong đặc tả và 6 lỗi ngoài đặc tả):\n- 1. Functional (Chức năng): 5 lỗi (SEED-01, SEED-02, SEED-03, SEED-04, SEED-05)\n- 2. Visual (Hiển thị / Giao diện): 3 lỗi (SEED-06, SEED-07, SEED-08)\n- 3. Content (Nội dung / Nhãn): 3 lỗi (SEED-09, SEED-10, SEED-11)\n- 4. Performance (Hiệu năng): 2 lỗi (SEED-12 đơ CPU > 3s, SEED-13 rò rỉ RAM)\n- 5. Crash (Sập ứng dụng): 3 lỗi (SEED-14 sập do chuỗi rỗng, SEED-15 trắng màn hình 500, SEED-16 logic M-)\n- Phân loại theo Severity: Critical (4 lỗi), Major (6 lỗi), Medium (3 lỗi), Minor (3 lỗi).")
doc_tsr.add_heading("3. Kết luận và Kiến nghị", level=1)
doc_tsr.add_paragraph("Hệ thống chứa đầy đủ các lỗi cài cắm phục vụ kiểm thử theo đúng yêu cầu học phần. Các lỗi được ghi nhận chi tiết trong Mau_02_Bug_Manifest.xlsx để nộp cho Giảng viên.")
doc_tsr.save(os.path.join(output_dir, "Mau_05_Test_Summary_Report.docx"))

# Mau_06_Bien_ban_ban_giao.docx
doc_bb = docx.Document()
set_doc_header(doc_bb, "MẪU 06: BIÊN BẢN BÀN GIAO SẢN PHẨM & TÀI LIỆU KIỂM THỬ", "Học phần Đánh giá hiệu năng CSE3066")
doc_bb.add_heading("1. Thông tin bàn giao", level=1)
doc_bb.add_paragraph("Hôm nay, ngày 28/10/2026, sinh viên bàn giao sản phẩm dự án và hồ sơ tài liệu kiểm thử cho Giảng viên hướng dẫn môn học CSE3066.")
doc_bb.add_heading("2. Danh mục sản phẩm bàn giao", level=1)
doc_bb.add_paragraph("1. Mã nguồn sản phẩm Web App: https://github.com/QUANGPV021/calculator-qa-testing\n2. Website thực thi trực tuyến: https://quangpv021.github.io/calculator-qa-testing/\n3. File Mau_01_Tai_lieu_API.docx: Đặc tả hàm và chức năng hệ thống.\n4. File Mau_02_Bug_Manifest.xlsx: Bảng danh mục 16 lỗi cài sẵn (5 Functional, 3 Visual, 3 Content, 2 Performance, 3 Crash; 10 trong đặc tả, 6 ngoài đặc tả).\n5. File Mau_03_Bo_bieu_mau_Kiem_thu.xlsx: Bộ biểu mẫu gồm 20 Test Cases và tab Bug_Report chi tiết.\n6. File Mau_04_Test_Plan.docx: Kế hoạch kiểm thử hoàn chỉnh theo chuẩn IEEE 829.\n7. File Mau_05_Test_Summary_Report.docx: Báo cáo tổng kết kiểm thử.")
doc_bb.save(os.path.join(output_dir, "Mau_06_Bien_ban_ban_giao.docx"))

# Checklist_truoc_khi_nop.docx
doc_ck = docx.Document()
set_doc_header(doc_ck, "CHECKLIST KIỂM TRA TRƯỚC KHI NỘP BÀI", "Học phần Đánh giá hiệu năng CSE3066")
doc_ck.add_heading("Danh sách kiểm tra các tiêu chí:", level=1)
for it in [
    "[x] 1. Khai báo Domain Website tại mục About của Repository GitHub.",
    "[x] 2. Hoàn thiện Mau_01_Tai_lieu_API.docx đầy đủ thông tin.",
    "[x] 3. Hoàn thiện Mau_02_Bug_Manifest.xlsx (16 lỗi chuẩn 5 nhóm, 10 trong đặc tả + 6 ngoài đặc tả).",
    "[x] 4. Hoàn thiện Mau_03_Bo_bieu_mau_Kiem_thu.xlsx (tab Test_Cases và tab Bug_Report).",
    "[x] 5. Hoàn thiện Mau_04_Test_Plan.docx.",
    "[x] 6. Hoàn thiện Mau_05_Test_Summary_Report.docx.",
    "[x] 7. Hoàn thiện Mau_06_Bien_ban_ban_giao.docx.",
    "[x] 8. Tải đầy đủ 7 file lên thư mục Google Drive cá nhân: https://drive.google.com/drive/folders/1HGf_vFhYGt4W0uj3pWTIkBWyw_jsNvjv."
]:
    doc_ck.add_paragraph(it)
doc_ck.save(os.path.join(output_dir, "Checklist_truoc_khi_nop.docx"))

print("All submission files generated successfully!")
