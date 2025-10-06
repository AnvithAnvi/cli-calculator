from app.calculator.repl import process_line
from app.calculation.calculation import History

def run(line, history=None):
    history = history or History()
    out, exit_ = process_line(line, history)
    return out, exit_, history

def test_help():
    out, exit_, _ = run("help")
    assert "Commands" in out and not exit_

def test_add_and_history():
    h = History()
    out, exit_, h = run("add 1 2 3", h)
    assert "add 1 2 3 = 6.0" in out and not exit_
    out, exit_, _ = run("history", h)
    assert "add 1 2 3 = 6.0" in out

def test_subtract_and_divide():
    h = History()
    out, _, _ = run("subtract 10 3", h)
    assert "subtract 10 3 = 7.0" in out
    out, _, _ = run("divide 10 2", h)
    assert "divide 10 2 = 5.0" in out

def test_errors():
    out, _, _ = run("divide 1 0")
    assert out.startswith("Error:")
    out, _, _ = run("add a b")
    assert out.startswith("Error:")

def test_exit():
    out, exit_, _ = run("exit")
    assert exit_ and "Goodbye" in out

# NEW: cover blank line branch
def test_blank_line_is_ignored():
    out, exit_ = process_line("   ", History())
    assert out is None and exit_ is False

# NEW: cover 'quit' alias branch
def test_quit_alias_exits():
    out, exit_ = process_line("quit", History())
    assert exit_ is True and "Goodbye" in out

def test_history_when_empty_shows_message():
    from app.calculation.calculation import History
    from app.calculator.repl import process_line
    out, exit_ = process_line("history", History())
    assert "(no history" in out.lower()
    assert exit_ is False
