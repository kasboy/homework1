""" Тесты на класс Rectangle. """

import pytest

from src.rectangle import Rectangle
from src.figure import Figure


def test_rectangle_create_instance(create_rectangle):
    """ Проверяем, что объект создается и является экземпляром классов 'Rectangle', 'Figure'. """

    assert isinstance(create_rectangle, (Rectangle, Figure))


def test_rectangle_has_attr_name(create_rectangle):
    """ Проверяем, что у фигуры есть имя и это имя 'Прямоугольник'. """

    assert create_rectangle.get_name() == 'Прямоугольник'


def test_rectangle_has_attr_area(create_rectangle):
    """ Проверяем, что у прямоугольника есть атрибут 'area' - площадь. """

    assert create_rectangle.area


def test_rectangle_has_attr_perimeter(create_rectangle):
    """ Проверяем, что у прямоугольника есть атрибут 'perimeter' - периметр. """

    assert create_rectangle.perimeter


def test_rectangle_has_sides(create_rectangle):
    """ Проверяем, что у прямоугольника есть стороны после создания объекта. """

    assert create_rectangle.sides == (4, 5)


@pytest.mark.parametrize("side,expected_area", [((13, 14), 182), ((2.1, 3.1), 6.510000000000001),
                                                ((20.588, 12), 247.056),
                                                ((0.29, 0.045), 0.013049999999999999)])
def test_rectangle_check_area_calculating(side, expected_area):
    """ Проверяем, что площадь прямоугольника считается корректно. """

    rectangle = Rectangle(side[0], side[1])
    assert rectangle.area == expected_area


@pytest.mark.parametrize("side,expected_perimeter", [((13, 14), 54), ((2.1, 3.1), 10.4),
                                                     ((20.588, 12), 65.176),
                                                     ((0.025, 0.005), 0.060000000000000005)])
def test_rectangle_check_perimeter_calculation(side, expected_perimeter):
    """ Проверяем, что периметр прямоугольника считается корректно. """

    rectangle = Rectangle(side[0], side[1])
    assert rectangle.perimeter == expected_perimeter


def test_rectangle_add_area_square(create_rectangle, create_square, create_circle, create_triangle):
    """ Проверяем, что к площади прямоугольника можно прибавить площадь другой геометрической фигуры
    ('Trinangle, 'Square', 'Circle', 'Rectangle'). """

    rectangle2 = Rectangle(13, 14)
    assert create_rectangle.add_area(rectangle2) == create_rectangle.area + rectangle2.area
    assert create_rectangle.add_area(create_square) == create_rectangle.area + create_square.area
    assert create_rectangle.add_area(create_circle) == create_rectangle.area + create_circle.area
    assert create_rectangle.add_area(create_triangle) == create_rectangle.area + \
           create_triangle.area


def test_rectangle_add_area_negative(create_rectangle):
    """ Проверяем, что нельзя складывать площади не геометрических фигур. """

    class Car:
        pass

    with pytest.raises(ValueError):
        create_rectangle.add_area(Car())

    with pytest.raises(ValueError):
        create_rectangle.add_area(1)


def test_rectangle_add_area_negative1(create_rectangle, create_incorrect_triangle):
    """ Проверяем, что нельзя складывать с не треугольником. """

    with pytest.raises(ValueError):
        create_rectangle.add_area(create_incorrect_triangle)
