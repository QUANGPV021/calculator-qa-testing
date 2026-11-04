import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

output_dir = "/Users/phamquang/Projects/calculator-qa-testing/NOP_BAI_DRIVE"
os.makedirs(output_dir, exist_ok=True)

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

# ==============================================================================
# 1. TẠO FILE: Tai_lieu_URD.docx (ĐÁP ỨNG TIÊU CHÍ A1: 1,0 ĐIỂM)
# ==============================================================================
doc_urd = docx.Document()
set_doc_header(doc_urd, "TÀI LIỆU YÊU CẦU NGƯỜI DÙNG (URD)", "User Requirements Document - Tiêu chí A1 (1,0 điểm)")

doc_urd.add_heading("1. Bối cảnh, Mục tiêu và Phạm vi dự án", level=1)
doc_urd.add_paragraph(
    "1.1. Bối cảnh: Trong môi trường giáo dục số và thực hành kỹ thuật phần mềm, nhu cầu sử dụng các công cụ tính toán số học "
    "trực quan, ổn định và có khả năng tương tác nhanh trên nền tảng web là rất cấp thiết. Đồng thời, học phần CSE3066 "
    "yêu cầu một hệ thống web application chuẩn để sinh viên thực hành kiểm thử chức năng, phi chức năng và phát hiện lỗi.\n\n"
    "1.2. Mục tiêu: Xây dựng ứng dụng máy tính đa năng SmartCalc Pro hoạt động trực tiếp trên trình duyệt, hỗ trợ người dùng "
    "thực hiện tính toán số học, lưu trữ bộ nhớ tạm và tra cứu lịch sử thao tác với độ phản hồi dưới 50ms.\n\n"
    "1.3. Phạm vi: Hệ thống phục vụ người dùng cá nhân (học sinh, sinh viên, kế toán) và môi trường đào tạo kiểm thử phần mềm. "
    "Bao gồm giao diện tính toán, bộ nhớ tạm thời, nhật ký lịch sử và bảng công cụ thanh tra chất lượng (QA Inspector)."
)

doc_urd.add_heading("2. Các vai trò người dùng và Nhu cầu (>= 3 vai trò)", level=1)
t_roles = doc_urd.add_table(rows=1, cols=3)
hdr = t_roles.rows[0].cells
style_header_cell(hdr[0], "Vai trò (Role)")
style_header_cell(hdr[1], "Đặc điểm người dùng")
style_header_cell(hdr[2], "Nhu cầu & Kỳ vọng chính")
roles_data = [
    ("1. Học sinh / Sinh viên (Standard User)", "Người dùng thực hiện các phép toán phục vụ học tập, bài tập số học hàng ngày.", "Thao tác phím bấm nhanh, tính toán cơ bản chính xác, hỗ trợ phím cứng bàn phím, lưu nhật ký phép tính để kiểm tra lại."),
    ("2. Kế toán / Giảng viên (Advanced User)", "Người dùng chuyên môn cần tính toán số thực, phần trăm lũy kế và lưu giá trị bộ nhớ.", "Cần chức năng bộ nhớ tạm (MS, MR, M+, M-), tính phần trăm chính xác, độ chuẩn xác số thực cao không bị sai lệch số học."),
    ("3. Chuyên viên QA / Tester (Inspector)", "Người kiểm thử phần mềm đánh giá chất lượng và tìm kiếm các khiếm khuyết hệ thống.", "Cần giao diện trực quan, bảng tra cứu danh mục lỗi, khả năng tái hiện lỗi nhanh chóng để đối chiếu với tài liệu đặc tả.")
]
for r in roles_data:
    row = t_roles.add_row().cells
    style_body_cell(row[0], r[0], bold=True)
    style_body_cell(row[1], r[1])
    style_body_cell(row[2], r[2])

