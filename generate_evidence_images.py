import os
from PIL import Image, ImageDraw, ImageFont

assets_dir = "/Users/phamquang/Projects/calculator-qa-testing/assets"
os.makedirs(assets_dir, exist_ok=True)

bugs = [
    {
        "id": "SEED-01", "num": "01", "cat": "Functional", "sev": "Critical",
        "title": "Sai số dấu phẩy động IEEE-754 (0.1 + 0.2 ra 0.30000000000000004)",
        "steps": "1. Nhập '0.1' -> 2. Bấm '+' -> 3. Nhập '0.2' -> 4. Bấm '='",
        "expected": "0.3 (Được làm tròn chuẩn số học)",
        "actual": "0.30000000000000004",
        "root": "app.js (performRawCalculation): return firstVal + secondVal"
    },
    {
        "id": "SEED-02", "num": "02", "cat": "Functional", "sev": "Major",
        "title": "Cho phép nhập nhiều dấu chấm thập phân (5.2.3)",
        "steps": "1. Nhập '5' -> 2. Bấm '.' -> 3. Nhập '2' -> 4. Bấm '.' -> 5. Nhập '3'",
        "expected": "Chỉ nhận 1 dấu chấm hợp lệ (5.23)",
        "actual": "Màn hình hiển thị chuỗi dị tật '5.2.3'",
        "root": "app.js (inputDecimal): chỉ kiểm tra ký tự liền kề cuối cùng"
    },
    {
        "id": "SEED-03", "num": "03", "cat": "Functional", "sev": "Critical",
        "title": "Phép chia cho 0 xuất hiện 'Infinity' thay vì thông báo lỗi",
        "steps": "1. Nhập '9' -> 2. Bấm '÷' -> 3. Nhập '0' -> 4. Bấm '='",
        "expected": "Báo lỗi 'Cannot divide by 0' và khóa tính tiếp",
        "actual": "Màn hình xuất chuỗi 'Infinity'",
        "root": "app.js (performRawCalculation): if (secondVal === 0) return Infinity;"
    },
    {
        "id": "SEED-04", "num": "04", "cat": "Functional", "sev": "Major",
        "title": "Vi phạm thứ tự BODMAS: 2 + 3 * 4 ra 20 thay vì 14",
        "steps": "1. Nhập 2 + 3 × 4 =",
        "expected": "14 (Nhân chia trước, cộng trừ sau)",
        "actual": "20 ((2 + 3) * 4 do tính dồn từ trái qua phải)",
        "root": "app.js (handleOperator): tính ngay khi gặp toán tử mới"
    },
    {
        "id": "SEED-05", "num": "05", "cat": "Functional", "sev": "Major",
        "title": "Căn bậc hai số âm xuất hiện chuỗi 'NaN'",
        "steps": "1. Nhập 9 -> 2. Bấm ± (-9) -> 3. Bấm √",
        "expected": "Báo lỗi hợp lệ 'Invalid Input'",
        "actual": "Màn hình hiển thị chuỗi 'NaN'",
        "root": "app.js (calcSquareRoot): Math.sqrt(val) thiếu kiểm tra val < 0"
    },
    {
        "id": "SEED-06", "num": "06", "cat": "Visual", "sev": "Medium",
        "title": "Tràn viền màn hình (Layout Overflow) khi nhập > 16 số",
        "steps": "1. Nhập liên tục 25 phím số '9'",
        "expected": "Giới hạn 16 số hoặc tự co nhỏ cỡ chữ e-notation",
        "actual": "Dãy số tràn vượt ra khỏi khung máy tính làm vỡ giao diện",
        "root": "style.css (.screen-main) đặt overflow: visible & thiếu maxlength"
    },
    {
        "id": "SEED-07", "num": "07", "cat": "Visual", "sev": "Minor",
        "title": "Đổi dấu số 0 biến thành '-0' và nhảy lệch lề trái",
        "steps": "1. Màn hình đang là 0 -> 2. Bấm phím '±'",
        "expected": "Vẫn giữ nguyên là '0' và căn lề phải chuẩn",
        "actual": "Hiển thị '-0' và bị nhảy thụt lề sang mép trái",
        "root": "app.js (toggleSign) tạo -0 & kích hoạt căn lề trái"
    },
    {
        "id": "SEED-08", "num": "08", "cat": "Visual", "sev": "Minor",
        "title": "Thẻ lịch sử tính toán bị vỡ khung khi biểu thức dài",
        "steps": "1. Nhập phép tính dài: 123456789 + 987654321 = -> 2. Nhìn thẻ bên phải",
        "expected": "Biểu thức tự động ngắt dòng gọn gàng trong thẻ",
        "actual": "Khung lịch sử bị tràn thanh cuộn ngang xộc xệch",
        "root": "style.css (.history-expr) thiếu word-break: break-all"
    },
    {
        "id": "SEED-09", "num": "09", "cat": "Content", "sev": "Minor",
        "title": "Cho phép nhập nhiều số 0 vô nghĩa ở đầu (0008)",
        "steps": "1. Bấm '0' ba lần -> 2. Bấm '8'",
        "expected": "Tự động chuẩn hóa thành '8'",
        "actual": "Màn hình hiển thị chuỗi '0008'",
        "root": "app.js (inputDigit): state.currentInput = '00' khi nhập 0 liên tiếp"
    },
    {
        "id": "SEED-10", "num": "10", "cat": "Content", "sev": "Major",
        "title": "Sai công thức tính phần trăm: 100 + 10% ra 100.1 thay vì 110",
        "steps": "1. Nhập 100 + 10 % =",
        "expected": "110 (100 + 10% của 100)",
        "actual": "100.1 (code chia thẳng 10% thành 0.1 rồi cộng)",
        "root": "app.js (calcPercent): state.currentInput = val / 100"
    },
    {
        "id": "SEED-11", "num": "11", "cat": "Content", "sev": "Minor",
        "title": "Nút 'C' bị ghi sai Tooltip thành 'Clear All Data & Memory'",
        "steps": "1. Rê chuột lên nút 'C' trên bàn phím",
        "expected": "Tooltip: 'Clear Entry (Xóa mục hiện tại)'",
        "actual": "Tooltip hiển thị: 'Clear All Data & Memory'",
        "root": "index.html (nút #btnC) title='Clear All Data & Memory'"
    },
    {
        "id": "SEED-12", "num": "12", "cat": "Performance", "sev": "Major",
        "title": "Đơ lag giao diện > 3 giây khi bấm x² (CPU Heavy Loop vi phạm NFR-01)",
        "steps": "1. Nhập số '5' -> 2. Bấm nút 'x²' (Bình phương)",
        "expected": "Kết quả 25 hiển thị tức thì (< 10ms theo NFR-01)",
        "actual": "Trình duyệt bị treo Main Thread > 3.2 giây rồi mới hiển thị",
        "root": "app.js (calcSquare): vòng lặp 400,000,000 lần khóa Main Thread"
    },
    {
        "id": "SEED-13", "num": "13", "cat": "Performance", "sev": "Major",
        "title": "Rò rỉ bộ nhớ RAM (Memory Leak) khi bấm Xóa lịch sử",
        "steps": "1. Tính 1+1=2 -> 2. Bấm Xóa lịch sử -> 3. Tính 2+2=4",
        "expected": "Mảng RAM được giải phóng, chỉ lưu duy nhất 2+2=4",
        "actual": "Phép tính cũ 1+1=2 bị phục hồi do mảng RAM historyData không bị xóa",
        "root": "app.js (clearHistory): comment out dòng state.historyData = []"
    },
    {
        "id": "SEED-14", "num": "14", "cat": "Crash", "sev": "Critical",
        "title": "Sập ứng dụng (Fatal Crash) khi xóa rỗng rồi bấm tính toán",
        "steps": "1. Có số 5 trên màn hình -> 2. Bấm ⌫ -> 3. Bấm '+' -> 4. Bấm '='",
        "expected": "Màn hình chuyển về '0' an toàn, không ném lỗi",
        "actual": "Ném ngoại lệ Unhandled TypeError, máy tính bị sập treo đơ",
        "root": "app.js (backspace) gán chuỗi rỗng '' & calculate ném lỗi"
    },
    {
        "id": "SEED-15", "num": "15", "cat": "Crash", "sev": "Critical",
        "title": "Trắng màn hình (White Screen 500) khi nhập chuỗi toán tử đặc biệt",
        "steps": "1. Bấm 8 -> 2. Bấm ÷ -> 3. Bấm × -> 4. Bấm =",
        "expected": "Báo lỗi cú pháp nhẹ nhàng hoặc bỏ qua",
        "actual": "Giao diện biến thành màn hình trắng báo 500 Unhandled Exception",
        "root": "app.js (triggerFatalWhiteScreen)"
    },
    {
        "id": "SEED-16", "num": "16", "cat": "Functional", "sev": "Major",
        "title": "Nút 'M-' (Memory Subtract) tính ngược thành cộng dồn",
        "steps": "1. Lưu 100 vào MS -> 2. Nhập 30 -> 3. Bấm M- -> 4. Bấm MR",
        "expected": "MR = 70 (100 - 30)",
        "actual": "MR = 130 (bị cộng dồn 30 vào bộ nhớ)",
        "root": "app.js (memorySubtract): state.memoryValue += val nhầm dấu"
    }
]

