import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import shutil

project_dir = "/Users/phamquang/Projects/calculator-qa-testing"
output_dir = os.path.join(project_dir, "NOP_2_FILE_DRIVE")
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. TẠO FILE THỨ NHẤT: TAI_LIEU_DU_AN_CSE3066_23110342.docx
# -------------------------------------------------------------
doc = docx.Document()

# Thiết lập lề trang
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1.2)
    section.right_margin = Inches(1)

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def style_header_cell(cell, text):
    set_cell_background(cell, "1F4E79")
    cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = cell.paragraphs[0].add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(10)
    run.font.bold = True
    run.font.color.rgb = RGBColor(255, 255, 255)

def style_body_cell(cell, text, bold=False, center=False):
    if center:
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = cell.paragraphs[0].add_run(text)
    run.font.name = 'Calibri'
    run.font.size = Pt(9.5)
    run.font.bold = bold

# --- TRANG BÌA BÁO CÁO ---
p_inst = doc.add_paragraph()
p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_inst = p_inst.add_run("ĐẠI HỌC QUỐC GIA HÀ NỘI\nTRƯỜNG ĐẠI HỌC VIỆT NHẬT (VJU)\n")
r_inst.font.name = 'Calibri'
r_inst.font.size = Pt(12)
r_inst.font.bold = True

doc.add_paragraph("\n" * 3)

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_title = p_title.add_run("BÁO CÁO TỔNG HỢP HỒ SƠ TÀI LIỆU DỰ ÁN\nHỌC PHẦN: ĐÁNH GIÁ HIỆU NĂNG (CSE3066)\n")
r_title.font.name = 'Calibri'
r_title.font.size = Pt(18)
r_title.font.bold = True
r_title.font.color.rgb = RGBColor(31, 78, 121)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_sub = p_sub.add_run("HỆ THỐNG MÁY TÍNH BỎ TÚI SMARTCALC PRO & HỒ SƠ KIỂM THỬ\n(Bao gồm URD, SRS, API, Test Plan, Test Cases, Review & Test Summary Report)")
r_sub.font.name = 'Calibri'
r_sub.font.size = Pt(11)
r_sub.font.italic = True
r_sub.font.color.rgb = RGBColor(89, 89, 89)

doc.add_paragraph("\n" * 4)

p_info = doc.add_paragraph()
p_info.paragraph_format.left_indent = Inches(1.5)
p_info.add_run("Sinh viên thực hiện: ").bold = True
p_info.add_run("Phạm Văn Quang\n")
p_info.add_run("Mã số sinh viên: ").bold = True
p_info.add_run("23110342\n")
p_info.add_run("Học phần: ").bold = True
p_info.add_run("Đánh giá hiệu năng (CSE3066)\n")
p_info.add_run("Repository GitHub: ").bold = True
p_info.add_run("https://github.com/QUANGPV021/calculator-qa-testing\n")
p_info.add_run("Website trực tuyến: ").bold = True
p_info.add_run("https://quangpv021.github.io/calculator-qa-testing/\n")

doc.add_paragraph("\n" * 4)
p_date = doc.add_paragraph()
p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_date.add_run("Hà Nội, Năm học 2026")

doc.add_page_break()

