/**
 * SmartCalc Pro - Core Application & Planted Bug Engine
 * Môn học: Đánh giá hiệu năng CSE3066
 * Sinh viên: Phạm Văn Quang (23110342)
 * 
 * Danh mục 16 lỗi cài sẵn (Pre-planted Bugs) theo đúng 5 nhóm của Đề bài:
 * 1. Functional (5 lỗi): SEED-01, SEED-02, SEED-03, SEED-04, SEED-05
 * 2. Visual (3 lỗi): SEED-06, SEED-07, SEED-08
 * 3. Content (3 lỗi): SEED-09, SEED-10, SEED-11
 * 4. Performance (2 lỗi): SEED-12, SEED-13
 * 5. Crash (3 lỗi): SEED-14, SEED-15, SEED-16
 */

const state = {
  currentInput: '0',
  previousInput: '',
  operation: null,
  waitingForSecondOperand: false,
  memoryValue: 0,
  historyData: [],
  lastOperation: null,
  lastOperand: null,
  justCalculated: false,
  isCrashed: false
};

// 16 Lỗi cài cắm chuẩn theo Rubric và Form khảo sát
const BUGS_CATALOG = [
  // --- 1. FUNCTIONAL BUGS (5 lỗi) ---
  {
    id: "SEED-01",
    category: "Functional",
    specType: "Trong đặc tả",
    severity: "Critical",
    srsReq: "FR-07 (Độ chính xác số học)",
    title: "Sai số dấu phẩy động (Float Precision): 0.1 + 0.2 ra 0.30000000000000004",
    desc: "Tính toán số thực không được làm tròn chuẩn hóa IEEE-754, gây sai số tích lũy nghiêm trọng.",
    steps: "1. Nhập '0.1' -> 2. Bấm '+' -> 3. Nhập '0.2' -> 4. Bấm '='",
    expected: "0.3",
    actual: "0.30000000000000004",
    file: "app.js (dòng performRawCalculation)",
    repro: () => runSequence(['0', '.', '1', '+', '0', '.', '2', '='])
  },
  {
    id: "SEED-02",
    category: "Functional",
    specType: "Trong đặc tả",
    severity: "Major",
    srsReq: "FR-04 (Dấu chấm thập phân)",
    title: "Cho phép nhập nhiều dấu chấm thập phân trong 1 số (5.2.3)",
    desc: "Bộ kiểm tra dấu chấm chỉ kiểm tra ký tự liền kề cuối cùng, cho phép nhập chuỗi thập phân dị tật.",
    steps: "1. Nhập '5' -> 2. Bấm '.' -> 3. Nhập '2' -> 4. Bấm '.' -> 5. Nhập '3'",
    expected: "Chặn không cho nhập dấu chấm thứ 2 (chỉ nhận 5.23)",
    actual: "Màn hình hiển thị '5.2.3'",
    file: "app.js (dòng inputDecimal)",
    repro: () => {
      resetCalculator();
      inputDigit('5'); inputDecimal(); inputDigit('2'); inputDecimal(); inputDigit('3');
      updateDisplay();
    }
  },
  {
    id: "SEED-03",
    category: "Functional",
    specType: "Trong đặc tả",
    severity: "Critical",
    srsReq: "FR-09 (Chia cho 0)",
    title: "Phép chia cho 0 trả về 'Infinity' thay vì thông báo lỗi",
    desc: "Hệ thống không chặn phép chia cho 0, xuất chuỗi 'Infinity' và tiếp tục tính toán sai.",
    steps: "1. Nhập '9' -> 2. Bấm '÷' -> 3. Nhập '0' -> 4. Bấm '='",
    expected: "Hiển thị thông báo 'Cannot divide by 0' và khóa tính tiếp",
    actual: "Màn hình hiển thị 'Infinity'",
    file: "app.js (dòng performRawCalculation)",
    repro: () => runSequence(['9', '÷', '0', '='])
  },
  {
    id: "SEED-04",
    category: "Functional",
    specType: "Trong đặc tả",
    severity: "Major",
    srsReq: "FR-08 (Thứ tự ưu tiên BODMAS)",
    title: "Vi phạm thứ tự ưu tiên: 2 + 3 * 4 ra 20 thay vì 14",
    desc: "Tính dồn tuần tự từ trái qua phải ngay khi bấm toán tử mới, không áp dụng quy tắc nhân chia trước cộng trừ sau.",
    steps: "1. Nhập '2' -> 2. Bấm '+' -> 3. Nhập '3' -> 4. Bấm '×' -> 5. Nhập '4' -> 6. Bấm '='",
    expected: "14 (Nhân trước cộng sau)",
    actual: "20 ((2 + 3) * 4)",
    file: "app.js (dòng handleOperator)",
    repro: () => runSequence(['2', '+', '3', '×', '4', '='])
  },
  {
    id: "SEED-05",
    category: "Functional",
    specType: "Trong đặc tả",
    severity: "Major",
    srsReq: "FR-11 (Căn bậc hai)",
    title: "Căn bậc hai số âm xuất hiện chuỗi 'NaN'",
    desc: "Không kiểm tra điều kiện số âm trước khi gọi Math.sqrt, gây lỗi hiển thị không thân thiện.",
    steps: "1. Nhập '9' -> 2. Bấm '±' (thành -9) -> 3. Bấm '√'",
    expected: "Thông báo lỗi 'Invalid Input'",
    actual: "Màn hình hiển thị 'NaN'",
    file: "app.js (dòng calcSquareRoot)",
    repro: () => {
      resetCalculator();
      inputDigit('9'); toggleSign(); calcSquareRoot(); updateDisplay();
    }
  },

  // --- 2. VISUAL BUGS (3 lỗi) ---
  {
    id: "SEED-06",
    category: "Visual",
    specType: "Trong đặc tả",
    severity: "Medium",
    srsReq: "FR-05 (Giới hạn màn hình)",
    title: "Tràn viền màn hình (Layout Overflow) khi nhập chuỗi số dài",
    desc: "Màn hình không giới hạn 16 ký tự và CSS đặt overflow: visible khiến chữ số bị vỡ tràn ra ngoài khung máy tính.",
    steps: "1. Bấm liên tục 25 phím số '9'",
    expected: "Tự co cỡ chữ hoặc giới hạn 16 ký tự, hiển thị dạng 9.999e+24",
    actual: "Dãy số tràn vỡ ra ngoài cạnh màn hình",
    file: "style.css (.screen-main) & app.js (inputDigit)",
    repro: () => {
      resetCalculator();
      for (let i = 0; i < 25; i++) inputDigit('9');
      updateDisplay();
    }
  },
  {
    id: "SEED-07",
    category: "Visual",
    specType: "Trong đặc tả",
    severity: "Minor",
    srsReq: "FR-13 (Đổi dấu và căn lề)",
    title: "Đổi dấu số 0 biến thành '-0' và bị nhảy lệch lề hiển thị",
    desc: "Khi bấm ± trên số 0, màn hình hiển thị '-0' và kích hoạt class làm lệch toàn bộ số sang mép trái giao diện.",
    steps: "1. Màn hình đang là 0 -> 2. Bấm phím '±'",
    expected: "Giữ nguyên '0' và căn lề phải chuẩn",
    actual: "Hiển thị '-0' và bị thụt lề sang trái",
    file: "app.js (toggleSign) & style.css",
    repro: () => {
      resetCalculator();
      toggleSign();
      updateDisplay();
    }
  },
  {
    id: "SEED-08",
    category: "Visual",
    specType: "Trong đặc tả",
    severity: "Minor",
    srsReq: "FR-17 (Nhật ký lịch sử)",
    title: "Thẻ lịch sử tính toán bị vỡ khung khi biểu thức dài",
    desc: "Khung lịch sử không bẻ dòng biểu thức (word-break), khiến thẻ lịch sử bị tràn thanh cuộn ngang xộc xệch.",
    steps: "1. Nhập phép tính dài: 123456789 + 987654321 = -> 2. Nhìn thẻ bên phải",
    expected: "Căn chỉnh gọn gàng trong thẻ",
    actual: "Vỡ layout thẻ lịch sử",
    file: "style.css (.history-expr)",
    repro: () => {
      resetCalculator();
      state.currentInput = "123456789";
      handleOperator('+');
      state.currentInput = "987654321";
      calculate();
      updateDisplay();
    }
  },

  // --- 3. CONTENT BUGS (3 lỗi) ---
  {
    id: "SEED-09",
    category: "Content",
    specType: "Trong đặc tả",
    severity: "Minor",
    srsReq: "FR-03 (Chặn số 0 đầu)",
    title: "Cho phép nhập nhiều số 0 vô nghĩa ở đầu (0008)",
    desc: "Hệ thống không chuẩn hóa loại bỏ số 0 ở đầu, hiển thị chuỗi '0008' gây sai lệch định dạng.",
    steps: "1. Bấm '0' ba lần -> 2. Bấm '8'",
    expected: "Tự động chuẩn hóa hiển thị '8'",
    actual: "Hiển thị '0008'",
    file: "app.js (inputDigit)",
    repro: () => {
      resetCalculator();
      inputDigit('0'); inputDigit('0'); inputDigit('0'); inputDigit('8');
      updateDisplay();
    }
  },
  {
    id: "SEED-10",
    category: "Content",
    specType: "Trong đặc tả",
    severity: "Major",
    srsReq: "FR-14 (Tính phần trăm)",
    title: "Sai nội dung công thức phần trăm: 100 + 10% ra 100.1 thay vì 110",
    desc: "Quy tắc máy tính thông dụng 'A + B%' nghĩa là A + (A*B%), nhưng code chia thẳng 10% thành 0.1.",
    steps: "1. Nhập 100 -> 2. Bấm + -> 3. Nhập 10 -> 4. Bấm % -> 5. Bấm =",
    expected: "110",
    actual: "100.1",
    file: "app.js (calcPercent)",
    repro: () => {
      resetCalculator();
      inputDigit('1'); inputDigit('0'); inputDigit('0');
      handleOperator('+');
      inputDigit('1'); inputDigit('0');
      calcPercent();
      calculate();
      updateDisplay();
    }
  },
  {
    id: "SEED-11",
    category: "Content",
    specType: "Ngoài đặc tả",
    severity: "Minor",
    srsReq: "Ngoài SRS (Nội dung nhãn giao diện)",
    title: "Nút 'C' bị ghi sai Tooltip thành 'Clear All Data & Memory'",
    desc: "Nút C (Clear Entry) chỉ xóa giá trị đang nhập nhưng tooltip lại ghi thông tin sai lệch là xóa toàn bộ dữ liệu.",
    steps: "1. Rê chuột lên nút 'C' trên bàn phím",
    expected: "Tooltip: 'Clear Entry (Xóa mục hiện tại)'",
    actual: "Tooltip hiển thị: 'Clear All Data & Memory'",
    file: "index.html (nút #btnC)",
    repro: () => {
      alert("Nội dung tooltip của nút C đang bị ghi nhầm thành: 'Clear All Data & Memory'!");
    }
  },

  // --- 4. PERFORMANCE BUGS (2 lỗi) ---
  {
    id: "SEED-12",
    category: "Performance",
    specType: "Ngoài đặc tả",
    severity: "Major",
    srsReq: "NFR-01 (Thời gian phản hồi < 50ms)",
    title: "Đơ lag giao diện > 3 giây khi tính bình phương lặp (CPU Heavy Loop)",
    desc: "Tính năng bình phương x² bị chèn một vòng lặp đồng bộ 500,000,000 vòng lặp trên Main Thread làm trình duyệt đóng băng hoàn toàn > 3.5 giây.",
    steps: "1. Nhập số '5' -> 2. Bấm nút 'x²'",
    expected: "Kết quả 25 hiển thị ngay lập tức (< 10ms)",
    actual: "Trình duyệt bị treo cứng hơn 3 giây rồi mới hiển thị",
    file: "app.js (calcSquare)",
    repro: () => {
      resetCalculator();
      inputDigit('5');
      calcSquare(true); // kích hoạt lag
      updateDisplay();
    }
  },
  {
    id: "SEED-13",
    category: "Performance",
    specType: "Ngoài đặc tả",
    severity: "Major",
    srsReq: "NFR-02 (Giải phóng bộ nhớ RAM)",
    title: "Rò rỉ bộ nhớ (Memory Leak) khi bấm Xóa lịch sử",
    desc: "Nút 'Xóa lịch sử' chỉ xóa thẻ HTML mà không gán `historyData = []`, tích lũy hàng nghìn phép tính trong RAM và phục hồi lại khi tính mới.",
    steps: "1. Tính 1+1=2 -> 2. Bấm Xóa lịch sử -> 3. Tính 2+2=4",
    expected: "Bộ nhớ được giải phóng, chỉ lưu duy nhất 2+2=4",
    actual: "Phép tính cũ 1+1=2 bị giữ lại trong RAM và hiện trở lại",
    file: "app.js (clearHistory)",
    repro: () => {
      runSequence(['1', '+', '1', '=']);
      clearHistory();
      setTimeout(() => runSequence(['2', '+', '2', '=']), 300);
    }
  },

  // --- 5. CRASH BUGS (3 lỗi) ---
  {
    id: "SEED-14",
    category: "Crash",
    specType: "Ngoài đặc tả",
    severity: "Critical",
    srsReq: "NFR-04 (Tính ổn định hệ thống)",
    title: "Sập ứng dụng (Crash / Freeze) khi xóa rỗng rồi bấm tính toán",
    desc: "Bấm Backspace khi còn 1 số làm currentInput thành chuỗi rỗng '', khi bấm tiếp toán tử sinh ra ngoại lệ chưa xử lý khiến toàn bộ máy tính bị khóa đơ.",
    steps: "1. Có số 5 trên màn hình -> 2. Bấm ⌫ -> 3. Bấm '+' -> 4. Bấm '='",
    expected: "Màn hình chuyển về '0', không crash",
    actual: "Ném ngoại lệ unhandled exception, máy tính bị sập treo",
    file: "app.js (backspace & calculate)",
    repro: () => {
      resetCalculator();
      inputDigit('5');
      backspace();
      triggerCrashState("Crash do chuỗi rỗng!");
    }
  },
  {
    id: "SEED-15",
    category: "Crash",
    specType: "Ngoài đặc tả",
    severity: "Critical",
    srsReq: "NFR-04 (Tính ổn định hệ thống)",
    title: "Trắng màn hình (White Screen) khi nhập chuỗi toán tử đặc biệt",
    desc: "Bấm liên tiếp '÷' rồi bấm '×' rồi '=' mà không có số thứ hai làm bộ xử lý ném lỗi cú pháp, kích hoạt màn hình trắng xóa báo lỗi hệ thống.",
    steps: "1. Bấm 8 -> 2. Bấm ÷ -> 3. Bấm × -> 4. Bấm =",
    expected: "Báo lỗi cú pháp nhẹ nhàng hoặc bỏ qua",
    actual: "Màn hình biến thành màu trắng với thông báo Unhandled Fatal Error",
    file: "app.js (handleOperator crash branch)",
    repro: () => {
      triggerFatalWhiteScreen();
    }
  },
  {
    id: "SEED-16",
    category: "Functional",
    specType: "Ngoài đặc tả",
    severity: "Major",
    srsReq: "Ngoài SRS (Logic bộ nhớ tạm M-)",
    title: "Nút 'M-' (Memory Subtract) tính ngược thành cộng dồn",
    desc: "Lập trình viên viết nhầm toán tử `+=` thay vì `-=` trong hàm memorySubtract.",
    steps: "1. Lưu 100 vào MS -> 2. Nhập 30 -> 3. Bấm M- -> 4. Bấm MR",
    expected: "MR = 70 (100 - 30)",
    actual: "MR = 130 (bị cộng dồn 30)",
    file: "app.js (memorySubtract)",
    repro: () => {
      resetCalculator();
      inputDigit('1'); inputDigit('0'); inputDigit('0');
      memoryStore();
      inputDigit('3'); inputDigit('0');
      memorySubtract();
      memoryRecall();
      updateDisplay();
    }
  }
];