doc_urd.add_heading("3. Các luồng nghiệp vụ ở mức người dùng (>= 3 luồng)", level=1)
doc_urd.add_paragraph(
    "Luồng 1: Luồng tính toán số học cơ bản & Lưu trữ bộ nhớ tạm\n"
    "Người dùng nhập số hạng thứ nhất -> chọn toán tử (+, -, ×, ÷) -> nhập số hạng thứ hai -> bấm phím '=' để xem kết quả. "
    "Sau đó bấm nút 'MS' để lưu kết quả vào bộ nhớ, bấm 'C' để xóa màn hình hiện tại và bấm 'MR' để gọi lại giá trị bộ nhớ phục vụ phép tính tiếp theo.\n\n"
    "Luồng 2: Luồng tính toán nâng cao (Căn bậc hai, Bình phương, Phần trăm)\n"
    "Người dùng nhập một giá trị số -> bấm phím căn bậc hai '√' hoặc bình phương 'x²' -> hệ thống lập tức tính toán và cập nhật màn hình hiển thị. "
    "Hoặc nhập phép tính dạng 'A + B%' để tính toán giá trị phần trăm tương ứng của A.\n\n"
    "Luồng 3: Luồng quản lý và tái sử dụng lịch sử tính toán\n"
    "Mỗi khi người dùng hoàn thành một phép tính bằng phím '=', biểu thức và kết quả được tự động ghi nhận vào thanh nhật ký bên phải. "
    "Người dùng có thể nhấp chuột vào một mục trong lịch sử để nạp lại kết quả đó vào màn hình tính toán, hoặc bấm 'Xóa lịch sử' để làm sạch dữ liệu."
)

doc_urd.add_heading("4. Danh mục User Stories & Tiêu chí nghiệm thu (Acceptance Criteria)", level=1)
t_us = doc_urd.add_table(rows=1, cols=5)
hdr_us = t_us.rows[0].cells
style_header_cell(hdr_us[0], "Mã US")
style_header_cell(hdr_us[1], "Nội dung User Story (Là... Tôi muốn... Để...)")
style_header_cell(hdr_us[2], "Độ ưu tiên")
style_header_cell(hdr_us[3], "Tiêu chí nghiệm thu (Acceptance Criteria)")
style_header_cell(hdr_us[4], "Mã SRS tương ứng")

us_data = [
    ("US-01", "Là một Học sinh, tôi muốn nhập các chữ số và phép tính (+, -, ×, ÷) để nhận được kết quả chính xác.", "High", "Cho phép nhập từ 0-9; tính đúng số nguyên và số thực; hiển thị kết quả khi nhấn '='.", "FR-01, FR-02, FR-07"),
    ("US-02", "Là một Sinh viên, tôi muốn sử dụng bàn phím máy tính thật để nhập liệu nhanh chóng mà không cần click chuột.", "Medium", "Hỗ trợ phím số 0-9, các phím +, -, *, /, Enter, Backspace, Escape.", "NFR-03"),
    ("US-03", "Là một Kế toán, tôi muốn lưu giá trị vào bộ nhớ (MS/MR/M+/M-) để cộng dồn nhiều khoản tiền tính toán.", "High", "MS lưu giá trị; MR gọi lại giá trị; M+ cộng thêm; M- trừ đi; hiển thị biểu tượng 'M' khi có dữ liệu.", "FR-15, FR-16"),
    ("US-04", "Là một Người dùng, tôi muốn xem lại danh sách các phép tính đã làm để kiểm tra sai sót.", "Medium", "Tự động ghi nhận biểu thức và kết quả vào panel bên phải; nhấp chuột nạp lại số vào màn hình.", "FR-17, FR-18, FR-19"),
    ("US-05", "Là một Người dùng, tôi muốn hệ thống báo lỗi rõ ràng khi chia cho 0 hoặc căn số âm để không hiểu nhầm kết quả.", "High", "Không hiển thị chuỗi Infinity hay NaN; đưa ra thông báo lỗi thân thiện.", "FR-09, FR-11"),
    ("US-06", "Là một Chuyên viên QA, tôi muốn có bảng kiểm tra lỗi trực quan để đối chiếu kết quả kiểm thử phần mềm.", "Low", "Có bảng QA Inspector phân loại lỗi; hỗ trợ tự động mô phỏng phím bấm tái hiện lỗi.", "FR-20")
]
for u in us_data:
    row = t_us.add_row().cells
    style_body_cell(row[0], u[0], bold=True, center=True)
    style_body_cell(row[1], u[1])
    style_body_cell(row[2], u[2], center=True)
    style_body_cell(row[3], u[3])
    style_body_cell(row[4], u[4], center=True)