# --- MỤC LỤC TỔNG HỢP ---
doc.add_heading("MỤC LỤC BÁO CÁO TỔNG HỢP", level=1)
doc.add_paragraph(
    "PHẦN 1. TÀI LIỆU YÊU CẦU NGƯỜI DÙNG (URD - TIÊU CHÍ A1: 1,0 ĐIỂM)\n"
    "PHẦN 2. ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS - TIÊU CHÍ A2: 1,5 ĐIỂM)\n"
    "PHẦN 3. ĐẶC TẢ HÀM VÀ API HỆ THỐNG (API SPEC - TIÊU CHÍ A3: 0,5 ĐIỂM)\n"
    "PHẦN 4. KẾ HOẠCH KIỂM THỬ PHẦN MỀM (TEST PLAN - TIÊU CHÍ B1)\n"
    "PHẦN 5. BỘ KỊCH BẢN KIỂM THỬ CHI TIẾT (TEST CASES - TIÊU CHÍ B2: 1,5 ĐIỂM)\n"
    "PHẦN 6. PHIẾU REVIEW SRS & BÁO CÁO TỔNG KẾT KIỂM THỬ (TSR - TIÊU CHÍ B1, B3)\n"
    "PHẦN 7. BIÊN BẢN BÀN GIAO SẢN PHẨM & CHECKLIST RÀ SOÁT"
)
doc.add_paragraph("-" * 75)

# --- PHẦN 1: URD ---
doc.add_heading("PHẦN 1. TÀI LIỆU YÊU CẦU NGƯỜI DÙNG (URD)", level=1)
doc.add_paragraph(
    "1. Bối cảnh & Mục tiêu:\n"
    "SmartCalc Pro là Web Application máy tính trực quan, đáp ứng nhu cầu tính toán hàng ngày và kiểm thử phần mềm học phần CSE3066. "
    "Mục tiêu là cung cấp hệ thống chạy trực tiếp trên web với thời gian phản hồi < 50ms, bảo toàn trạng thái bộ nhớ và nhật ký lịch sử."
)

doc.add_heading("1.1. Các vai trò người dùng (>= 3 vai trò)", level=2)
t_roles = doc.add_table(rows=1, cols=3)
hdr = t_roles.rows[0].cells
style_header_cell(hdr[0], "Vai trò (Role)")
style_header_cell(hdr[1], "Đặc điểm người dùng")
style_header_cell(hdr[2], "Nhu cầu & Kỳ vọng chính")
for r in [
    ("1. Học sinh / Sinh viên (Standard User)", "Người dùng học tập, làm bài tập số học hàng ngày.", "Thao tác phím bấm nhanh, tính toán cơ bản chính xác, hỗ trợ phím cứng bàn phím, lưu nhật ký phép tính."),
    ("2. Kế toán / Giảng viên (Advanced User)", "Người dùng chuyên môn tính toán số thực, phần trăm và bộ nhớ.", "Cần chức năng bộ nhớ tạm (MS, MR, M+, M-), tính phần trăm chính xác, độ chuẩn xác số thực cao không bị sai lệch số học."),
    ("3. Chuyên viên QA / Tester (Inspector)", "Người kiểm thử phần mềm đánh giá chất lượng và tìm kiếm lỗi.", "Cần giao diện trực quan, bảng tra cứu danh mục lỗi, khả năng tái hiện lỗi nhanh chóng để đối chiếu với tài liệu đặc tả.")
]:
    row = t_roles.add_row().cells
    style_body_cell(row[0], r[0], bold=True)
    style_body_cell(row[1], r[1])
    style_body_cell(row[2], r[2])

doc.add_heading("1.2. Các luồng nghiệp vụ người dùng (>= 3 luồng)", level=2)
doc_urd_p = doc.add_paragraph(
    "- Luồng 1 (Tính toán cơ bản & Bộ nhớ): Nhập số A -> chọn toán tử (+, -, ×, ÷) -> nhập số B -> bấm '=' xem kết quả. Bấm 'MS' lưu bộ nhớ (sáng biểu tượng M), bấm 'C' xóa màn hình và bấm 'MR' gọi lại giá trị bộ nhớ.\n"
    "- Luồng 2 (Tính toán nâng cao): Nhập giá trị số -> bấm căn '√' hoặc bình phương 'x²' hệ thống phản hồi tức thì. Hoặc nhập phép tính 'A + B%' để tính phần trăm.\n"
    "- Luồng 3 (Quản lý lịch sử): Sau mỗi phép tính, hệ thống tự động ghi nhật ký bên phải. Người dùng có thể nhấp chuột vào một mục trong lịch sử để nạp lại số, hoặc bấm 'Xóa lịch sử' để giải phóng RAM."
)