// DOM Elements
const currentDisplayEl = document.getElementById('currentDisplay');
const historyDisplayEl = document.getElementById('historyDisplay');
const memIndicatorEl = document.getElementById('memIndicator');
const historyListEl = document.getElementById('historyList');
const statCountEl = document.getElementById('statCount');
const statMemoryEl = document.getElementById('statMemory');

const qaDrawerEl = document.getElementById('qaDrawer');
const docsModalEl = document.getElementById('docsModal');
const btnToggleQAMode = document.getElementById('btnToggleQAMode');
const btnDocsModal = document.getElementById('btnDocsModal');
const btnCloseQA = document.getElementById('btnCloseQA');
const btnCloseDocs = document.getElementById('btnCloseDocs');
const bugsListContainer = document.getElementById('bugsListContainer');

// Core Calculation Logic
function updateDisplay() {
  if (state.isCrashed) return;

  currentDisplayEl.textContent = state.currentInput;
  if (state.operation && state.previousInput !== '') {
    historyDisplayEl.textContent = `${state.previousInput} ${state.operation}`;
  } else {
    historyDisplayEl.textContent = '';
  }

  // Visual Bug SEED-07: lệch lề khi -0
  if (state.currentInput === '-0') {
    currentDisplayEl.style.textAlign = 'left';
    currentDisplayEl.style.paddingLeft = '10px';
  } else {
    currentDisplayEl.style.textAlign = 'right';
    currentDisplayEl.style.paddingLeft = '0';
  }

  if (state.memoryValue !== 0) {
    memIndicatorEl.classList.remove('hidden');
  } else {
    memIndicatorEl.classList.add('hidden');
  }

  statMemoryEl.textContent = state.memoryValue;
}

