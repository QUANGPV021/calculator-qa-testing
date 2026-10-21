import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

output_dir = "/Users/phamquang/Projects/calculator-qa-testing/NOP_BAI_DRIVE"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. TẠO FILE: Mau_02_Bug_Manifest.xlsx
# -------------------------------------------------------------
wb_bug = openpyxl.Workbook()
ws_bug = wb_bug.active
ws_bug.title = "Bug Manifest"

header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
border_thin = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

# Header metadata
ws_bug.merge_cells("A1:I1")
ws_bug["A1"] = "BẢNG DANH MỤC LỖI PHẦN MỀM (BUG MANIFEST) - SMARTCALC PRO"
ws_bug["A1"].font = Font(name="Calibri", size=14, bold=True, color="1F4E79")
ws_bug["A1"].alignment = Alignment(horizontal="center")

ws_bug["A2"] = "Môn học: Đánh giá hiệu năng CSE3066"
ws_bug["A2"].font = Font(name="Calibri", size=11, bold=True)
ws_bug["E2"] = "Sinh viên: Phạm Văn Quang - MSSV: 23110342"
ws_bug["E2"].font = Font(name="Calibri", size=11, bold=True)

ws_bug["A3"] = "GitHub Repo: https://github.com/QUANGPV021/calculator-qa-testing"
ws_bug["E3"] = "Demo Pages: https://quangpv021.github.io/calculator-qa-testing/"

headers_bug = [
    "Bug ID", "Phân loại", "Mô tả lỗi (Title)", "Mức độ (Severity)",
    "Các bước tái hiện (Steps)", "Kết quả thực tế (Actual)", "Kết quả kỳ vọng (Expected)",
    "Dòng code lỗi (app.js)", "Giải pháp sửa (Patch)"
]

ws_bug.append([]) # Row 4 empty
ws_bug.append(headers_bug) # Row 5