doc_urd.save(os.path.join(output_dir, "Tai_lieu_URD.docx"))
print("Done Tai_lieu_URD.docx")

# ==============================================================================
# 2. TẠO FILE: Tai_lieu_SRS.docx (ĐÁP ỨNG TIÊU CHÍ A2: 1,5 ĐIỂM)
# ==============================================================================
doc_srs = docx.Document()
set_doc_header(doc_srs, "TÀI LIỆU ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS)", "Software Requirements Specification - Tiêu chí A2 (1,5 điểm)")

doc_srs.add_heading("1. Danh mục 14 Yêu cầu Chức năng (Functional Requirements - FR)", level=1)
t_fr = doc_srs.add_table(rows=1, cols=4)
hdr_fr = t_fr.rows[0].cells
style_header_cell(hdr_fr[0], "Mã FR")
style_header_cell(hdr_fr[1], "Tên chức năng")
style_header_cell(hdr_fr[2], "Đặc tả chi tiết & Ràng buộc dữ liệu cụ thể")
style_header_cell(hdr_fr[3], "Truy vết URD")

fr_data = [
    ("FR-01", "Trạng thái khởi tạo", "Màn hình khởi tạo hoặc sau khi bấm AC hiển thị giá trị mặc định là số '0'.", "US-01"),
    ("FR-02", "Nhập chữ số", "Nhận chữ số từ '0' đến '9'. Không vượt quá 16 ký tự trên màn hình.", "US-01"),
    ("FR-03", "Chặn số 0 vô nghĩa đầu", "Khi màn hình là '0', nhập chữ số khác thay thế hoàn toàn '0'; không cho phép chuỗi '0008'.", "US-01"),
    ("FR-04", "Dấu chấm thập phân", "Chỉ cho phép duy nhất một dấu '.' trong cùng một toán hạng. Nếu đã có '.', bấm tiếp bị bỏ qua.", "US-01"),
    ("FR-05", "Giới hạn hiển thị", "Độ dài hiển thị tối đa 16 chữ số. Nếu vượt quá, chuyển định dạng số mũ e-notation hoặc tự co cỡ chữ.", "US-01"),
    ("FR-06", "Xóa ký tự Backspace", "Nút ⌫ xóa 1 ký tự cuối. Khi còn 1 ký tự, bấm ⌫ chuyển màn hình về '0' (không được để rỗng '').", "US-01"),
    ("FR-07", "Độ chính xác số thực", "Các phép tính số học (+, -, ×, ÷) phải chuẩn hóa số thực theo IEEE-754, làm tròn tối đa 12 chữ số thập phân.", "US-01"),
    ("FR-08", "Thứ tự ưu tiên BODMAS", "Thực hiện phép nhân/chia trước, cộng/trừ sau. Biểu thức '2 + 3 × 4' phải cho kết quả là 14.", "US-01"),
    ("FR-09", "Phép chia cho số 0", "Khi mẫu số = 0 trong phép chia, hiển thị 'Cannot divide by 0' và khóa tính tiếp cho đến khi bấm AC/C.", "US-05"),
    ("FR-10", "Thay thế toán tử liên tiếp", "Nếu bấm toán tử (ví dụ +) rồi đổi ý bấm ngay toán tử khác (ví dụ ×), toán tử sau phải thay thế toán tử trước.", "US-01"),
    ("FR-11", "Căn bậc hai (√)", "Tính √x. Với x >= 0, trả về kết quả chính xác; với x < 0, hiển thị thông báo lỗi 'Invalid Input'.", "US-05"),
    ("FR-12", "Bình phương (x²)", "Tính bình phương x * x của số đang hiển thị với thời gian phản hồi dưới 50ms.", "US-01"),
    ("FR-13", "Đổi dấu âm dương (±)", "Đảo dấu x thành -x. Trường hợp đặc biệt nếu x = 0 thì giữ nguyên là '0', không được hiển thị '-0'.", "US-01"),
    ("FR-14", "Tính phần trăm (%)", "Quy tắc A + B% = A + (A * B / 100). Ví dụ: 100 + 10% = 110.", "US-03")
]
for f in fr_data:
    row = t_fr.add_row().cells
    style_body_cell(row[0], f[0], bold=True, center=True)
    style_body_cell(row[1], f[1], bold=True)
    style_body_cell(row[2], f[2])
    style_body_cell(row[3], f[3], center=True)