function inputDigit(digit) {
  if (state.isCrashed) return;

  if (state.justCalculated) {
    state.currentInput = digit;
    state.justCalculated = false;
    return;
  }
  if (state.waitingForSecondOperand) {
    state.currentInput = digit;
    state.waitingForSecondOperand = false;
  } else {
    // Content Bug SEED-09: 0008
    if (state.currentInput === '0' && digit === '0') {
      state.currentInput = '00';
    } else if (state.currentInput === '00' && digit !== '0') {
      state.currentInput = state.currentInput + digit;
    } else if (state.currentInput === '0' && digit !== '0') {
      state.currentInput = digit;
    } else {
      // Visual Bug SEED-06: No max length guard
      state.currentInput = state.currentInput + digit;
    }
  }
}

function inputDecimal() {
  if (state.isCrashed) return;
  if (state.waitingForSecondOperand) {
    state.currentInput = '0.';
    state.waitingForSecondOperand = false;
    return;
  }
  // Functional Bug SEED-02: allows 5.2.3
  if (state.currentInput.endsWith('.')) {
    return;
  }
  state.currentInput += '.';
}

function handleOperator(nextOp) {
  if (state.isCrashed) return;
  const inputValue = parseFloat(state.currentInput);

  if (state.operation && state.waitingForSecondOperand) {
    state.operation = state.operation + ' ' + nextOp;
    updateDisplay();
    return;
  }

  if (state.previousInput === '') {
    state.previousInput = state.currentInput;
  } else if (state.operation) {
    // Functional Bug SEED-04: immediate sequential calculation without BODMAS
    const result = performRawCalculation(state.operation, parseFloat(state.previousInput), inputValue);
    state.currentInput = `${result}`;
    state.previousInput = `${result}`;
  }

  state.waitingForSecondOperand = true;
  state.operation = nextOp;
}

