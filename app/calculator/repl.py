"""REPL interface (testable via process_line)."""
from __future__ import annotations
from typing import Tuple, Optional, List
from app.calculation.calculation import History
from app.calculation.factory import CalculationFactory, parse_operands, normalize_token

_HELP_TEXT = """\
Commands:
  add|+ NUM [NUM ...]         add numbers
  subtract|- A B              subtract B from A
  multiply|* NUM [NUM ...]    multiply numbers
  divide|/ A B                divide A by B

  history                     show previous calculations
  help                        show this help
  exit                        quit the program
"""

def format_calc(calc) -> str:
    ops = " ".join(str(x).rstrip("0").rstrip(".") if float(x).is_integer() else str(x) for x in calc.operands)
    return f"{calc.operation_name} {ops} = {calc.result()}"

def process_line(line: str, history: History) -> Tuple[Optional[str], bool]:
    if not line.strip():
        return None, False
    parts: List[str] = line.strip().split()
    cmd = normalize_token(parts[0])

    if cmd in {"help", "?"}:
        return _HELP_TEXT, False
    if cmd == "history":
        if not list(history):
            return "(no history)", False
        return "\n".join(format_calc(c) for c in history), False
    if cmd in {"exit", "quit"}:
        return "Goodbye!", True

    # Treat as operation
    try:
        operands = parse_operands(parts[1:])
        calc = CalculationFactory.create(cmd, operands)
        history.add(calc)
        return format_calc(calc), False
    except Exception as exc:  # EAFP: catch-and-report
        return f"Error: {exc}", False

def run_repl(stdin=None, stdout=None) -> None:  # pragma: no cover
    import sys
    inp = stdin or sys.stdin
    out = stdout or sys.stdout
    history = History()
    print("Calculator CLI. Type 'help' for instructions.", file=out)
    while True:
        out.write("> "); out.flush()
        line = inp.readline()
        if not line:
            break
        output, should_exit = process_line(line, history)
        if output:
            print(output, file=out)
        if should_exit:
            break