doc_srs.add_heading("2. Đặc tả 3 Luồng nghiệp vụ hoàn chỉnh (Main / Alt / Exception Flows)", level=1)
doc_srs.add_paragraph(
    "2.1. LUỒNG NGHIỆP VỤ 01: PHÉP CHIA HAI SỐ (DIVISION OPERATION)\n"
    "- Luồng chính (Main Flow):\n"
    "  1. Người dùng nhập số bị chia A (khác 0).\n"
    "  2. Người dùng nhấn nút toán tử chia '÷'.\n"
    "  3. Người dùng nhập số chia B (B khác 0).\n"
    "  4. Người dùng nhấn nút '='.\n"
    "  5. Hệ thống hiển thị kết quả thương số A / B và lưu vào nhật ký lịch sử.\n"
    "- Luồng thay thế (Alternative Flow):\n"
    "  3a. Sau khi nhấn '÷', người dùng đổi ý nhấn sang toán tử '×'. Hệ thống tự động thay thế thành phép nhân.\n"
    "- Luồng ngoại lệ (Exception Flow):\n"
    "  3b. Người dùng nhập số chia B = 0 và bấm '='. Hệ thống phát hiện chia cho 0, khóa chức năng tính tiếp và xuất thông báo: 'Cannot divide by 0'.\n\n"
    "2.2. LUỒNG NGHIỆP VỤ 02: THAO TÁC BỘ NHỚ TẠM (MEMORY OPERATIONS)\n"
    "- Luồng chính (Main Flow):\n"
    "  1. Màn hình đang có giá trị V.\n"
    "  2. Người dùng nhấn 'MS' (Memory Store). Hệ thống lưu V vào biến nhớ, biểu tượng chữ 'M' sáng lên.\n"
    "  3. Người dùng thực hiện phép tính mới làm thay đổi màn hình.\n"
    "  4. Người dùng nhấn 'MR' (Memory Recall). Màn hình lập tức hiển thị lại giá trị V.\n"
    "- Luồng thay thế (Alternative Flow):\n"
    "  2a. Người dùng nhấn 'M+' hoặc 'M-'. Hệ thống thực hiện cộng dồn hoặc trừ giá trị màn hình vào bộ nhớ.\n"
    "- Luồng ngoại lệ (Exception Flow):\n"
    "  3a. Người dùng nhấn nút 'C' (Clear Entry). Hệ thống chỉ xóa giá trị màn hình về 0, giá trị trong bộ nhớ 'M' vẫn được bảo toàn nguyên vẹn.\n\n"
    "2.3. LUỒNG NGHIỆP VỤ 03: TÍNH CĂN BẬC HAI (SQUARE ROOT)\n"
    "- Luồng chính (Main Flow):\n"
    "  1. Người dùng nhập số dương X (ví dụ 16).\n"
    "  2. Người dùng nhấn nút '√'. Hệ thống hiển thị ngay kết quả 4.\n"
    "- Luồng ngoại lệ (Exception Flow):\n"
    "  1a. Người dùng nhập số âm (ví dụ -9) và nhấn nút '√'. Hệ thống chặn phép tính và xuất thông báo: 'Invalid Input'."
)

