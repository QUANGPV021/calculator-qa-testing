/**
 * SmartCalc Pro - Core Application & Buggy Engine
 * Mục đích: Ứng dụng máy tính bỏ túi đa chức năng phục vụ đồ án kiểm thử phần mềm.
 * Chứa 15 lỗi logic / UI / validation có chủ đích cho sinh viên & tester thực hành.
 */

// ==========================================
// 1. DATA STATE & CONFIGURATION
// ==========================================
const state = {
  currentInput: '0',
  previousInput: '',
  operation: null,
  waitingForSecondOperand: false,
  memoryValue: 0,
  historyData: [], // Stores { expression, result, timestamp }
  lastOperation: null,
  lastOperand: null
};

// Danh mục 15 lỗi cài cắm (Bug Catalog)
const BUGS_CATALOG = [
  {
    id: "BUG-01",
    severity: "Critical",
    title: "Lỗi độ chính xác số thực (Floating-Point Precision)",
    desc: "Tính toán số thập phân cơ bản như 0.1 + 0.2 cho ra 0.30000000000000004 thay vì 0.3 do không format kết quả chuẩn IEEE 754.",
    steps: "1. Nhập '0.1' -> 2. Nhấn '+' -> 3. Nhập '0.2' -> 4. Nhấn '='",
    expected: "0.3",
    actual: "0.30000000000000004",
    repro: () => {
      runCalculationSequence(['0', '.', '1', '+', '0', '.', '2', '=']);
    }
  },
  {
    id: "BUG-02",
    severity: "Major",
    title: "Cho phép nhập nhiều dấu chấm thập phân trong cùng 1 số",
    desc: "Hệ thống không chặn việc người dùng nhập liên tiếp hoặc rải rác nhiều dấu chấm thập phân (VD: 5.2.3.1).",
    steps: "1. Nhập '5' -> 2. Nhấn '.' -> 3. Nhập '2' -> 4. Nhấn '.' -> 5. Nhập '3'",
    expected: "Chỉ cho phép 1 dấu chấm (5.23)",
    actual: "Màn hình hiển thị '5.2.3'",
    repro: () => {
      resetCalculator();
      inputDigit('5');
      inputDecimal();
      inputDigit('2');
      inputDecimal(); // BUG: allows multiple
      inputDigit('3');
      updateDisplay();
    }
  },
  {
    id: "BUG-03",
    severity: "Critical",
    title: "Phép chia cho 0 trả về 'Infinity' thay vì thông báo lỗi",
    desc: "Khi thực hiện phép chia bất kỳ số nào cho 0, hệ thống xuất 'Infinity' và cho phép thực hiện tiếp các phép tính làm sai lệch hệ thống.",
    steps: "1. Nhập '9' -> 2. Nhấn '÷' -> 3. Nhập '0' -> 4. Nhấn '='",
    expected: "Hiển thị thông báo 'Cannot divide by zero' hoặc 'Error'",
    actual: "Hiển thị 'Infinity'",
    repro: () => {
      runCalculationSequence(['9', '÷', '0', '=']);
    }
  },
  {
    id: "BUG-04",
    severity: "Major",
    title: "Vi phạm thứ tự ưu tiên toán học (Operator Precedence)",
    desc: "Khi tính toán chuỗi biểu thức 2 + 3 * 4 liên tiếp, hệ thống thực hiện tuần tự từ trái sang phải ((2 + 3) * 4 = 20) thay vì tuân theo BODMAS (14).",
    steps: "1. Nhập '2' -> 2. Nhấn '+' -> 3. Nhập '3' -> 4. Nhấn '×' -> 5. Nhập '4' -> 6. Nhấn '='",
    expected: "Kết quả đúng toán học là 14 (nhân chia trước cộng trừ sau)",
    actual: "Kết quả trả về 20",
    repro: () => {
      runCalculationSequence(['2', '+', '3', '×', '4', '=']);
    }
  },
  {
    id: "BUG-05",
    severity: "Major",
    title: "Căn bậc hai số âm trả về 'NaN'",
    desc: "Nhấn nút tính căn bậc hai (√) khi số đang hiển thị là số âm (VD: -9) xuất hiện giá trị NaN không thân thiện.",
    steps: "1. Nhập '9' -> 2. Nhấn '±' (thành -9) -> 3. Nhấn nút '√'",
    expected: "Thông báo lỗi 'Invalid Input' hoặc chặn không cho tính",
    actual: "Hiển thị chuỗi 'NaN'",
    repro: () => {
      resetCalculator();
      inputDigit('9');
      toggleSign();
      calcSquareRoot();
      updateDisplay();
    }
  },
  {
    id: "BUG-06",
    severity: "Minor",
    title: "Cho phép nhập nhiều số 0 vô nghĩa ở đầu (Leading Zeros)",
    desc: "Người dùng có thể nhập liên tục nhiều số 0 ở đầu số nguyên, ví dụ '0008' thay vì tự động format thành '8'.",
    steps: "1. Nhấn nút '0' nhiều lần -> 2. Nhấn nút '8'",
    expected: "Chỉ hiển thị '8' (hoặc tối đa một số 0)",
    actual: "Hiển thị '0008'",
    repro: () => {
      resetCalculator();
      inputDigit('0');
      inputDigit('0');
      inputDigit('0');
      inputDigit('8');
      updateDisplay();
    }
  },
  {
    id: "BUG-07",
    severity: "Medium",
    title: "Tràn giao diện màn hình khi nhập quá nhiều chữ số",
    desc: "Không giới hạn độ dài chuỗi nhập hoặc tự động co kích thước chữ / chuyển sang e-notation, dẫn tới chữ số tràn ra khỏi màn hình.",
    steps: "1. Nhập liên tục 25 chữ số 9",
    expected: "Giới hạn 15 ký tự hoặc chuyển dạng 9.999e+24, không vỡ layout",
    actual: "Chữ số tràn vỡ khung giao diện",
    repro: () => {
      resetCalculator();
      for (let i = 0; i < 25; i++) inputDigit('9');
      updateDisplay();
    }
  },
  {
    id: "BUG-08",
    severity: "Medium",
    title: "Nút Backspace (⌫) xóa hết số để lại chuỗi rỗng rác",
    desc: "Khi chỉ còn 1 chữ số, nhấn Backspace biến currentInput thành chuỗi rỗng rỗng '' thay vì quay về '0', gây lỗi ở thao tác kế tiếp.",
    steps: "1. Khi màn hình là '5', nhấn '⌫' -> 2. Nhấn '+' -> 3. Nhấn '2'",
    expected: "Màn hình chuyển về '0' sau khi xóa",
    actual: "Màn hình trống rỗng, tính toán tiếp sinh ra lỗi NaN",
    repro: () => {
      resetCalculator();
      inputDigit('5');
      backspace();
      updateDisplay();
    }
  },
  {
    id: "BUG-09",
    severity: "Major",
    title: "Nhấn liên tiếp các toán tử gây nối chuỗi toán tử lỗi",
    desc: "Khi nhấn 5 rồi nhấn '+', sau đó đổi ý nhấn '×', hệ thống không thay thế toán tử mà ghi nhận lỗi hoặc biểu thức hỏng.",
    steps: "1. Nhập '5' -> 2. Nhấn '+' -> 3. Nhấn '×' -> 4. Nhập '2' -> 5. Nhấn '='",
    expected: "Toán tử '×' thay thế '+', kết quả 5 × 2 = 10",
    actual: "Bị tính toán sai hoặc màn hình expression bị lỗi '5 + ×'",
    repro: () => {
      runCalculationSequence(['5', '+', '×', '2', '=']);
    }
  },
  {
    id: "BUG-10",
    severity: "Major",
    title: "Lỗi tính phần trăm (%) trong phép cộng/trừ",
    desc: "Biểu thức '100 + 10%' trong máy tính thông thường phải bằng 110 (100 + 10% của 100), nhưng hệ thống tính 10% = 0.1 -> ra 100.1.",
    steps: "1. Nhập '100' -> 2. Nhấn '+' -> 3. Nhập '10' -> 4. Nhấn '%' -> 5. Nhấn '='",
    expected: "110",
    actual: "100.1",
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
    id: "BUG-11",
    severity: "Medium",
    title: "Nút 'C' (Clear Entry) xóa luôn bộ nhớ tạm Memory",
    desc: "Nút C chỉ được phép xóa giá trị đang nhập hiện tại, nhưng code lại reset luôn cả memoryValue = 0.",
    steps: "1. Nhập '50' -> 2. Nhấn 'MS' -> 3. Nhập '99' -> 4. Nhấn 'C' -> 5. Nhấn 'MR'",
    expected: "MR phải gọi lại được 50",
    actual: "MR trả về 0 vì bộ nhớ đã bị nút C xóa mất",
    repro: () => {
      resetCalculator();
      inputDigit('5'); inputDigit('0');
      memoryStore();
      inputDigit('9'); inputDigit('9');
      clearEntry(); // BUG: wipes memory
      memoryRecall();
      updateDisplay();
    }
  },
  {
    id: "BUG-12",
    severity: "Major",
    title: "Nút 'M-' (Memory Subtract) tính ngược thành cộng dồn",
    desc: "Logic của nút M- bị lập trình viên viết nhầm dấu thành '+=' thay vì '-='.",
    steps: "1. Nhập '100' -> 2. Nhấn 'MS' (Memory = 100) -> 3. Nhập '30' -> 4. Nhấn 'M-' -> 5. Nhấn 'MR'",
    expected: "MR = 70 (100 - 30)",
    actual: "MR = 130 (bị cộng thêm 30)",
    repro: () => {
      resetCalculator();
      inputDigit('1'); inputDigit('0'); inputDigit('0');
      memoryStore();
      inputDigit('3'); inputDigit('0');
      memorySubtract(); // BUG: adds instead of subtracts
      memoryRecall();
      updateDisplay();
    }
  },
  {
    id: "BUG-13",
    severity: "Minor",
    title: "Đổi dấu số 0 biến thành '-0'",
    desc: "Nhấn nút '±' khi màn hình là số 0 tạo ra giá trị '-0' gây sai lệch kiểm thử giá trị ranh giới.",
    steps: "1. Màn hình đang là '0' -> 2. Nhấn '±'",
    expected: "Vẫn là '0'",
    actual: "Hiển thị '-0'",
    repro: () => {
      resetCalculator();
      toggleSign(); // BUG: turns 0 into -0
      updateDisplay();
    }
  },
  {
    id: "BUG-14",
    severity: "Medium",
    title: "Nhấn phím '=' lần 2 bị reset kết quả về 0",
    desc: "Máy tính chuẩn khi nhấn '=' liên tục sẽ lặp lại phép tính cuối (VD: 5 + 2 = 7 = 9 = 11). Ứng dụng này nhấn '=' lần 2 sẽ xóa hoặc về 0.",
    steps: "1. Nhập '5' -> 2. Nhấn '+' -> 3. Nhập '2' -> 4. Nhấn '=' (ra 7) -> 5. Nhấn '=' lần nữa",
    expected: "9 (tiếp tục cộng 2)",
    actual: "Màn hình chuyển về '0'",
    repro: () => {
      runCalculationSequence(['5', '+', '2', '=', '=']);
    }
  },
  {
    id: "BUG-15",
    severity: "Major",
    title: "Xóa lịch sử (Clear History) bị rò rỉ dữ liệu (Memory Leak)",
    desc: "Nút 'Xóa lịch sử' chỉ xóa các thẻ HTML trên giao diện nhưng không xóa mảng historyData trong code; khi thực hiện phép tính mới, các mục cũ bị phục hồi lại.",
    steps: "1. Thực hiện phép tính 1+1=2 -> 2. Bấm 'Xóa lịch sử' (danh sách trống) -> 3. Thực hiện phép tính 2+2=4",
    expected: "Lịch sử chỉ chứa duy nhất phép tính 2+2=4",
    actual: "Phép tính 1+1=2 cũ xuất hiện trở lại cùng với 2+2=4",
    repro: () => {
      runCalculationSequence(['1', '+', '1', '=']);
      clearHistory();
      setTimeout(() => {
        runCalculationSequence(['2', '+', '2', '=']);
      }, 400);
    }
  }
];