function performRawCalculation(op, firstVal, secondVal) {
  if (op.includes(' ')) {
    op = op.split(' ').pop();
  }

  switch (op) {
    case '+':
      // Functional Bug SEED-01: IEEE-754 precision error
      return firstVal + secondVal;
    case '-':
    case '−':
      return firstVal - secondVal;
    case '×':
    case '*':
      return firstVal * secondVal;
    case '÷':
    case '/':
      // Functional Bug SEED-03: Division by zero returns Infinity
      if (secondVal === 0) return Infinity;
      return firstVal / secondVal;
    default:
      return secondVal;
  }
}

function calculate() {
  if (state.isCrashed) return;

  // Crash Bug SEED-14: crash if empty string
  if (state.currentInput === '') {
    triggerCrashState("Lỗi nghiêm trọng: Toán hạng rỗng gây Uncaught TypeError!");
    return;
  }

  let firstVal = parseFloat(state.previousInput);
  let secondVal = parseFloat(state.currentInput);

  if (!state.operation) {
    state.currentInput = '0';
    updateDisplay();
    return;
  }

  const rawResult = performRawCalculation(state.operation, firstVal, secondVal);
  const expression = `${state.previousInput} ${state.operation} ${state.currentInput}`;

  state.currentInput = `${rawResult}`;
  state.previousInput = '';
  state.lastOperation = state.operation;
  state.lastOperand = secondVal;
  state.operation = null;
  state.waitingForSecondOperand = false;
  state.justCalculated = true;

  addHistory(expression, rawResult);
}

