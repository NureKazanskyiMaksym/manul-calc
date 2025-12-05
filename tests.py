import pytest
import io
from main import ManulCalculator

@pytest.fixture
def calc():
    return ManulCalculator(10)

def test_add(monkeypatch, capsys):
    inputs = iter(["1", "5", "2", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calc = ManulCalculator(10)
    calc.add(5)
    captured = capsys.readouterr()
    assert calc.get_count() == 15
    calc.subtract(3)
    assert calc.get_count() == 12

def test_subtract_negative(calc):
    with pytest.raises(ValueError, match="Cannot have negative manuls."):
        calc.subtract(15)