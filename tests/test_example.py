import pytest

from math import pi
from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square


# Тесты на класс Circle
def test_circle_create_instance(create_circle):
    assert isinstance(create_circle, (Circle, Figure))


def test_circle_has_attr_radius(create_circle):
    assert create_circle.radius == 5


@pytest.mark.parametrize("amount", [0, 10, 9999.21, 0.01])
def test_circle_has_attr_radius(amount):
    circle = Circle(amount)
    assert circle.radius == amount


def test_circle_has_attr_area(create_circle):
    assert create_circle.area == pi * 5 ** 3


def test_circle_has_attr_name(create_circle):
    assert create_circle.get_name() == 'Круг'


def test_circle_has_attr_perimeter(create_circle):
    assert create_circle.perimeter == 2 * pi * 5


def test_circle_add_area_square(create_circle, create_square):
    assert create_circle.add_area(create_square) == create_circle.area + create_square.area


def test_circle_add_area_negative(create_circle):
    """Can't sum other classes"""

    class Car:
        pass

    with pytest.raises(ValueError):
        create_circle.add_area(Car())


# Тесты на класс Figure
def test_figure_create_instance():
    # Проверяем, что при попытке создать экземпляр класса 'Figure' возникает исключение
    with pytest.raises(Exception):
        figure = Figure()


# Тесты на класс Square
def test_square_create_instance(create_square):
    assert isinstance(create_square, (Figure, Square))


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
