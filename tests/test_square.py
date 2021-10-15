""" Тесты на класс Square. """

import pytest

from src.square import Square
from src.figure import Figure


def test_square_create_instance(create_square):
    """ Проверяем, что объект создается и является экземпляром классов 'Square', 'Figure'. """

    assert isinstance(create_square, (Square, Figure))


def test_square_has_attr_name(create_square):
    """ Проверяем, что у фигуры есть имя и это имя 'Квадрат'. """

    assert create_square.get_name() == 'Квадрат'


def test_square_has_attr_area(create_square):
    """ Проверяем, что у квадрата есть атрибут 'area' - площадь. """

    assert create_square.area


def test_square_has_attr_perimeter(create_square):
    """ Проверяем, что у квадрата есть атрибут 'perimeter' - периметр. """

    assert create_square.perimeter


def test_square_has_sides(create_square):
    """ Проверяем, что у квадрата есть стороны после создания объекта. """

    assert create_square.sides == 4


@pytest.mark.parametrize("side,expected_area", [(13, 169), (2.1, 4.41),
                                                (20.588, 423.86574400000006), (0.29, 0.0841)])
def test_square_check_area_calculating(side, expected_area):
    """ Проверяем, что площадь квадрата считается корректно. """

    square = Square(side)
    assert square.area == expected_area


@pytest.mark.parametrize("side,expected_perimeter", [(13, 52), (2.1, 8.4),
                                                     (20.588, 82.352), (0.29, 1.16)])
def test_square_check_perimeter_calculation(side, expected_perimeter):
    """ Проверяем, что периметр квадрата считается корректно. """

    square = Square(side)
    assert square.perimeter == expected_perimeter


def test_square_add_area_square(create_square, create_triangle, create_circle, create_rectangle):
    """ Проверяем, что к площади квадрата можно прибавить площадь другой геометрической фигуры
    ('Square', 'Trinangle', 'Circle', 'Rectangle'). """

    square2 = Square(20)
    assert create_square.add_area(square2) == create_square.area + square2.area
    assert create_square.add_area(create_triangle) == create_square.area + create_triangle.area
    assert create_square.add_area(create_circle) == create_square.area + create_circle.area
    assert create_square.add_area(create_rectangle) == create_square.area + create_rectangle.area


def test_square_add_area_negative(create_square):
    """ Проверяем, что нельзя складывать площади не геометрических фигур. """

    class Animal:
        pass

    with pytest.raises(ValueError):
        create_square.add_area(Animal())

    with pytest.raises(ValueError):
        create_square.add_area(1)


def test_square_add_area_negative1(create_square, create_incorrect_triangle):
    """ Проверяем, что нельзя складывать с не треугольником. """

    with pytest.raises(ValueError):
        create_square.add_area(create_incorrect_triangle)
