from main import Number

def test_inc_zero():
    assert Number.inc(0) == 1

def test_inc_negative():
    assert Number.inc(-1) == 0

def test_inc_large_number():
    assert Number.inc(999999) == 1000000

def test_inc_float():
    assert Number.inc(3.5) == 4.5