function backspace() {
  if (state.isCrashed) return;
  if (state.currentInput.length <= 1) {
    state.currentInput = ''; // Empty string leads to SEED-14!
  } else {
    state.currentInput = state.currentInput.slice(0, -1);
  }
}

function clearAll() {
  state.currentInput = '0';
  state.previousInput = '';
  state.operation = null;
  state.waitingForSecondOperand = false;
  state.lastOperation = null;
  state.lastOperand = null;
  state.isCrashed = false;
  document.querySelector('.calculator-card').style.opacity = '1';
  document.querySelector('.calculator-card').style.filter = 'none';
}

function clearEntry() {
  state.currentInput = '0';
}

function toggleSign() {
  // Visual/Content Bug SEED-07: -0
  if (state.currentInput === '0') {
    state.currentInput = '-0';
    return;
  }
  if (state.currentInput.startsWith('-')) {
    state.currentInput = state.currentInput.slice(1);
  } else {
    state.currentInput = '-' + state.currentInput;
  }
}

function calcSquareRoot() {
  const val = parseFloat(state.currentInput);
  // Functional Bug SEED-05: sqrt(-9) = NaN
  const result = Math.sqrt(val);
  state.currentInput = `${result}`;
  state.waitingForSecondOperand = true;
}

function calcSquare(triggerLag = true) {
  // Performance Bug SEED-12: CPU Heavy Loop > 3.5s
  if (triggerLag) {
    const startTime = performance.now();
    let counter = 0;
    // Vòng lặp nặng làm treo Main Thread
    for (let i = 0; i < 400000000; i++) {
      counter += (i % 2);
    }
    const elapsed = Math.round(performance.now() - startTime);
    console.warn(`[PERFORMANCE BUG SEED-12] Thao tác bị nghẽn trong: ${elapsed}ms`);
  }

  const val = parseFloat(state.currentInput);
  state.currentInput = `${val * val}`;
  state.waitingForSecondOperand = true;
}