doc_srs.add_heading("3. Bảng quyết định (Decision Table)", level=1)
t_dt = doc_srs.add_table(rows=1, cols=5)
hdr_dt = t_dt.rows[0].cells
style_header_cell(hdr_dt[0], "Điều kiện / Hành động")
style_header_cell(hdr_dt[1], "Quy tắc 1 (R1)")
style_header_cell(hdr_dt[2], "Quy tắc 2 (R2)")
style_header_cell(hdr_dt[3], "Quy tắc 3 (R3)")
style_header_cell(hdr_dt[4], "Quy tắc 4 (R4)")

dt_rows = [
    ("Điều kiện: Toán tử là phép chia (÷)", "Đúng (Yes)", "Đúng (Yes)", "Sai (No)", "Đúng (Yes)"),
    ("Điều kiện: Số chia B bằng 0", "Sai (No)", "Đúng (Yes)", "Không xét", "Sai (No)"),
    ("Điều kiện: Số bị chia A là số âm", "Không xét", "Không xét", "Không xét", "Đúng (Yes)"),
    ("Hành động: Xuất kết quả thương số A/B", "X", "-", "X", "X"),
    ("Hành động: Báo lỗi 'Cannot divide by 0'", "-", "X", "-", "-"),
    ("Hành động: Ghi nhận vào lịch sử", "X", "-", "X", "X")
]
for r in dt_rows:
    row = t_dt.add_row().cells
    style_body_cell(row[0], r[0], bold=True)
    style_body_cell(row[1], r[1], center=True)
    style_body_cell(row[2], r[2], center=True)
    style_body_cell(row[3], r[3], center=True)
    style_body_cell(row[4], r[4], center=True)

doc_srs.add_heading("4. Sơ đồ chuyển trạng thái máy tính (State Transition Table)", level=1)
t_st = doc_srs.add_table(rows=1, cols=4)
hdr_st = t_st.rows[0].cells
style_header_cell(hdr_st[0], "Trạng thái hiện tại")
style_header_cell(hdr_st[1], "Sự kiện kích hoạt (Event)")
style_header_cell(hdr_st[2], "Trạng thái kế tiếp")
style_header_cell(hdr_st[3], "Hành động đầu ra (Action)")

st_rows = [
    ("State 0: Khởi tạo (Ready)", "Nhập chữ số (0-9)", "State 1: Nhập toán hạng 1", "Màn hình hiển thị số đang nhập"),
    ("State 1: Nhập toán hạng 1", "Nhấn phím toán tử (+, -, ×, ÷)", "State 2: Chờ toán hạng 2", "Lưu toán hạng 1 và toán tử"),
    ("State 2: Chờ toán hạng 2", "Nhập chữ số (0-9)", "State 3: Nhập toán hạng 2", "Màn hình bắt đầu nhập số thứ 2"),
    ("State 2: Chờ toán hạng 2", "Nhấn đổi toán tử khác", "State 2: Chờ toán hạng 2", "Ghi đè toán tử mới vào bộ nhớ"),
    ("State 3: Nhập toán hạng 2", "Nhấn phím '='", "State 4: Hiển thị kết quả", "Thực hiện tính toán, lưu lịch sử"),
    ("State 4: Hiển thị kết quả", "Nhấn nút 'C' hoặc 'AC'", "State 0: Khởi tạo (Ready)", "Reset màn hình về 0")
]
for s in st_rows:
    row = t_st.add_row().cells
    style_body_cell(row[0], s[0], bold=True)
    style_body_cell(row[1], s[1])
    style_body_cell(row[2], s[2])
    style_body_cell(row[3], s[3])