W, H = 1000, 560
bg_color = (15, 23, 42) # Slate 900
card_color = (30, 41, 59) # Slate 800
border_color = (51, 65, 85)

for b in bugs:
    img = Image.new("RGB", (W, H), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Viền card chính
    draw.rounded_rectangle([30, 30, W - 30, H - 30], radius=16, fill=card_color, outline=border_color, width=2)

    # Header bar
    draw.rounded_rectangle([30, 30, W - 30, 95], radius=16, fill=(31, 78, 121))
    draw.rectangle([30, 75, W - 30, 95], fill=(31, 78, 121))

    # Header text
    draw.text((50, 45), f"SMARTCALC PRO - MINH CHỨNG LỖI BÍ MẬT [{b['id']}]", fill=(255, 255, 255))
    draw.text((W - 280, 45), f"SEVERITY: {b['sev'].upper()}", fill=(253, 224, 71))
    draw.text((W - 130, 45), f"[{b['cat']}]", fill=(147, 197, 253))

    # Title
    draw.text((50, 115), "Tiêu đề lỗi (Title):", fill=(148, 163, 184))
    draw.text((50, 135), b["title"], fill=(248, 250, 252))

    # Steps
    draw.text((50, 175), "Các bước tái hiện (Steps to Reproduce):", fill=(148, 163, 184))
    draw.rounded_rectangle([50, 195, W - 50, 240], radius=8, fill=(15, 23, 42), outline=(71, 85, 105))
    draw.text((65, 207), b["steps"], fill=(56, 189, 248))

    # Comparison Grid: Actual vs Expected
    # Actual Box (Red)
    draw.rounded_rectangle([50, 260, 480, 380], radius=10, fill=(69, 10, 10), outline=(239, 68, 68), width=2)
    draw.text((65, 275), "❌ KẾT QUẢ THỰC TẾ (ACTUAL RESULT - BUG):", fill=(248, 113, 113))
    draw.text((65, 305), b["actual"], fill=(255, 255, 255))

    # Expected Box (Green)
    draw.rounded_rectangle([520, 260, W - 50, 380], radius=10, fill=(6, 78, 59), outline=(16, 185, 129), width=2)
    draw.text((535, 275), "✅ KẾT QUẢ KỲ VỌNG (EXPECTED RESULT - SRS):", fill=(52, 211, 153))
    draw.text((535, 305), b["expected"], fill=(255, 255, 255))

    # Root cause
    draw.text((50, 400), "Vị trí mã nguồn gây lỗi (Root Cause):", fill=(148, 163, 184))
    draw.rounded_rectangle([50, 420, W - 50, 460], radius=8, fill=(15, 23, 42), outline=(71, 85, 105))
    draw.text((65, 432), b["root"], fill=(251, 146, 60))

    # Footer
    draw.text((50, 485), "Học phần: Đánh giá hiệu năng CSE3066 | Tester: Phạm Văn Quang (23110342) | Hệ thống: SmartCalc Pro", fill=(100, 116, 139))
    draw.text((W - 270, 485), "Live: quangpv021.github.io", fill=(99, 102, 241))

    out_file = os.path.join(assets_dir, f"evidence_bug{b['num']}.png")
    img.save(out_file)
    print(f"Generated: {out_file}")

print("All 16 bug evidence images generated successfully!")