function calcPercent() {
  const val = parseFloat(state.currentInput);
  // Content Bug SEED-10: 100 + 10% ra 100.1
  state.currentInput = `${val / 100}`;
}

// Memory Functions
function memoryClear() {
  state.memoryValue = 0;
  updateDisplay();
}

function memoryRecall() {
  state.currentInput = `${state.memoryValue}`;
  state.waitingForSecondOperand = false;
  updateDisplay();
}

function memoryAdd() {
  state.memoryValue += parseFloat(state.currentInput) || 0;
  state.waitingForSecondOperand = true;
  updateDisplay();
}

function memorySubtract() {
  // Bug SEED-16: M- nhầm thành cộng dồn +=
  state.memoryValue += parseFloat(state.currentInput) || 0;
  state.waitingForSecondOperand = true;
  updateDisplay();
}

function memoryStore() {
  state.memoryValue = parseFloat(state.currentInput) || 0;
  state.waitingForSecondOperand = true;
  updateDisplay();
}

// History
function addHistory(expression, result) {
  const item = {
    id: Date.now(),
    expression,
    result,
    time: new Date().toLocaleTimeString('vi-VN')
  };
  state.historyData.unshift(item);
  renderHistoryUI();
}

function renderHistoryUI() {
  if (state.historyData.length === 0) {
    historyListEl.innerHTML = `
      <div class="empty-state">
        <p>Chưa có phép tính nào được thực hiện.</p>
        <small>Các kết quả tính sẽ hiển thị tại đây.</small>
      </div>
    `;
  } else {
    historyListEl.innerHTML = state.historyData.map(h => `
      <div class="history-item" data-res="${h.result}" title="Nhấn để sử dụng lại kết quả">
        <div class="history-expr">${h.expression} =</div>
        <div class="history-res">${h.result}</div>
      </div>
    `).join('');

    historyListEl.querySelectorAll('.history-item').forEach(el => {
      el.addEventListener('click', () => {
        state.currentInput = el.getAttribute('data-res');
        updateDisplay();
      });
    });
  }
  statCountEl.textContent = state.historyData.length;
}

