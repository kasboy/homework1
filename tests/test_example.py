import pytest
from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle

circle = Circle(5)

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