// ==========================================
// 2. DOM ELEMENTS
// ==========================================
const currentDisplayEl = document.getElementById('currentDisplay');
const historyDisplayEl = document.getElementById('historyDisplay');
const memIndicatorEl = document.getElementById('memIndicator');
const historyListEl = document.getElementById('historyList');
const statCountEl = document.getElementById('statCount');
const statMemoryEl = document.getElementById('statMemory');

// Modals
const qaDrawerEl = document.getElementById('qaDrawer');
const docsModalEl = document.getElementById('docsModal');
const btnToggleQAMode = document.getElementById('btnToggleQAMode');
const btnDocsModal = document.getElementById('btnDocsModal');
const btnCloseQA = document.getElementById('btnCloseQA');
const btnCloseDocs = document.getElementById('btnCloseDocs');
const bugsListContainer = document.getElementById('bugsListContainer');

// ==========================================
// 3. CORE CALCULATOR LOGIC (WITH INTENTIONAL BUGS)
// ==========================================

function updateDisplay() {
  currentDisplayEl.textContent = state.currentInput;
  if (state.operation && state.previousInput !== '') {
    historyDisplayEl.textContent = `${state.previousInput} ${state.operation}`;
  } else {
    historyDisplayEl.textContent = '';
  }

  // Memory indicator
  if (state.memoryValue !== 0) {
    memIndicatorEl.classList.remove('hidden');
  } else {
    memIndicatorEl.classList.add('hidden');
  }

  statMemoryEl.textContent = state.memoryValue;
}