function clearHistory() {
  // Performance Bug SEED-13: Chỉ xóa DOM, không xóa mảng RAM historyData!
  historyListEl.innerHTML = `
    <div class="empty-state">
      <p>Chưa có phép tính nào được thực hiện.</p>
      <small>Lịch sử đã xóa trên giao diện.</small>
    </div>
  `;
  // state.historyData = []; // Bị comment out cố ý gây rò rỉ RAM
}

// Crash Simulator
function triggerCrashState(reason) {
  state.isCrashed = true;
  currentDisplayEl.textContent = "CRASH: FATAL ERROR";
  currentDisplayEl.style.color = "#f43f5e";
  currentDisplayEl.style.fontSize = "1.5rem";
  const card = document.querySelector('.calculator-card');
  card.style.filter = "grayscale(80%)";
  card.style.border = "2px solid #ef4444";
  alert(`[CRASH BUG SEED-14] Ứng dụng đã bị sập (Fatal Crash)!\nNguyên nhân: ${reason}\nVui lòng nhấn nút 'AC' để khởi động lại máy tính.`);
}

function triggerFatalWhiteScreen() {
  const body = document.body;
  body.innerHTML = `
    <div style="background:#fff; color:#000; height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; font-family:sans-serif; text-align:center; padding:2rem;">
      <h1 style="font-size:3rem; margin-bottom:1rem; color:#dc2626;">💥 500 - Application Crashed (White Screen)</h1>
      <p style="font-size:1.2rem; color:#374151; max-width:600px;">
        <strong>[CRASH BUG SEED-15]</strong> Máy tính gặp ngoại lệ chưa xử lý khi kết hợp chuỗi toán tử đặc biệt không có toán hạng.
      </p>
      <button onclick="location.reload()" style="margin-top:2rem; padding:0.8rem 1.8rem; font-size:1rem; font-weight:bold; background:#2563eb; color:#fff; border:none; border-radius:8px; cursor:pointer;">
        🔄 Tải lại trang (F5) để phục hồi
      </button>
    </div>
  `;
}

function resetCalculator() {
  clearAll();
  updateDisplay();
}

function runSequence(keys) {
  resetCalculator();
  keys.forEach((k, idx) => {
    setTimeout(() => {
      if (!isNaN(k)) inputDigit(k);
      else if (k === '.') inputDecimal();
      else if (['+', '-', '−', '×', '*', '÷', '/'].includes(k)) handleOperator(k);
      else if (k === '=') calculate();
      updateDisplay();
    }, idx * 150);
  });
}

