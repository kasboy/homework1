"""Тесты на класс Circle."""
import pytest

from src.circle import Circle
from src.figure import Figure


def test_circle_create_instance(create_circle):
    """ Проверяем, что объект создается и является экземпляром классов 'Circle', 'Figure'. """

    assert isinstance(create_circle, (Circle, Figure))


def test_circle_has_attr_name(create_circle):
    """ Проверяем, что у фигуры есть имя и это имя 'Круг'. """

    assert create_circle.get_name() == 'Круг'


def test_circle_has_attr_area(create_circle):
    """ Проверяем, что у круга есть атрибут 'area' - площадь. """

    assert create_circle.area


def test_circle_has_attr_perimeter(create_circle):
    """ Проверяем, что у круга есть атрибут 'perimeter' - периметр. """

    assert create_circle.perimeter


def test_circle_has_sides(create_circle):
    """ Проверяем, что у круга есть радиус после создания объекта. """

    assert create_circle.radius == 5


@pytest.mark.parametrize("radius,expected_area", [(13, 530.929158456675), (2.1, 13.854423602330987),
                                                  (20.588, 1331.6135074587721),
                                                  (0.25, 0.19634954084936207)])
def test_circle_check_area_calculating(radius, expected_area):
    """ Проверяем, что площадь круга считается корректно. """

    circle = Circle(radius)
    assert circle.area == expected_area


@pytest.mark.parametrize("radius,expected_perimeter", [(13, 81.68140899333463),
                                                       (2.1, 13.194689145077131),
                                                       (20.588, 129.35821910421333)])
def test_circle_check_perimeter_calculation(radius, expected_perimeter):
    """ Проверяем, что периметр круга считается корректно. """

    circle = Circle(radius)
    assert circle.perimeter == expected_perimeter


def test_circle_add_area_square(create_circle, create_square, create_triangle, create_rectangle):
    """ Проверяем, что к площади круга можно прибавить площадь другой геометрической фигуры
    (Circle', 'Square', 'Trinangle', 'Rectangle'). """

    circle2 = Circle(13)
    assert create_circle.add_area(circle2) == create_circle.area + circle2.area
    assert create_circle.add_area(create_square) == create_circle.area + create_square.area
    assert create_circle.add_area(create_triangle) == create_circle.area + create_triangle.area
    assert create_circle.add_area(create_rectangle) == create_circle.area + create_rectangle.area


def test_circle_add_area_negative(create_circle):
    """ Проверяем, что нельзя складывать площади не геометрических фигур. """

    class Car:
        pass

    with pytest.raises(ValueError):
        create_circle.add_area(Car())

    with pytest.raises(ValueError):
        create_circle.add_area(1)


def test_circle_add_area_negative1(create_circle, create_incorrect_triangle):
    """ Проверяем, что нельзя складывать с не треугольником. """

    with pytest.raises(ValueError):
        create_circle.add_area(create_incorrect_triangle)
