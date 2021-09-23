import pytest


def devision(a, b):
    # raise Exception
    return a / b


def test_devision_1():
    assert devision(10, 5) == 2


def test_devision_2():
    assert False


def test_devision_3():
    assert 1 > 4


def test_devision_4():
    assert True


def test_devision_5():
    with pytest.raises(ZeroDivisionError):
        devision(5, 5)
