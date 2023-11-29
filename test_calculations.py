import calculations


def test_add():
    assert calculations.add(5, 5) == 10


def test_multiply():
    assert calculations.multiply(2, 4) == 8


def test_power():
    assert calculations.power(2, 5) == 32
