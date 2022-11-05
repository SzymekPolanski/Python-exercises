import sys
sys.path.append(r"..")
import pytest
from programs.fraction_fuel_to_percent import convert
from programs.fraction_fuel_to_percent import gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"


def test_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("cat/dog")