for col_idx in range(1, len(headers_bug) + 1):
    cell = ws_bug.cell(row=5, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

bugs_data = [
    # 10 Bug liên quan đến đặc tả
    ["BUG-01", "Trong đặc tả (FR-07)", "Sai số dấu phẩy động: 0.1 + 0.2 ra 0.30000000000000004", "Critical", "Nhập 0.1 -> bấm + -> nhập 0.2 -> bấm =", "0.30000000000000004", "0.3 (chuẩn hóa làm tròn số thực)", "Dòng 359: return firstVal + secondVal;", "return parseFloat((firstVal + secondVal).toFixed(12));"],
    ["BUG-02", "Trong đặc tả (FR-04)", "Cho phép nhập nhiều dấu chấm thập phân trong 1 số (5.2.3)", "Major", "Nhập 5 -> bấm . -> nhập 2 -> bấm . -> nhập 3", "Màn hình hiển thị 5.2.3", "Chỉ cho phép duy nhất 1 dấu chấm (5.23)", "Dòng 321: if (state.currentInput.endsWith('.'))", "if (state.currentInput.includes('.')) return;"],
    ["BUG-03", "Trong đặc tả (FR-09)", "Phép chia cho 0 trả về Infinity thay vì báo lỗi", "Critical", "Nhập 9 -> bấm ÷ -> nhập 0 -> bấm =", "Hiển thị 'Infinity'", "Thông báo lỗi: 'Cannot divide by 0'", "Dòng 371: if (secondVal === 0) return Infinity;", "return 'Cannot divide by 0'; khóa thao tác tính."],
    ["BUG-04", "Trong đặc tả (FR-08)", "Vi phạm thứ tự ưu tiên BODMAS: 2 + 3 * 4 ra 20", "Major", "Nhập 2 -> bấm + -> nhập 3 -> bấm × -> nhập 4 -> =", "Tính tuần tự ra 20", "Kết quả đúng toán học là 14 (nhân chia trước)", "Dòng 342: tính dồn ngay khi gặp toán tử mới", "Áp dụng thuật toán Shunting-yard parse biểu thức."],
    ["BUG-05", "Trong đặc tả (FR-11)", "Căn bậc hai số âm xuất hiện chuỗi 'NaN'", "Major", "Nhập 9 -> bấm ± (thành -9) -> bấm √", "Hiển thị chuỗi 'NaN'", "Báo lỗi hợp lệ 'Invalid Input'", "Dòng 424: Math.sqrt(val) thiếu kiểm tra val < 0", "if (val < 0) return 'Invalid Input';"],
    ["BUG-06", "Trong đặc tả (FR-03)", "Cho phép nhập nhiều số 0 vô nghĩa ở đầu (0008)", "Minor", "Bấm 0 liên tiếp 3 lần -> bấm 8", "Hiển thị '0008'", "Tự động chuẩn hóa thành '8'", "Dòng 297: state.currentInput = '00';", "state.currentInput = digit;"],
    ["BUG-07", "Trong đặc tả (FR-05)", "Tràn viền màn hình máy tính khi nhập quá 16 chữ số", "Medium", "Nhập liên tục 25 chữ số 9", "Chữ số tràn vỡ ra ngoài khung máy tính", "Giới hạn 15-16 số hoặc tự co chữ / e-notation", "Thiếu giới hạn maxlength và CSS overflow", "Thêm if (length >= 15) return và font scaling."],
    ["BUG-08", "Trong đặc tả (FR-06)", "Nút Backspace (⌫) xóa ký tự cuối làm rỗng màn hình", "Medium", "Màn hình có số 5 -> bấm ⌫ -> bấm +", "Màn hình trống rỗng '', bấm tiếp sinh NaN", "Màn hình phải quay về số 0 mặc định", "Dòng 403: state.currentInput = '';", "state.currentInput = '0';"],
    ["BUG-09", "Trong đặc tả (FR-10)", "Nhấn liên tiếp toán tử làm hỏng biểu thức (5 + × 2)", "Major", "Nhập 5 -> bấm + -> bấm × -> nhập 2 -> bấm =", "Toán tử bị nối chuỗi '5 + ×'", "Toán tử sau (×) tự động thay thế toán tử trước (+)", "Dòng 333: state.operation = state.operation + ' ' + nextOp;", "state.operation = nextOp; (ghi đè toán tử)."],
    ["BUG-10", "Trong đặc tả (FR-14)", "Tính phần trăm sai quy tắc: 100 + 10% ra 100.1", "Major", "Nhập 100 -> bấm + -> nhập 10 -> bấm % -> bấm =", "Tính ra 100.1 (chia 10 cho 100 rồi cộng)", "110 (100 + 10% của 100)", "Dòng 434: state.currentInput = `${val / 100}`;", "Cộng phần trăm dựa trên số hạng thứ nhất."],
    # 5 Bug ngoài đặc tả
    ["BUG-11", "Ngoài đặc tả (Edge)", "Nút 'C' (Clear Entry) xóa luôn biến nhớ Memory", "Medium", "Lưu 50 vào MS -> nhập 99 -> bấm C -> bấm MR", "MR trả về 0 (bộ nhớ bị xóa trắng)", "MR phải giữ nguyên giá trị 50 đã lưu", "Dòng 413: state.memoryValue = 0; trong clearEntry()", "Bỏ dòng xóa memoryValue, C chỉ xóa màn hình."],
    ["BUG-12", "Ngoài đặc tả (Logic)", "Nút 'M-' (Memory Subtract) tính ngược thành cộng", "Major", "Lưu 100 vào MS -> nhập 30 -> bấm M- -> bấm MR", "MR ra 130 (bị cộng dồn 30)", "MR ra 70 (100 - 30)", "Dòng 450: state.memoryValue += val; (nhầm dấu)", "Đổi thành state.memoryValue -= val;"],
    ["BUG-13", "Ngoài đặc tả (UI/UX)", "Đổi dấu số 0 biến thành số '-0'", "Minor", "Màn hình đang là 0 -> bấm nút ±", "Màn hình hiển thị '-0'", "Vẫn giữ nguyên là '0'", "Dòng 418: if (state.currentInput === '0') '-0'", "if (state.currentInput === '0') return;"],
    ["BUG-14", "Ngoài đặc tả (State)", "Bấm phím '=' lần 2 bị reset kết quả về 0", "Medium", "Bấm 5 + 2 = (kết quả 7) -> bấm tiếp =", "Màn hình bị xóa về 0", "Lặp lại phép tính cuối: 7 + 2 = 9", "Dòng 383: if (!state.operation) currentInput = '0';", "Lưu lastOperation và lastOperand để tính lặp."],
    ["BUG-15", "Ngoài đặc tả (Data)", "Xóa lịch sử (Clear History) bị rò rỉ dữ liệu cũ", "Major", "Tính 1+1=2 -> Bấm Xóa lịch sử -> Tính tiếp 2+2=4", "Phép tính cũ 1+1=2 tự động phục hồi lại", "Lịch sử chỉ lưu duy nhất 2+2=4", "Dòng 473: comment out dòng state.historyData = []", "Bỏ comment state.historyData = []; khi bấm xóa."]
]

for row_data in bugs_data:
    ws_bug.append(row_data)

for row in ws_bug.iter_rows(min_row=5, max_row=len(bugs_data)+5, min_col=1, max_col=len(headers_bug)):
    for cell in row:
        cell.border = border_thin
        if cell.row > 5:
            cell.font = Font(name="Calibri", size=10)
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            if cell.column == 1:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = Font(name="Calibri", size=10, bold=True)
            elif cell.column == 4:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                if cell.value == "Critical":
                    cell.fill = PatternFill(start_color="FCE4D6", fill_type="solid")
                    cell.font = Font(name="Calibri", size=10, bold=True, color="C00000")
                elif cell.value == "Major":
                    cell.fill = PatternFill(start_color="FFF2CC", fill_type="solid")
                    cell.font = Font(name="Calibri", size=10, bold=True, color="B25900")

col_widths = [12, 18, 30, 14, 28, 25, 25, 30, 30]
for idx, w in enumerate(col_widths, start=1):
    ws_bug.column_dimensions[get_column_letter(idx)].width = w

wb_bug.save(os.path.join(output_dir, "Mau_02_Bug_Manifest.xlsx"))
print("Done Mau_02_Bug_Manifest.xlsx")

# -------------------------------------------------------------
# 2. TẠO FILE: Mau_03_Bo_bieu_mau_Kiem_thu.xlsx
# -------------------------------------------------------------
wb_test = openpyxl.Workbook()
ws_tc = wb_test.active
ws_tc.title = "Test Cases"

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

test_cases_rows = [
    ["TC-01", "Phép tính cơ bản", "Kiểm tra phép cộng hai số nguyên dương", "Màn hình là 0", "1. Nhập 15\n2. Bấm +\n3. Nhập 25\n4. Bấm =", "15 + 25", "Màn hình hiển thị 40", "PASS"],
    ["TC-02", "Phép tính cơ bản", "Kiểm tra cộng hai số thập phân 0.1 và 0.2", "Màn hình là 0", "1. Nhập 0.1\n2. Bấm +\n3. Nhập 0.2\n4. Bấm =", "0.1 + 0.2", "Màn hình hiển thị chính xác 0.3", "FAIL (BUG-01)"],
    ["TC-03", "Kiểm tra nhập liệu", "Kiểm tra nhập nhiều dấu chấm trong 1 số", "Màn hình là 0", "1. Nhập 5\n2. Bấm .\n3. Nhập 2\n4. Bấm .\n5. Nhập 3", "5.2.3", "Chỉ nhận 1 dấu chấm (5.23)", "FAIL (BUG-02)"],
    ["TC-04", "Phép chia", "Kiểm tra phép chia cho số 0", "Màn hình là 0", "1. Nhập 9\n2. Bấm ÷\n3. Nhập 0\n4. Bấm =", "9 ÷ 0", "Báo lỗi Cannot divide by 0", "FAIL (BUG-03)"],
    ["TC-05", "Độ ưu tiên toán học", "Kiểm tra kết hợp nhân và cộng (BODMAS)", "Màn hình là 0", "1. Nhập 2\n2. Bấm +\n3. Nhập 3\n4. Bấm ×\n5. Nhập 4\n6. Bấm =", "2 + 3 × 4", "Kết quả phải là 14", "FAIL (BUG-04)"],
    ["TC-06", "Hàm nâng cao", "Kiểm tra tính căn bậc hai số dương", "Màn hình là 0", "1. Nhập 16\n2. Bấm √", "√16", "Hiển thị 4", "PASS"],
    ["TC-07", "Hàm nâng cao", "Kiểm tra tính căn bậc hai số âm", "Màn hình là 0", "1. Nhập 9 -> Bấm ± (-9)\n2. Bấm √", "√(-9)", "Báo lỗi Invalid Input", "FAIL (BUG-05)"],
    ["TC-08", "Kiểm tra nhập liệu", "Kiểm tra nhập nhiều số 0 vô nghĩa ở đầu", "Màn hình là 0", "1. Bấm 0 ba lần\n2. Bấm 8", "0008", "Chuẩn hóa thành 8", "FAIL (BUG-06)"],
    ["TC-09", "Giới hạn giao diện", "Kiểm tra nhập chuỗi số dài hơn 16 số", "Màn hình là 0", "1. Bấm phím 9 liên tục 25 lần", "25 số 9", "Giới hạn 15 ký tự hoặc co chữ e-notation", "FAIL (BUG-07)"],
    ["TC-10", "Xóa ký tự", "Kiểm tra phím Backspace khi còn 1 số", "Màn hình có số 5", "1. Bấm phím ⌫", "5 -> ⌫", "Màn hình quay về 0", "FAIL (BUG-08)"],
    ["TC-11", "Toán tử liên tiếp", "Kiểm tra thay đổi toán tử giữa chừng", "Màn hình là 0", "1. Nhập 5 -> Bấm +\n2. Bấm × -> Nhập 2 -> Bấm =", "5 + × 2", "Toán tử × thay thế +, kết quả là 10", "FAIL (BUG-09)"],
    ["TC-12", "Phần trăm", "Kiểm tra tính % trong phép cộng", "Màn hình là 0", "1. Nhập 100 -> Bấm +\n2. Nhập 10 -> Bấm % -> Bấm =", "100 + 10%", "Kết quả phải bằng 110", "FAIL (BUG-10)"],
    ["TC-13", "Bộ nhớ tạm", "Kiểm tra nút C không được xóa Memory", "Bộ nhớ lưu 50", "1. Nhập 50 -> Bấm MS\n2. Nhập 99 -> Bấm C\n3. Bấm MR", "MS: 50, C, MR", "MR phục hồi lại số 50", "FAIL (BUG-11)"],
    ["TC-14", "Bộ nhớ tạm", "Kiểm tra nút M- (Memory Subtract)", "Bộ nhớ lưu 100", "1. Nhập 100 -> MS\n2. Nhập 30 -> M-\n3. Bấm MR", "100 - 30", "MR hiển thị 70", "FAIL (BUG-12)"],
    ["TC-15", "Đổi dấu", "Kiểm tra đổi dấu trên số 0", "Màn hình là 0", "1. Màn hình là 0 -> Bấm ±", "±(0)", "Giữ nguyên là 0", "FAIL (BUG-13)"],
    ["TC-16", "Phím Bằng", "Kiểm tra bấm phím = lặp lại", "Màn hình là 0", "1. Nhập 5 + 2 = (ra 7)\n2. Bấm tiếp phím =", "5 + 2 = =", "Tiếp tục cộng 2 thành 9", "FAIL (BUG-14)"],
    ["TC-17", "Nhật ký lịch sử", "Kiểm tra xóa lịch sử và tính phép mới", "Có lịch sử", "1. Tính 1+1=2\n2. Bấm Xóa lịch sử\n3. Tính 2+2=4", "Clear History", "Lịch sử chỉ chứa duy nhất 2+2=4", "FAIL (BUG-15)"],
    ["TC-18", "Bình phương", "Kiểm tra hàm tính bình phương", "Màn hình là 0", "1. Nhập 8 -> Bấm x²", "8²", "Hiển thị 64", "PASS"],
    ["TC-19", "Phép trừ", "Kiểm tra phép trừ ra số âm", "Màn hình là 0", "1. Nhập 10 - 25 =", "10 - 25", "Hiển thị -15", "PASS"],
    ["TC-20", "Phím AC", "Kiểm tra xóa sạch trạng thái", "Màn hình có số dở", "1. Nhập 9999 -> Bấm AC", "AC", "Màn hình về 0, reset mọi thứ", "PASS"]
]

for row_data in test_cases_rows:
    ws_tc.append(row_data)

for row in ws_tc.iter_rows(min_row=4, max_row=len(test_cases_rows)+4, min_col=1, max_col=len(headers_tc)):
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

col_widths_tc = [14, 18, 30, 16, 26, 16, 26, 16]
for idx, w in enumerate(col_widths_tc, start=1):
    ws_tc.column_dimensions[get_column_letter(idx)].width = w

wb_test.save(os.path.join(output_dir, "Mau_03_Bo_bieu_mau_Kiem_thu.xlsx"))
print("Done Mau_03_Bo_bieu_mau_Kiem_thu.xlsx")

# -------------------------------------------------------------
# 3. TẠO CÁC FILE WORD (.docx): Mau_01, Mau_04, Mau_05, Mau_06, Checklist
# -------------------------------------------------------------

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
    p_meta.add_run("Dự án: ").bold = True
    p_meta.add_run("SmartCalc Pro (Máy tính bỏ túi phục vụ kiểm thử phần mềm)\n")
    p_meta.add_run("Repository GitHub: ").bold = True
    p_meta.add_run("https://github.com/QUANGPV021/calculator-qa-testing\n")
    p_meta.add_run("Trang web triển khai (GitHub Pages): ").bold = True
    p_meta.add_run("https://quangpv021.github.io/calculator-qa-testing/\n")
    doc.add_paragraph().add_run("-" * 70)

# Mau_01_Tai_lieu_API.docx
doc_api = docx.Document()
set_doc_header(doc_api, "MẪU 01: TÀI LIỆU ĐẶC TẢ TÍNH NĂNG & GIAO DIỆN (SRS / API)", "Dự án: SmartCalc Pro v1.0")
doc_api.add_heading("1. Giới thiệu tổng quan", level=1)
doc_api.add_paragraph("Ứng dụng SmartCalc Pro là một máy tính bỏ túi đa năng được xây dựng nhằm mô phỏng hệ thống tính toán toán học và phục vụ công tác kiểm thử phần mềm. Ứng dụng cung cấp các hàm xử lý tính toán số học, bộ nhớ tạm thời và lịch sử thao tác.")
doc_api.add_heading("2. Đặc tả các hàm và chức năng chính (Core Functions & APIs)", level=1)
table_api = doc_api.add_table(rows=1, cols=4)
hdr_cells = table_api.rows[0].cells
hdr_cells[0].text = "Tên Hàm / Action"
hdr_cells[1].text = "Tham số đầu vào"
hdr_cells[2].text = "Mô tả chức năng"
hdr_cells[3].text = "Kết quả trả về"
api_rows = [
    ("inputDigit(digit)", "digit: string ('0'-'9')", "Nhập chữ số vào màn hình tính toán", "Cập nhật state.currentInput"),
    ("inputDecimal()", "Không", "Thêm dấu chấm thập phân vào toán hạng hiện tại", "Thêm '.' nếu hợp lệ"),
    ("handleOperator(op)", "op: string ('+', '-', '×', '÷')", "Ghi nhận phép toán và tính toán trung gian", "Lưu operator vào state"),
    ("calculate()", "Không", "Thực hiện phép tính bằng dấu '='", "Hiển thị kết quả ra màn hình"),
    ("calcSquareRoot()", "Không", "Tính căn bậc hai (√) của giá trị hiện tại", "Căn bậc hai số dương, báo lỗi nếu âm"),
    ("memoryStore() / Recall()", "Không", "Lưu vào (MS) hoặc gọi lại (MR) giá trị bộ nhớ", "Cập nhật memoryValue"),
    ("clearAll() / clearEntry()", "Không", "Xóa toàn bộ (AC) hoặc xóa mục đang nhập (C)", "Reset màn hình"),
    ("clearHistory()", "Không", "Làm sạch danh sách lịch sử phép tính", "Xóa mảng historyData và UI")
]
for r in api_rows:
    row_cells = table_api.add_row().cells
    for i in range(4):
        row_cells[i].text = r[i]
doc_api.save(os.path.join(output_dir, "Mau_01_Tai_lieu_API.docx"))
print("Done Mau_01_Tai_lieu_API.docx")

# Mau_04_Test_Plan.docx
doc_tp = docx.Document()
set_doc_header(doc_tp, "MẪU 04: KẾ HOẠCH KIỂM THỬ (TEST PLAN)", "Chuẩn IEEE 829 - Dự án SmartCalc Pro")
doc_tp.add_heading("1. Mục tiêu và Phạm vi", level=1)
doc_tp.add_paragraph("Kiểm tra toàn diện các chức năng tính toán số học, xử lý ranh giới dữ liệu, kiểm tra giao diện và tính toàn vẹn bộ nhớ của ứng dụng máy tính.")
doc_tp.add_heading("2. Chiến lược kiểm thử", level=1)
doc_tp.add_paragraph("- Phân vùng tương đương (Equivalence Partitioning): Số dương, âm, số 0, số thập phân.\n- Phân tích giá trị biên (Boundary Value Analysis): Giới hạn ký tự màn hình, chia cho 0.\n- Kiểm thử chuyển trạng thái (State Transition): Chuỗi thao tác bộ nhớ tạm MS -> C -> MR.\n- Kỹ thuật đoán lỗi (Error Guessing): Bấm nhiều dấu chấm, chia cho 0, xóa ký tự rỗng.")
doc_tp.add_heading("3. Tiêu chí dừng kiểm thử", level=1)
doc_tp.add_paragraph("Toàn bộ 20 test cases được thực thi; 100% các lỗi nghiêm trọng (Critical, Major) được phân loại và lập Bug Report đầy đủ.")
doc_tp.save(os.path.join(output_dir, "Mau_04_Test_Plan.docx"))
print("Done Mau_04_Test_Plan.docx")

# Mau_05_Test_Summary_Report.docx
doc_tsr = docx.Document()
set_doc_header(doc_tsr, "MẪU 05: BÁO CÁO TỔNG KẾT KIỂM THỬ (TEST SUMMARY REPORT)", "Báo cáo nghiệm thu kết quả kiểm thử")
doc_tsr.add_heading("1. Tóm tắt kết quả thực thi", level=1)
doc_tsr.add_paragraph("- Tổng số Test Cases thiết kế: 20 kịch bản.\n- Số Test Cases Passed: 5 kịch bản (25%).\n- Số Test Cases Failed: 15 kịch bản (75%).")
doc_tsr.add_heading("2. Thống kê lỗi phát hiện được", level=1)
doc_tsr.add_paragraph("- Tổng số lỗi phát hiện: 15 lỗi.\n  + Lỗi trong đặc tả: 10 lỗi (Đạt chỉ tiêu tối thiểu 10 bug đặc tả).\n  + Lỗi ngoài đặc tả: 5 lỗi (Vượt chỉ tiêu tối thiểu 3 bug ngoài đặc tả).\n- Phân loại theo Severity:\n  + Critical: 2 lỗi (BUG-01, BUG-03)\n  + Major: 6 lỗi (BUG-02, BUG-04, BUG-05, BUG-09, BUG-10, BUG-12, BUG-15)\n  + Medium: 4 lỗi (BUG-07, BUG-08, BUG-11, BUG-14)\n  + Minor: 2 lỗi (BUG-06, BUG-13)")
doc_tsr.add_heading("3. Đánh giá chất lượng và kết luận", level=1)
doc_tsr.add_paragraph("Hệ thống máy tính hiện tại chứa nhiều lỗi logic toán học và bảo toàn dữ liệu. Cần phải áp dụng các bản vá (Patches) đề xuất trong Bug Manifest trước khi đưa vào phát hành chính thức.")
doc_tsr.save(os.path.join(output_dir, "Mau_05_Test_Summary_Report.docx"))
print("Done Mau_05_Test_Summary_Report.docx")

# Mau_06_Bien_ban_ban_giao.docx
doc_bb = docx.Document()
set_doc_header(doc_bb, "MẪU 06: BIÊN BẢN BÀN GIAO SẢN PHẨM & TÀI LIỆU KIỂM THỬ", "Học phần Đánh giá hiệu năng CSE3066")
doc_bb.add_heading("1. Thông tin bàn giao", level=1)
doc_bb.add_paragraph("Hôm nay, ngày 21/10/2026, sinh viên bàn giao sản phẩm dự án kiểm thử phần mềm cho Giảng viên hướng dẫn học phần CSE3066.")
doc_bb.add_heading("2. Danh mục sản phẩm bàn giao", level=1)
doc_bb.add_paragraph("1. Mã nguồn ứng dụng Web: https://github.com/QUANGPV021/calculator-qa-testing\n2. Trang web thực thi trực tuyến: https://quangpv021.github.io/calculator-qa-testing/\n3. File Mau_01_Tai_lieu_API.docx: Đặc tả hàm và cấu trúc.\n4. File Mau_02_Bug_Manifest.xlsx: Danh mục 15 lỗi (10 trong đặc tả, 5 ngoài đặc tả).\n5. File Mau_03_Bo_bieu_mau_Kiem_thu.xlsx: 20 Test Cases chi tiết.\n6. File Mau_04_Test_Plan.docx: Kế hoạch kiểm thử hoàn chỉnh.\n7. File Mau_05_Test_Summary_Report.docx: Báo cáo tổng kết kiểm thử.")
doc_bb.save(os.path.join(output_dir, "Mau_06_Bien_ban_ban_giao.docx"))
print("Done Mau_06_Bien_ban_ban_giao.docx")

# Checklist_truoc_khi_nop.docx
doc_ck = docx.Document()
set_doc_header(doc_ck, "CHECKLIST KIỂM TRA TRƯỚC KHI NỘP BÀI", "Học phần Đánh giá hiệu năng CSE3066")
doc_ck.add_heading("Danh sách các mục đã hoàn thành:", level=1)
items = [
    "[x] 1. Khai báo Domain Website (GitHub Pages) tại phần About của Repository GitHub.",
    "[x] 2. Hoàn thành Mau_01_Tai_lieu_API.docx đầy đủ thông tin.",
    "[x] 3. Hoàn thành Mau_02_Bug_Manifest.xlsx (10 bug trong đặc tả + 5 bug ngoài đặc tả).",
    "[x] 4. Hoàn thành Mau_03_Bo_bieu_mau_Kiem_thu.xlsx (Bộ kịch bản kiểm thử).",
    "[x] 5. Hoàn thành Mau_04_Test_Plan.docx (Kế hoạch test).",
    "[x] 6. Hoàn thành Mau_05_Test_Summary_Report.docx (Tổng kết test).",
    "[x] 7. Hoàn thành Mau_06_Bien_ban_ban_giao.docx.",
    "[x] 8. Tải đầy đủ toàn bộ file lên thư mục Google Drive cá nhân."
]
for it in items:
    doc_ck.add_paragraph(it)
doc_ck.save(os.path.join(output_dir, "Checklist_truoc_khi_nop.docx"))
print("Done Checklist_truoc_khi_nop.docx")