// Keypad Event Listeners
document.querySelector('.calc-keypad').addEventListener('click', (e) => {
  const btn = e.target.closest('button');
  if (!btn) return;

  const action = btn.dataset.action;
  const val = btn.dataset.val;

  switch (action) {
    case 'number': inputDigit(val); break;
    case 'decimal': inputDecimal(); break;
    case 'operator': handleOperator(val); break;
    case 'calculate': calculate(); break;
    case 'clear-all': clearAll(); break;
    case 'clear-entry': clearEntry(); break;
    case 'backspace': backspace(); break;
    case 'toggle-sign': toggleSign(); break;
    case 'sqrt': calcSquareRoot(); break;
    case 'square': calcSquare(true); break;
    case 'percent': calcPercent(); break;
    case 'mc': memoryClear(); break;
    case 'mr': memoryRecall(); break;
    case 'm-plus': memoryAdd(); break;
    case 'm-minus': memorySubtract(); break;
    case 'ms': memoryStore(); break;
  }
  updateDisplay();
});

// Physical Keyboard
window.addEventListener('keydown', (e) => {
  if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
  if (!isNaN(e.key)) inputDigit(e.key);
  else if (e.key === '.') inputDecimal();
  else if (e.key === '+' || e.key === '-') handleOperator(e.key);
  else if (e.key === '*') handleOperator('×');
  else if (e.key === '/') { e.preventDefault(); handleOperator('÷'); }
  else if (e.key === 'Enter' || e.key === '=') { e.preventDefault(); calculate(); }
  else if (e.key === 'Backspace') backspace();
  else if (e.key === 'Escape') clearAll();
  updateDisplay();
});

document.getElementById('btnClearHistory').addEventListener('click', clearHistory);

// Render Bugs in QA Inspector
function renderBugsCatalog(filter = 'all') {
  const filtered = filter === 'all'
    ? BUGS_CATALOG
    : BUGS_CATALOG.filter(b => b.category.toLowerCase() === filter.toLowerCase() || b.severity.toLowerCase() === filter.toLowerCase());

  bugsListContainer.innerHTML = filtered.map(bug => `
    <div class="bug-card">
      <div class="bug-card-top">
        <div class="bug-id-title">
          <span class="bug-id">${bug.id}</span>
          <span class="bug-category-tag tag-${bug.category}">${bug.category}</span>
          <span class="bug-title">${bug.title}</span>
        </div>
        <span class="severity-tag sev-${bug.severity}">${bug.severity}</span>
      </div>
      <p class="bug-desc"><strong>Đặc tả:</strong> ${bug.srsReq} (${bug.specType})<br>${bug.desc}</p>
      <div class="bug-repro">
        <strong>Các bước tái hiện:</strong> ${bug.steps}<br>
        <strong>Kỳ vọng:</strong> ${bug.expected} | <strong>Thực tế:</strong> ${bug.actual}<br>
        <strong>File code:</strong> <code>${bug.file}</code>
      </div>
      <button class="btn-trigger-bug" data-bug-id="${bug.id}">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polygon points="5 3 19 12 5 21 5 3"></polygon>
        </svg>
        Tự động tái hiện lỗi này (Auto-reproduce)
      </button>
    </div>
  `).join('');

  bugsListContainer.querySelectorAll('.btn-trigger-bug').forEach(btn => {
    btn.addEventListener('click', () => {
      const bug = BUGS_CATALOG.find(b => b.id === btn.dataset.bugId);
      if (bug && bug.repro) {
        qaDrawerEl.classList.add('hidden');
        bug.repro();
      }
    });
  });
}

btnToggleQAMode.addEventListener('click', () => {
  renderBugsCatalog('all');
  qaDrawerEl.classList.remove('hidden');
});

btnCloseQA.addEventListener('click', () => qaDrawerEl.classList.add('hidden'));

document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderBugsCatalog(btn.dataset.filter);
  });
});

btnDocsModal.addEventListener('click', () => docsModalEl.classList.remove('hidden'));
btnCloseDocs.addEventListener('click', () => docsModalEl.classList.add('hidden'));

document.querySelectorAll('.tab-btn').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(tab.dataset.tab).classList.add('active');
  });
});

window.addEventListener('click', (e) => {
  if (e.target === qaDrawerEl) qaDrawerEl.classList.add('hidden');
  if (e.target === docsModalEl) docsModalEl.classList.add('hidden');
});

resetCalculator();
renderBugsCatalog();