function inputDigit(digit) {
  if (state.waitingForSecondOperand) {
    state.currentInput = digit;
    state.waitingForSecondOperand = false;
  } else {
    // BUG-06: Allows multiple leading zeros if not properly handled
    // If current is '0' and typing '0', it could become '00' or typing '0008'
    if (state.currentInput === '0' && digit === '0') {
      state.currentInput = '00'; // BUG-06 demonstration
    } else if (state.currentInput === '00' && digit !== '0') {
      state.currentInput = state.currentInput + digit; // results in 008
    } else if (state.currentInput === '0' && digit !== '0') {
      state.currentInput = digit;
    } else {
      // BUG-07: No max length guard, overflows screen freely
      state.currentInput = state.currentInput + digit;
    }
  }
}

function inputDecimal() {
  // BUG-02: Flawed decimal check allows multiple dots
  // If state is waiting for second operand, start fresh
  if (state.waitingForSecondOperand) {
    state.currentInput = '0.';
    state.waitingForSecondOperand = false;
    return;
  }

  // Intentional Bug #2: Only checks if the last character is a dot,
  // allowing strings like '12.3.4'
  if (state.currentInput.endsWith('.')) {
    return;
  }
  state.currentInput += '.';
}

function handleOperator(nextOp) {
  const inputValue = parseFloat(state.currentInput);

  if (state.operation && state.waitingForSecondOperand) {
    // BUG-09: Instead of smoothly replacing the operator,
    // it appends or messes with previous expression
    state.operation = state.operation + ' ' + nextOp; // Concat bug!
    updateDisplay();
    return;
  }

  if (state.previousInput === '') {
    state.previousInput = state.currentInput;
  } else if (state.operation) {
    // BUG-04: Immediate sequential calculation without operator precedence
    const result = performRawCalculation(state.operation, parseFloat(state.previousInput), inputValue);
    state.currentInput = `${result}`;
    state.previousInput = `${result}`;
  }

  state.waitingForSecondOperand = true;
  state.operation = nextOp;
}