doc.add_heading("1.3. User Stories & Tiêu chí nghiệm thu (Acceptance Criteria)", level=2)
t_us = doc.add_table(rows=1, cols=4)
hdr_us = t_us.rows[0].cells
style_header_cell(hdr_us[0], "Mã US")
style_header_cell(hdr_us[1], "Nội dung User Story (Là... Tôi muốn... Để...)")
style_header_cell(hdr_us[2], "Độ ưu tiên")
style_header_cell(hdr_us[3], "Tiêu chí nghiệm thu (Acceptance Criteria)")
for u in [
    ("US-01", "Là một Học sinh, tôi muốn nhập các chữ số và phép tính (+, -, ×, ÷) để nhận kết quả chính xác.", "High", "Nhận 0-9; tính đúng số nguyên và số thực; hiển thị kết quả tức thì khi nhấn '='."),
    ("US-02", "Là một Sinh viên, tôi muốn sử dụng bàn phím máy tính thật để nhập liệu nhanh.", "Medium", "Hỗ trợ phím 0-9, dấu chấm, +, -, *, /, Enter, Backspace, Escape."),
    ("US-03", "Là một Kế toán, tôi muốn lưu giá trị vào bộ nhớ (MS/MR/M+/M-) để cộng dồn khoản tiền.", "High", "MS lưu giá trị; MR gọi lại; M+ cộng thêm; M- trừ đi; có ký hiệu 'M' sáng."),
    ("US-04", "Là một Người dùng, tôi muốn xem lại nhật ký các phép tính đã làm.", "Medium", "Tự động ghi biểu thức và kết quả; nhấp chuột nạp lại số vào màn hình."),
    ("US-05", "Là một Người dùng, tôi muốn hệ thống báo lỗi rõ ràng khi chia cho 0 hoặc căn số âm.", "High", "Không hiển thị chuỗi Infinity hay NaN; đưa ra thông báo lỗi thân thiện."),
    ("US-06", "Là một Chuyên viên QA, tôi muốn có bảng kiểm tra lỗi trực quan để đối chiếu kiểm thử.", "Low", "Có bảng QA Inspector phân loại 5 nhóm; hỗ trợ nút tự động tái hiện lỗi.")
]:
    row = t_us.add_row().cells
    style_body_cell(row[0], u[0], bold=True, center=True)
    style_body_cell(row[1], u[1])
    style_body_cell(row[2], u[2], center=True)
    style_body_cell(row[3], u[3])