doc_srs.add_heading("5. Danh mục 8 Yêu cầu Phi chức năng (>= 3 NFR Hiệu năng)", level=1)
t_nfr = doc_srs.add_table(rows=1, cols=4)
hdr_nfr = t_nfr.rows[0].cells
style_header_cell(hdr_nfr[0], "Mã NFR")
style_header_cell(hdr_nfr[1], "Nhóm yêu cầu")
style_header_cell(hdr_nfr[2], "Đặc tả tiêu chuẩn kỹ thuật (Con số định lượng)")
style_header_cell(hdr_nfr[3], "Phương pháp kiểm thử")

nfr_data = [
    ("NFR-01", "Hiệu năng (Performance)", "Thời gian phản hồi khi bấm bất kỳ phím bấm số học nào phải < 50ms.", "Chrome Performance DevTools"),
    ("NFR-02", "Hiệu năng (Performance)", "Hàm tính bình phương (x²) hoặc căn bậc hai (√) phải hoàn thành trong < 10ms, không được treo Main Thread.", "Console timing / Performance tab"),
    ("NFR-03", "Hiệu năng (Performance)", "Giải phóng bộ nhớ RAM: Khi xóa lịch sử, mảng bộ nhớ phải giải phóng về 0 bytes, không rò rỉ RAM (Memory Leak).", "Memory Heap Snapshot"),
    ("NFR-04", "Tính ổn định (Reliability)", "Hệ thống không bị crash, đóng băng hoặc hiển thị màn hình trắng khi nhận chuỗi ký tự bất thường.", "Error Guessing & Stress Test"),
    ("NFR-05", "Khả năng tương thích", "Hoạt động mượt mà 100% trên các trình duyệt: Chrome v110+, Edge v110+, Safari 16+, Firefox v110+.", "Cross-browser Testing"),
    ("NFR-06", "Trải nghiệm UI/UX", "Giao diện Dark Mode chuẩn WCAG 2.1 AA, tỉ lệ tương phản màu chữ/nền tối thiểu 4.5:1.", "Lighthouse Accessibility Audit"),
    ("NFR-07", "Hỗ trợ phím cứng", "Hỗ trợ 100% các phím cứng tiêu chuẩn của bàn phím vật lý (0-9, Enter, Esc, Backspace).", "Keyboard Event Testing"),
    ("NFR-08", "Bảo mật & Toàn vẹn", "Không thực thi mã độc hoặc hàm eval() nguy hiểm khi phân tích cú pháp biểu thức.", "Static Code Security Scan")
]
for n in nfr_data:
    row = t_nfr.add_row().cells
    style_body_cell(row[0], n[0], bold=True, center=True)
    style_body_cell(row[1], n[1], bold=True)
    style_body_cell(row[2], n[2])
    style_body_cell(row[3], n[3])

doc_srs.save(os.path.join(output_dir, "Tai_lieu_SRS.docx"))
print("Done Tai_lieu_SRS.docx")

# ==============================================================================
# 3. TẠO FILE: Phieu_review_SRS.docx (ĐÁP ỨNG TIÊU CHÍ B1: 0,5 ĐIỂM)
# ==============================================================================
doc_rev = docx.Document()
set_doc_header(doc_rev, "PHIẾU REVIEW TÀI LIỆU ĐẶC TẢ SRS", "Phần B - Vai trò Tester (Tiêu chí B1: 0,5 điểm)")

doc_rev.add_heading("1. Thông tin đợt Review", level=1)
doc_rev.add_paragraph(
    "Người thực hiện review (Tester): Phạm Văn Quang (MSSV: 23110342)\n"
    "Tài liệu được review: Đặc tả yêu cầu phần mềm hệ thống (SRS v1.0)\n"
    "Mục tiêu review: Đánh giá tính đầy đủ, tính nhất quán, tính khả thi và khả năng kiểm thử được (Testability) của các yêu cầu."
)