function performRawCalculation(op, firstVal, secondVal) {
  // Normalize operator if broken by BUG-09
  if (op.includes(' ')) {
    op = op.split(' ').pop();
  }

  switch (op) {
    case '+':
      // BUG-01: Raw IEEE 754 addition without rounding
      return firstVal + secondVal;
    case '-':
    case '−':
      return firstVal - secondVal;
    case '×':
    case '*':
      return firstVal * secondVal;
    case '÷':
    case '/':
      // BUG-03: Division by zero returns Infinity
      if (secondVal === 0) {
        return Infinity; // BUG: Not throwing error or showing "Cannot divide by 0"
      }
      return firstVal / secondVal;
    default:
      return secondVal;
  }
}

function calculate() {
  let firstVal = parseFloat(state.previousInput);
  let secondVal = parseFloat(state.currentInput);

  // BUG-14: Pressing '=' when no operation resets display to '0'
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

  addHistory(expression, rawResult);
}

function backspace() {
  // BUG-08: When length is 1 or '0', leaves empty string '' instead of '0'
  if (state.currentInput.length <= 1) {
    state.currentInput = ''; // BUG-08: Empty string!
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
}

function clearEntry() {
  state.currentInput = '0';
  // BUG-11: Clearing entry accidentally wipes Memory!
  state.memoryValue = 0;
}

function toggleSign() {
  // BUG-13: Toggling sign on '0' results in '-0'
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
  // BUG-05: Negative square root outputs NaN without error message
  const result = Math.sqrt(val);
  state.currentInput = `${result}`;
  state.waitingForSecondOperand = true;
}

function calcSquare() {
  const val = parseFloat(state.currentInput);
  state.currentInput = `${val * val}`;
  state.waitingForSecondOperand = true;
}

function calcPercent() {
  const val = parseFloat(state.currentInput);
  // BUG-10: In standard arithmetic, 100 + 10% should be 100 + (100 * 0.1) = 110.
  // Here it strictly divides by 100 without multiplying by previous base!
  state.currentInput = `${val / 100}`;
}

// Memory Operations
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
  // BUG-12: M- adds instead of subtracts!
  state.memoryValue += parseFloat(state.currentInput) || 0; // BUG: Written as += instead of -=
  state.waitingForSecondOperand = true;
  updateDisplay();
}

