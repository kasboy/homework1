import pytest
from math import pi
from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


# Тесты на класс Circle
def test_circle_create_instance(create_circle):
    assert isinstance(create_circle, Circle)
    assert isinstance(create_circle, Figure)

def test_circle_has_attr(create_circle):
    assert create_circle.radius == 5
    assert create_circle.area == pi * 5 ** 2
    assert create_circle.get_name() == 'Круг'
    assert create_circle.perimeter == 2 * pi * 5

def test_circle_add_area_square(create_circle, create_square):
    assert create_circle.add_area(create_square) == create_circle.area + create_square.area

# Тесты на класс Figure
def test_figure_create_instance(create_square):
    # Проверяем, что при попытке создать экземпляр класса 'Figure' возникает исключение
    with pytest.raises(Exception):
        figure = Figure()

# Тесты на класс Square
def test_square_create_instance(create_square):
    assert isinstance(create_square, Square)
    assert isinstance(create_square, Figure)

def test_square_has_attr(create_square):
    assert create_square.side == 4
    assert create_square.area == 4 ** 2
    assert create_square.get_name() == 'Квадрат'
    assert create_square.perimeter == 4 * 4

def test_circle_add_area_square(create_circle, create_square):
    assert create_circle.add_area(create_square) == create_circle.area + create_square.area

# def devision(a, b):
#     # raise Exception
#     return a / b
#
# def test_devision_1():
#     assert devision(10, 5) == 2
#
# def test_devision_2():
#     assert False
#
# def test_devision_3():
#     assert 1 > 4
#
# def test_devision_4():
#     assert True
#
# def test_devision_5():
#     with pytest.raises(ZeroDivisionError):
#         devision(5, 5)