# --- PHẦN 2: SRS ---
doc.add_page_break()
doc.add_heading("PHẦN 2. ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS)", level=1)
doc.add_heading("2.1. Danh mục 14 Yêu cầu chức năng (FR)", level=2)
t_fr = doc.add_table(rows=1, cols=4)
hdr_fr = t_fr.rows[0].cells
style_header_cell(hdr_fr[0], "Mã FR")
style_header_cell(hdr_fr[1], "Tên chức năng")
style_header_cell(hdr_fr[2], "Đặc tả chi tiết & Ràng buộc dữ liệu cụ thể")
style_header_cell(hdr_fr[3], "Truy vết URD")
for f in [
    ("FR-01", "Trạng thái khởi tạo", "Màn hình khởi tạo hoặc sau khi bấm AC hiển thị giá trị mặc định là số '0'.", "US-01"),
    ("FR-02", "Nhập chữ số", "Nhận chữ số từ '0' đến '9'. Độ dài tối đa 16 chữ số trên màn hình.", "US-01"),
    ("FR-03", "Chặn số 0 vô nghĩa đầu", "Khi màn hình là '0', nhập chữ số khác thay thế hoàn toàn '0'; không cho phép chuỗi '0008'.", "US-01"),
    ("FR-04", "Dấu chấm thập phân", "Chỉ cho phép duy nhất một dấu '.' trong cùng một toán hạng. Bấm tiếp dấu '.' bị bỏ qua.", "US-01"),
    ("FR-05", "Giới hạn hiển thị", "Độ dài hiển thị tối đa 16 chữ số. Vượt quá tự co cỡ chữ hoặc chuyển định dạng e-notation.", "US-01"),
    ("FR-06", "Xóa ký tự Backspace", "Nút ⌫ xóa 1 ký tự cuối. Khi còn 1 ký tự, bấm ⌫ chuyển màn hình về '0' (không để rỗng '').", "US-01"),
    ("FR-07", "Độ chính xác số thực", "Các phép tính (+, -, ×, ÷) phải chuẩn hóa số thực theo IEEE-754, làm tròn tối đa 12 chữ số thập phân.", "US-01"),
    ("FR-08", "Thứ tự ưu tiên BODMAS", "Thực hiện nhân/chia trước, cộng/trừ sau. Biểu thức '2 + 3 × 4' phải cho kết quả là 14.", "US-01"),
    ("FR-09", "Phép chia cho số 0", "Khi mẫu số = 0 trong phép chia, hiển thị 'Cannot divide by 0' và khóa tính tiếp.", "US-05"),
    ("FR-10", "Thay thế toán tử liên tiếp", "Nếu bấm toán tử rồi đổi ý bấm toán tử khác, toán tử sau tự động thay thế toán tử trước.", "US-01"),
    ("FR-11", "Căn bậc hai (√)", "Tính √x. Với x >= 0 trả về kết quả; với x < 0 hiển thị thông báo lỗi 'Invalid Input'.", "US-05"),
    ("FR-12", "Bình phương (x²)", "Tính bình phương x * x của số đang hiển thị với thời gian phản hồi dưới 50ms.", "US-01"),
    ("FR-13", "Đổi dấu âm dương (±)", "Đảo dấu x thành -x. Nếu x = 0 thì giữ nguyên là '0', không được hiển thị '-0'.", "US-01"),
    ("FR-14", "Tính phần trăm (%)", "Quy tắc A + B% = A + (A * B / 100). Ví dụ: 100 + 10% = 110.", "US-03")
]:
    row = t_fr.add_row().cells
    style_body_cell(row[0], f[0], bold=True, center=True)
    style_body_cell(row[1], f[1], bold=True)
    style_body_cell(row[2], f[2])
    style_body_cell(row[3], f[3], center=True)

doc.add_heading("2.2. Đặc tả 3 Luồng nghiệp vụ hoàn chỉnh (Main / Alt / Exception)", level=2)
doc.add_paragraph(
    "Luồng 1: Phép chia hai số (Division)\n"
    "- Main Flow: Nhập số bị chia A -> bấm '÷' -> nhập số chia B (khác 0) -> bấm '=' -> hiển thị thương số A/B và lưu lịch sử.\n"
    "- Alternative Flow: Sau khi bấm '÷', người dùng đổi ý bấm '×', hệ thống tự động thay thế thành phép nhân.\n"
    "- Exception Flow: Nhập số chia B = 0 và bấm '=', hệ thống khóa tính tiếp và xuất thông báo: 'Cannot divide by 0'.\n\n"
    "Luồng 2: Thao tác bộ nhớ tạm (Memory)\n"
    "- Main Flow: Màn hình có số V -> bấm 'MS' (lưu V vào bộ nhớ, sáng chữ M) -> thực hiện phép tính khác -> bấm 'MR' (hiển thị lại V).\n"
    "- Alternative Flow: Bấm 'M+' hoặc 'M-' để cộng dồn hoặc trừ giá trị màn hình vào bộ nhớ.\n"
    "- Exception Flow: Người dùng bấm 'C' (Clear Entry), chỉ xóa màn hình về 0, giá trị bộ nhớ 'M' vẫn được bảo toàn nguyên vẹn.\n\n"
    "Luồng 3: Tính căn bậc hai (Square Root)\n"
    "- Main Flow: Nhập số dương 16 -> bấm '√' -> hiển thị kết quả 4.\n"
    "- Exception Flow: Nhập số âm -9 -> bấm '√' -> hệ thống chặn phép tính và xuất thông báo 'Invalid Input'."
)