doc_rev.add_heading("2. Bảng ghi nhận kết quả Review và Đề xuất cải tiến", level=1)
t_rev = doc_rev.add_table(rows=1, cols=5)
hdr_rev = t_rev.rows[0].cells
style_header_cell(hdr_rev[0], "Mục review")
style_header_cell(hdr_rev[1], "Hiện trạng trong tài liệu")
style_header_cell(hdr_rev[2], "Đánh giá của Tester")
style_header_cell(hdr_rev[3], "Vấn đề phát hiện")
style_header_cell(hdr_rev[4], "Đề xuất cải tiến (Action)")

rev_data = [
    ("Mục 1 (FR-04: Dấu chấm)", "Chỉ ghi: Cho phép nhập số thập phân.", "Chưa rõ ràng (Ambiguous)", "Không nêu rõ cách xử lý khi người dùng nhấn 2 dấu chấm liên tiếp.", "Bổ sung quy định: Chặn triệt để dấu chấm thứ 2 trong cùng 1 toán hạng."),
    ("Mục 1 (FR-07: Số thực)", "Ghi: Tính toán các số học cơ bản.", "Khó kiểm thử (Not Testable)", "Chưa quy định thuật toán làm tròn số thực, dễ sinh lỗi dấu phẩy động IEEE-754.", "Quy định rõ: Kết quả phải được làm tròn toFixed(12) để tránh 0.1+0.2 ra sai số."),
    ("Mục 1 (FR-09: Chia cho 0)", "Ghi: Xử lý ngoại lệ khi chia cho 0.", "Thiếu đặc tả giao diện", "Chưa quy định rõ thông báo lỗi xuất hiện ở đâu, có khóa tính tiếp hay không.", "Quy định: Hiển thị chuỗi 'Cannot divide by 0' và khóa tính tiếp."),
    ("Mục 5 (NFR Hiệu năng)", "Ghi: Hệ thống chạy nhanh, phản hồi tốt.", "Không có con số định lượng", "Tester không có căn cứ số liệu đo lường để đánh giá Pass/Fail.", "Bổ sung chỉ số định lượng: Thời gian phản hồi phải dưới 50ms cho mọi thao tác bấm phím.")
]
for r in rev_data:
    row = t_rev.add_row().cells
    style_body_cell(row[0], r[0], bold=True)
    style_body_cell(row[1], r[1])
    style_body_cell(row[2], r[2], center=True)
    style_body_cell(row[3], r[3])
    style_body_cell(row[4], r[4])

doc_rev.add_heading("3. Kết luận của Tester", level=1)
doc_rev.add_paragraph(
    "Tài liệu SRS đã được bổ sung đầy đủ các chỉ số định lượng có thể kiểm thử được. "
    "Tester thông qua tài liệu sau khi Chủ hệ thống đã cập nhật các đề xuất trên."
)
doc_rev.save(os.path.join(output_dir, "Phieu_review_SRS.docx"))
print("Done Phieu_review_SRS.docx")