function memoryStore() {
  state.memoryValue = parseFloat(state.currentInput) || 0;
  state.waitingForSecondOperand = true;
  updateDisplay();
}

// History & Statistics
function addHistory(expression, result) {
  const item = {
    id: Date.now(),
    expression,
    result,
    time: new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
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

    // Click history to restore result
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
  // BUG-15: Empties DOM list but leaks data by failing to clear state.historyData = []
  historyListEl.innerHTML = `
    <div class="empty-state">
      <p>Chưa có phép tính nào được thực hiện.</p>
      <small>Lịch sử đã xóa.</small>
    </div>
  `;
  // state.historyData = []; // <--- INTENTIONALLY COMMENTED OUT TO INTRODUCE BUG-15
}

function resetCalculator() {
  clearAll();
  updateDisplay();
}

// ==========================================
// 4. AUTOMATED REPRODUCTION HELPER FOR QA
// ==========================================
function runCalculationSequence(keys) {
  resetCalculator();
  let delay = 0;
  keys.forEach((key, idx) => {
    setTimeout(() => {
      simulateKey(key);
      updateDisplay();
    }, idx * 150);
  });
}

function simulateKey(key) {
  if (!isNaN(key)) {
    inputDigit(key);
  } else if (key === '.') {
    inputDecimal();
  } else if (['+', '-', '−', '×', '*', '÷', '/'].includes(key)) {
    handleOperator(key);
  } else if (key === '=') {
    calculate();
  }
}

// ==========================================
// 5. EVENT LISTENERS
// ==========================================
document.querySelector('.calc-keypad').addEventListener('click', (e) => {
  const btn = e.target.closest('button');
  if (!btn) return;

  const action = btn.dataset.action;
  const val = btn.dataset.val;

  switch (action) {
    case 'number':
      inputDigit(val);
      break;
    case 'decimal':
      inputDecimal();
      break;
    case 'operator':
      handleOperator(val);
      break;
    case 'calculate':
      calculate();
      break;
    case 'clear-all':
      clearAll();
      break;
    case 'clear-entry':
      clearEntry();
      break;
    case 'backspace':
      backspace();
      break;
    case 'toggle-sign':
      toggleSign();
      break;
    case 'sqrt':
      calcSquareRoot();
      break;
    case 'square':
      calcSquare();
      break;
    case 'percent':
      calcPercent();
      break;
    case 'mc':
      memoryClear();
      break;
    case 'mr':
      memoryRecall();
      break;
    case 'm-plus':
      memoryAdd();
      break;
    case 'm-minus':
      memorySubtract();
      break;
    case 'ms':
      memoryStore();
      break;
  }

  updateDisplay();
});

// Physical Keyboard Support
window.addEventListener('keydown', (e) => {
  if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

  if (!isNaN(e.key)) {
    inputDigit(e.key);
  } else if (e.key === '.') {
    inputDecimal();
  } else if (e.key === '+' || e.key === '-') {
    handleOperator(e.key);
  } else if (e.key === '*') {
    handleOperator('×');
  } else if (e.key === '/') {
    e.preventDefault();
    handleOperator('÷');
  } else if (e.key === 'Enter' || e.key === '=') {
    e.preventDefault();
    calculate();
  } else if (e.key === 'Backspace') {
    backspace();
  } else if (e.key === 'Escape') {
    clearAll();
  }
  updateDisplay();
});

document.getElementById('btnClearHistory').addEventListener('click', clearHistory);

// ==========================================
// 6. QA INSPECTOR & MODALS LOGIC
// ==========================================
function renderBugsCatalog(filter = 'all') {
  const filtered = filter === 'all' 
    ? BUGS_CATALOG 
    : BUGS_CATALOG.filter(b => b.severity.toLowerCase() === filter.toLowerCase());

  bugsListContainer.innerHTML = filtered.map(bug => `
    <div class="bug-card">
      <div class="bug-card-top">
        <div class="bug-id-title">
          <span class="bug-id">${bug.id}</span>
          <span class="bug-title">${bug.title}</span>
        </div>
        <span class="severity-tag sev-${bug.severity}">${bug.severity}</span>
      </div>
      <p class="bug-desc">${bug.desc}</p>
      <div class="bug-repro">
        <strong>Các bước tái hiện (Steps):</strong> ${bug.steps}<br>
        <strong>Kỳ vọng (Expected):</strong> ${bug.expected} | <strong>Thực tế (Actual):</strong> ${bug.actual}
      </div>
      <button class="btn-trigger-bug" data-bug-id="${bug.id}">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polygon points="5 3 19 12 5 21 5 3"></polygon>
        </svg>
        Tự động tái hiện lỗi này (Auto-reproduce)
      </button>
    </div>
  `).join('');

  // Attach reproduce buttons
  bugsListContainer.querySelectorAll('.btn-trigger-bug').forEach(btn => {
    btn.addEventListener('click', () => {
      const bugId = btn.dataset.bugId;
      const targetBug = BUGS_CATALOG.find(b => b.id === bugId);
      if (targetBug && targetBug.repro) {
        qaDrawerEl.classList.add('hidden');
        targetBug.repro();
      }
    });
  });
}

// QA Drawer Open/Close
btnToggleQAMode.addEventListener('click', () => {
  renderBugsCatalog('all');
  qaDrawerEl.classList.remove('hidden');
});

btnCloseQA.addEventListener('click', () => {
  qaDrawerEl.classList.add('hidden');
});

// QA Filter Buttons
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderBugsCatalog(btn.dataset.filter);
  });
});

// Docs Modal Open/Close & Tabs
btnDocsModal.addEventListener('click', () => {
  docsModalEl.classList.remove('hidden');
});

btnCloseDocs.addEventListener('click', () => {
  docsModalEl.classList.add('hidden');
});

document.querySelectorAll('.tab-btn').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(tab.dataset.tab).classList.add('active');
  });
});

// Close modal when clicking outside
window.addEventListener('click', (e) => {
  if (e.target === qaDrawerEl) qaDrawerEl.classList.add('hidden');
  if (e.target === docsModalEl) docsModalEl.classList.add('hidden');
});

// Initial boot
resetCalculator();
renderBugsCatalog();