doc.add_heading("2.3. Bảng quyết định (Decision Table)", level=2)
t_dt = doc.add_table(rows=1, cols=5)
hdr_dt = t_dt.rows[0].cells
style_header_cell(hdr_dt[0], "Điều kiện / Hành động")
style_header_cell(hdr_dt[1], "R1")
style_header_cell(hdr_dt[2], "R2")
style_header_cell(hdr_dt[3], "R3")
style_header_cell(hdr_dt[4], "R4")
for r in [
    ("Điều kiện: Toán tử là phép chia (÷)", "Đúng", "Đúng", "Sai", "Đúng"),
    ("Điều kiện: Số chia B bằng 0", "Sai", "Đúng", "-", "Sai"),
    ("Điều kiện: Số bị chia A là số âm", "-", "-", "-", "Đúng"),
    ("Hành động: Xuất kết quả thương số A/B", "X", "-", "X", "X"),
    ("Hành động: Báo lỗi 'Cannot divide by 0'", "-", "X", "-", "-"),
    ("Hành động: Ghi nhận vào lịch sử", "X", "-", "X", "X")
]:
    row = t_dt.add_row().cells
    style_body_cell(row[0], r[0], bold=True)
    style_body_cell(row[1], r[1], center=True)
    style_body_cell(row[2], r[2], center=True)
    style_body_cell(row[3], r[3], center=True)
    style_body_cell(row[4], r[4], center=True)

doc.add_heading("2.4. Danh mục 8 Yêu cầu phi chức năng (>= 3 NFR Hiệu năng)", level=2)
t_nfr = doc.add_table(rows=1, cols=4)
hdr_nfr = t_nfr.rows[0].cells
style_header_cell(hdr_nfr[0], "Mã NFR")
style_header_cell(hdr_nfr[1], "Nhóm yêu cầu")
style_header_cell(hdr_nfr[2], "Tiêu chuẩn kỹ thuật định lượng")
style_header_cell(hdr_nfr[3], "Phương pháp kiểm thử")
for n in [
    ("NFR-01", "Hiệu năng", "Thời gian phản hồi khi bấm phím số học phải < 50ms.", "Chrome Performance DevTools"),
    ("NFR-02", "Hiệu năng", "Hàm tính bình phương (x²) hoặc căn bậc hai (√) phải hoàn thành trong < 10ms, không treo Main Thread.", "Console timing"),
    ("NFR-03", "Hiệu năng", "Giải phóng bộ nhớ RAM: Khi xóa lịch sử, giải phóng mảng RAM về 0 bytes, không rò rỉ RAM.", "Memory Heap Snapshot"),
    ("NFR-04", "Tính ổn định", "Hệ thống không bị crash, đóng băng hoặc trắng màn hình khi nhận chuỗi ký tự bất thường.", "Error Guessing & Stress Test"),
    ("NFR-05", "Tương thích", "Hoạt động mượt mà 100% trên các trình duyệt: Chrome, Edge, Safari, Firefox.", "Cross-browser Testing"),
    ("NFR-06", "Trải nghiệm UI/UX", "Giao diện Dark Mode chuẩn WCAG 2.1 AA, tỉ lệ tương phản màu tối thiểu 4.5:1.", "Lighthouse Accessibility Audit"),
    ("NFR-07", "Hỗ trợ phím cứng", "Hỗ trợ 100% các phím cứng tiêu chuẩn của bàn phím vật lý (0-9, Enter, Esc, Backspace).", "Keyboard Event Testing"),
    ("NFR-08", "Toàn vẹn dữ liệu", "Không sử dụng hàm eval() nguy hiểm khi phân tích cú pháp biểu thức.", "Static Code Security Scan")
]:
    row = t_nfr.add_row().cells
    style_body_cell(row[0], n[0], bold=True, center=True)
    style_body_cell(row[1], n[1], bold=True)
    style_body_cell(row[2], n[2])
    style_body_cell(row[3], n[3])

