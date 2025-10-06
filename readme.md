# 🧮 CLI Calculator (Python)
![CI](https://github.com/AnvithAnvi/cli-calculator/actions/workflows/python-app.yml/badge.svg)

A **professional-grade, modular command-line calculator** built in Python.  
Includes a clean architecture, comprehensive error handling, **100 % test coverage**, and a full **GitHub Actions CI** workflow.

---

## 🚀 Features
- **REPL** (Read-Eval-Print-Loop) for continuous user interaction  
- Arithmetic operations: `add`, `subtract`, `multiply`, `divide`  
- Commands: `help`, `history`, `exit`  
- Input validation and clear feedback  
- Error handling using both **LBYL** (Look Before You Leap) and **EAFP** (Easier to Ask Forgiveness than Permission)  
- Modular, DRY, and well-documented code  
- Full unit-test suite with **100 % coverage enforcement**

---

## 📁 Project Structure
```
cli-calculator/
├── app/
│   ├── calculator/
│   │   ├── repl.py
│   │   └── __init__.py
│   ├── calculation/
│   │   ├── calculation.py
│   │   ├── factory.py
│   │   └── __init__.py
│   ├── operation/
│   │   ├── operations.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── test_calculations.py
│   ├── test_operations.py
│   └── test_repl.py
├── .github/workflows/python-app.yml
├── pyproject.toml
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone and open the project
```bash
git clone https://github.com/<your-username>/cli-calculator.git
cd cli-calculator
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
```

### 3️⃣ Install dependencies
```bash
python -m pip install --upgrade pip
pip install -e .
pip install pytest pytest-cov
```

---

## ▶️ Run the Calculator
```bash
python -m app.main
```

### Example Session
```
Calculator CLI. Type 'help' for instructions.
> add 2 3
add 2 3 = 5.0
> divide 10 2
divide 10 2 = 5.0
> history
add 2 3 = 5.0
divide 10 2 = 5.0
> exit
Goodbye!
```

---

## 🧪 Run Tests
```bash
pytest --cov=app tests/
coverage report --fail-under=100
```
✅ All tests pass  
✅ Coverage: **100 %**

---

## 🤖 Continuous Integration (CI)

GitHub Actions workflow at `.github/workflows/python-app.yml` automatically:
1. Installs dependencies  
2. Runs tests with coverage  
3. Fails the build if coverage < 100 %

---

## 🧱 Architecture Overview
| Layer | Description |
|-------|--------------|
| **Operation** | Low-level arithmetic (`add`, `subtract`, `multiply`, `divide`) |
| **Calculation** | Immutable `Calculation` objects & session `History` |
| **Factory** | Parses user input & builds `Calculation` instances |
| **REPL** | Command-line interface with commands and help |
| **Tests** | Pytest suites ensuring 100 % branch & line coverage |

---

## 🧩 Technologies
- Python 3.9 +
- `pytest`, `pytest-cov`
- GitHub Actions CI
- Editable install via `pyproject.toml`


> _“Clean code is simple, direct, and tested.”_