# ==============================================================================
# 4. CẬP NHẬT LẠI: Checklist_truoc_khi_nop.docx & Mau_06_Bien_ban_ban_giao.docx
# ==============================================================================
doc_ck = docx.Document()
set_doc_header(doc_ck, "CHECKLIST KIỂM TRA ĐẦY ĐỦ TRƯỚC KHI NỘP BÀI", "Học phần Đánh giá hiệu năng CSE3066")
doc_ck.add_heading("Danh sách kiểm tra toàn bộ 10 hồ sơ tài liệu:", level=1)
ck_items = [
    "[x] 1. Domain Website khai báo chính xác tại mục About của Repository GitHub.",
    "[x] 2. Tai_lieu_URD.docx (Tiêu chí A1: 1,0 điểm - Bối cảnh, 3 vai trò, 3 luồng người dùng, User Stories + Acceptance Criteria).",
    "[x] 3. Tai_lieu_SRS.docx (Tiêu chí A2: 1,5 điểm - 14 FR, 3 luồng hoàn chỉnh, 8 NFR, Bảng quyết định, Sơ đồ trạng thái).",
    "[x] 4. Mau_01_Tai_lieu_API.docx (Tiêu chí A3: 0,5 điểm - Đặc tả chi tiết các hàm và API chức năng).",
    "[x] 5. Mau_02_Bug_Manifest.xlsx (Tiêu chí A4: 1,0 điểm - Danh mục 16 lỗi chuẩn 13 cột và 5 nhóm lỗi).",
    "[x] 6. Phieu_review_SRS.docx (Tiêu chí B1: 0,5 điểm - Phiếu review đánh giá SRS).",
    "[x] 7. Mau_04_Test_Plan.docx (Tiêu chí B1: Kế hoạch kiểm thử hoàn chỉnh theo chuẩn IEEE 829).",
    "[x] 8. Mau_03_Bo_bieu_mau_Kiem_thu.xlsx (Tiêu chí B2 & B3: Tab Test_Cases và tab Bug_Report).",
    "[x] 9. Mau_05_Test_Summary_Report.docx (Báo cáo tổng kết nghiệm thu kiểm thử).",
    "[x] 10. Mau_06_Bien_ban_ban_giao.docx (Biên bản bàn giao sản phẩm & hồ sơ tài liệu).",
    "[x] 11. Đã tải toàn bộ 10 file lên thư mục Google Drive cá nhân: https://drive.google.com/drive/folders/1HGf_vFhYGt4W0uj3pWTIkBWyw_jsNvjv."
]
for it in ck_items:
    doc_ck.add_paragraph(it)
doc_ck.save(os.path.join(output_dir, "Checklist_truoc_khi_nop.docx"))

doc_bb = docx.Document()
set_doc_header(doc_bb, "MẪU 06: BIÊN BẢN BÀN GIAO SẢN PHẨM & TÀI LIỆU KIỂM THỬ", "Học phần Đánh giá hiệu năng CSE3066")
doc_bb.add_heading("1. Thông tin bàn giao", level=1)
doc_bb.add_paragraph("Hôm nay, sinh viên bàn giao sản phẩm dự án và trọn bộ hồ sơ tài liệu kiểm thử cho Giảng viên hướng dẫn môn học CSE3066.")
doc_bb.add_heading("2. Danh mục sản phẩm & 10 tài liệu bàn giao đầy đủ", level=1)
doc_bb.add_paragraph(
    "1. Mã nguồn sản phẩm Web: https://github.com/QUANGPV021/calculator-qa-testing\n"
    "2. Website thực thi trực tuyến: https://quangpv021.github.io/calculator-qa-testing/\n"
    "3. Tai_lieu_URD.docx: Yêu cầu người dùng (Bối cảnh, 3 vai trò, 3 luồng nghiệp vụ, User Stories & Tiêu chí nghiệm thu).\n"
    "4. Tai_lieu_SRS.docx: Đặc tả yêu cầu phần mềm (14 chức năng FR, 3 luồng Main/Alt/Exception, 8 NFR, Bảng quyết định, Sơ đồ trạng thái).\n"
    "5. Mau_01_Tai_lieu_API.docx: Đặc tả các hàm và API chức năng của hệ thống.\n"
    "6. Mau_02_Bug_Manifest.xlsx: Danh mục 16 lỗi cài sẵn (5 nhóm: Functional, Visual, Content, Performance, Crash).\n"
    "7. Phieu_review_SRS.docx: Phiếu đánh giá, phản biện tài liệu SRS của Tester.\n"
    "8. Mau_04_Test_Plan.docx: Kế hoạch kiểm thử hoàn chỉnh theo chuẩn IEEE 829.\n"
    "9. Mau_03_Bo_bieu_mau_Kiem_thu.xlsx: Bộ biểu mẫu 20 Test Cases và tab Bug_Report chi tiết.\n"
    "10. Mau_05_Test_Summary_Report.docx: Báo cáo tổng kết nghiệm thu chất lượng phần mềm."
)
doc_bb.save(os.path.join(output_dir, "Mau_06_Bien_ban_ban_giao.docx"))
print("All updated and complete files generated successfully!")