# --- PHẦN 3: API & KIẾN TRÚC ---
doc.add_page_break()
doc.add_heading("PHẦN 3. ĐẶC TẢ HÀM VÀ API HỆ THỐNG", level=1)
doc.add_paragraph("Bảng tổng hợp đặc tả các hàm và API chức năng của hệ thống SmartCalc Pro:")
t_api = doc.add_table(rows=1, cols=4)
hdr_api = t_api.rows[0].cells
style_header_cell(hdr_api[0], "Hàm / Action")
style_header_cell(hdr_api[1], "Tham số")
style_header_cell(hdr_api[2], "Mô tả chức năng")
style_header_cell(hdr_api[3], "Kết quả trả về")
for a in [
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
    row = t_api.add_row().cells
    style_body_cell(row[0], a[0], bold=True)
    style_body_cell(row[1], a[1])
    style_body_cell(row[2], a[2])
    style_body_cell(row[3], a[3])

# --- PHẦN 4: TEST PLAN ---
doc.add_page_break()
doc.add_heading("PHẦN 4. KẾ HOẠCH KIỂM THỬ (TEST PLAN)", level=1)
doc.add_paragraph(
    "1. Mục tiêu: Kiểm tra toàn diện 14 yêu cầu chức năng (FR) và 8 yêu cầu phi chức năng (NFR).\n"
    "2. Chiến lược & Kỹ thuật:\n"
    "- Phân vùng tương đương (EP): Số dương, âm, số 0, số thực thập phân.\n"
    "- Phân tích giá trị biên (BVA): Ngưỡng 16 chữ số màn hình, chia cho 0.\n"
    "- Chuyển trạng thái (State Transition): Trạng thái bộ nhớ MS -> C -> MR.\n"
    "- Đoán lỗi (Error Guessing): Chuỗi toán tử liên tiếp, xóa rỗng xâu, vòng lặp nặng CPU.\n"
    "3. Môi trường kiểm thử: Google Chrome v120+, macOS Sonoma / Windows 11, độ phân giải Desktop & Mobile."
)

# --- PHẦN 5: TEST CASES ---
doc.add_page_break()
doc.add_heading("PHẦN 5. BỘ KỊCH BẢN KIỂM THỬ (TEST CASES)", level=1)
t_tc = doc.add_table(rows=1, cols=5)
hdr_tc = t_tc.rows[0].cells
style_header_cell(hdr_tc[0], "Mã TC")
style_header_cell(hdr_tc[1], "Module / Chức năng")
style_header_cell(hdr_tc[2], "Các bước thực hiện (Steps)")
style_header_cell(hdr_tc[3], "Kết quả kỳ vọng")
style_header_cell(hdr_tc[4], "Trạng thái")
for tc in [
    ("TC-01", "Cộng số nguyên", "1. Nhập 15 -> Bấm + -> Nhập 25 -> Bấm =", "Màn hình hiển thị 40", "PASS"),
    ("TC-02", "Cộng số thực", "1. Nhập 0.1 -> Bấm + -> Nhập 0.2 -> Bấm =", "Màn hình hiển thị chính xác 0.3", "FAIL (SEED-01)"),
    ("TC-03", "Dấu thập phân", "1. Nhập 5 -> Bấm . -> Nhập 2 -> Bấm . -> Nhập 3", "Chỉ nhận 1 dấu chấm (5.23)", "FAIL (SEED-02)"),
    ("TC-04", "Chia cho 0", "1. Nhập 9 -> Bấm ÷ -> Nhập 0 -> Bấm =", "Báo lỗi Cannot divide by 0", "FAIL (SEED-03)"),
    ("TC-05", "Thứ tự BODMAS", "1. Nhập 2 -> Bấm + -> Nhập 3 -> Bấm × -> Nhập 4 -> =", "Kết quả phải là 14", "FAIL (SEED-04)"),
    ("TC-06", "Căn bậc hai", "1. Nhập 16 -> Bấm √", "Hiển thị 4", "PASS"),
    ("TC-07", "Căn số âm", "1. Nhập 9 -> Bấm ± (-9) -> Bấm √", "Báo lỗi Invalid Input", "FAIL (SEED-05)"),
    ("TC-08", "Tràn màn hình", "1. Bấm phím 9 liên tục 25 lần", "Giới hạn 16 số hoặc co chữ e-notation", "FAIL (SEED-06)"),
    ("TC-09", "Đổi dấu số 0", "1. Màn hình là 0 -> Bấm ±", "Giữ nguyên là 0, căn lề chuẩn", "FAIL (SEED-07)"),
    ("TC-10", "Vỡ khung lịch sử", "1. Nhập 123456789 + 987654321 =", "Bẻ dòng gọn gàng, không vỡ khung", "FAIL (SEED-08)"),
    ("TC-11", "Số 0 đầu", "1. Bấm 0 ba lần -> Bấm 8", "Chuẩn hóa thành 8", "FAIL (SEED-09)"),
    ("TC-12", "Phần trăm", "1. Nhập 100 -> Bấm + -> Nhập 10 -> Bấm % -> =", "Kết quả phải bằng 110", "FAIL (SEED-10)"),
    ("TC-13", "Tooltip nút C", "1. Rê chuột lên nút C", "Tooltip: Clear Entry", "FAIL (SEED-11)"),
    ("TC-14", "Đơ lag CPU", "1. Nhập 5 -> Bấm x²", "Hiển thị 25 ngay tức thì (< 50ms)", "FAIL (SEED-12: Treo > 3s)"),
    ("TC-15", "Rò rỉ RAM", "1. Tính 1+1=2 -> Bấm Xóa lịch sử -> Tính 2+2=4", "Lịch sử chỉ chứa duy nhất 2+2=4", "FAIL (SEED-13: Rò rỉ RAM)"),
    ("TC-16", "Sập ứng dụng", "1. Bấm ⌫ xóa sạch -> Bấm + =", "Về 0, không ném lỗi", "FAIL (SEED-14: Crash ứng dụng)"),
    ("TC-17", "Trắng màn hình", "1. Bấm 8 -> Bấm ÷ -> Bấm × -> Bấm =", "Báo lỗi cú pháp nhẹ nhàng", "FAIL (SEED-15: White Screen)"),
    ("TC-18", "Bộ nhớ M-", "1. Lưu 100 vào MS -> Nhập 30 -> Bấm M- -> Bấm MR", "MR hiển thị 70", "FAIL (SEED-16: Tính nhầm thành cộng)"),
    ("TC-19", "Phép trừ âm", "1. Nhập 10 - 25 =", "Hiển thị -15", "PASS"),
    ("TC-20", "Phím AC", "1. Nhập 9999 -> Bấm AC", "Màn hình về 0, reset mọi thứ", "PASS")
]:
    row = t_tc.add_row().cells
    style_body_cell(row[0], tc[0], bold=True, center=True)
    style_body_cell(row[1], tc[1], bold=True)
    style_body_cell(row[2], tc[2])
    style_body_cell(row[3], tc[3])
    style_body_cell(row[4], tc[4], center=True)

# --- PHẦN 6: REVIEW & TSR ---
doc.add_page_break()
doc.add_heading("PHẦN 6. PHIẾU REVIEW SRS & BÁO CÁO TỔNG KẾT KIỂM THỬ (TSR)", level=1)
doc.add_heading("6.1. Phiếu Review tài liệu đặc tả SRS (Tiêu chí B1: 0,5 điểm)", level=2)
doc.add_paragraph(
    "- Người review (Tester): Phạm Văn Quang (MSSV: 23110342)\n"
    "- Đánh giá: Tài liệu SRS đã được bổ sung đầy đủ các ràng buộc số học cụ thể (làm tròn số thực toFixed(12), chặn 2 dấu chấm, khóa tính tiếp khi chia cho 0, tiêu chuẩn phản hồi < 50ms). Đạt yêu cầu kiểm thử được."
)

doc.add_heading("6.2. Báo cáo tổng kết kiểm thử (Test Summary Report)", level=2)
doc.add_paragraph(
    "- Tổng số Test Cases: 20 kịch bản.\n"
    "- Số Test Cases Passed: 4 kịch bản (20%).\n"
    "- Số Test Cases Failed: 16 kịch bản (80%).\n"
    "- Thống kê lỗi phát hiện: 16 lỗi, chia chuẩn theo đúng 5 nhóm của Đề bài:\n"
    "  + 1. Functional: 5 lỗi (SEED-01, SEED-02, SEED-03, SEED-04, SEED-05)\n"
    "  + 2. Visual: 3 lỗi (SEED-06, SEED-07, SEED-08)\n"
    "  + 3. Content: 3 lỗi (SEED-09, SEED-10, SEED-11)\n"
    "  + 4. Performance: 2 lỗi (SEED-12 đơ lag > 3s, SEED-13 rò rỉ RAM)\n"
    "  + 5. Crash: 3 lỗi (SEED-14 sập xóa rỗng, SEED-15 trắng màn hình, SEED-16 logic M-)\n"
    "  + Có 4 lỗi Critical và 6 lỗi Major. Đạt và vượt chỉ tiêu tối thiểu của môn học."
)

# --- PHẦN 7: BIÊN BẢN & CHECKLIST ---
doc.add_page_break()
doc.add_heading("PHẦN 7. BIÊN BẢN BÀN GIAO & CHECKLIST RÀ SOÁT", level=1)
doc.add_paragraph(
    "1. Biên bản bàn giao:\n"
    "- Sinh viên bàn giao trọn bộ mã nguồn Web: https://github.com/QUANGPV021/calculator-qa-testing\n"
    "- Website thực thi trực tuyến: https://quangpv021.github.io/calculator-qa-testing/\n"
    "- File báo cáo tổng hợp tài liệu (file này) và File danh mục lỗi cài sẵn Bug Manifest.\n\n"
    "2. Checklist kiểm tra trước khi nộp:\n"
    "[x] Khai báo Domain Website tại mục About của Repository GitHub.\n"
    "[x] Hoàn thiện đầy đủ URD, SRS, API, Test Plan, Test Cases, TSR.\n"
    "[x] Cài cắm đủ 16 lỗi chuẩn 5 nhóm (10 trong đặc tả, 6 ngoài đặc tả).\n"
    "[x] Đóng gói thành đúng 2 file chuẩn mực trên Google Drive."
)

file_doc_path = os.path.join(output_dir, "TAI_LIEU_DU_AN_CSE3066_23110342.docx")
doc.save(file_doc_path)
print(f"Done File 1: {file_doc_path}")

# -------------------------------------------------------------
# 2. FILE THỨ HAI: BUG_MANIFEST_CSE3066_23110342.xlsx
# -------------------------------------------------------------
src_bug_file = os.path.join(project_dir, "NOP_BAI_DRIVE", "Mau_02_Bug_Manifest.xlsx")
dst_bug_file = os.path.join(output_dir, "BUG_MANIFEST_CSE3066_23110342.xlsx")
shutil.copy2(src_bug_file, dst_bug_file)
print(f"Done File 2: {dst_bug_file}")
