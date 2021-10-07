"""Тесты на класс Triangle."""
import pytest

from src.triangle import Triangle
from src.figure import Figure


def test_triangle_create_instance(create_triangle):
    """Проверяем, что объект создается и является экземпляром классов 'Triangle', 'Figure'."""

    assert isinstance(create_triangle, (Triangle, Figure))


@pytest.mark.parametrize("side", [(1, 2, 3), (100, 50, 200), (1.1, 2.22, 3.3333)])
def test_triangle_is_not_exist(side):
    """Проверяем, что если треугольник создать нельзя, то возвращается 'None'."""

    triangle = Triangle(side[0], side[1], side[2])
    assert triangle is None


def test_triangle_has_attr_name(create_triangle):
    """Проверяем, что у фигуры есть имя и это имя 'Треугольник'."""

    assert create_triangle.get_name() == 'Треугольник'


def test_triangle_has_attr_area(create_triangle):
    """Проверяем, что у треугольника есть атрибут 'area' - площадь."""

    assert create_triangle.area


def test_triangle_has_attr_perimeter(create_triangle):
    """Проверяем, что у треугольника есть атрибут 'perimeter' - периметр."""

    assert create_triangle.perimeter


def test_triangle_has_sides(create_triangle):
    """Проверяем, что у треугольника есть стороны после создания объекта."""

    assert create_triangle.sides == (13, 14, 15)


@pytest.mark.parametrize("side,expected_area", [((13, 14, 15), 84),
                                                ((2.1, 3.1, 4.1), 3.179389681998735),
                                                ((10.1, 12, 20.588), 41.17424432078754)])
def test_triangle_check_area_calculating(side, expected_area):
    """Проверяем, что площадь треугольника считается корректно."""

    triangle = Triangle(side[0], side[1], side[2])
    assert triangle.area == expected_area


@pytest.mark.parametrize("side,expected_perimeter", [((13, 14, 15), 42), ((2.1, 3.1, 4.1), 9.3),
                                                     ((10.1, 12, 20.588), 42.688)])
def test_triangle_check_perimeter_calculation(side, expected_perimeter):
    """Проверяем, что периметр треугольника считается корректно"""

    triangle = Triangle(side[0], side[1], side[2])
    assert triangle.perimeter == expected_perimeter


def test_triangle_add_area_square(create_triangle, create_square, create_circle, create_rectangle):
    """
    Проверяем, что к площади треугольника можно прибавить площадь другой геометрической фигуры
    ('Trinangle, 'Square', 'Circle', 'Rectangle').
    """

    triangle2 = Triangle(13, 14, 15)
    assert create_triangle.add_area(triangle2) == create_triangle.area + triangle2.area
    assert create_triangle.add_area(create_square) == create_triangle.area + create_square.area
    assert create_triangle.add_area(create_circle) == create_triangle.area + create_circle.area
    assert create_triangle.add_area(create_rectangle) == create_triangle.area + \
           create_rectangle.area


def test_triangle_add_area_negative(create_triangle):
    """Проверяем, что нельзя складывать площади не геометрических фигур."""

    class Car:
        pass

    with pytest.raises(ValueError):
        create_triangle.add_area(Car())


def test_triangle_add_area_negative1(create_triangle, create_incorrect_triangle):
    """Проверяем, что нельзя складывать с не треугольником."""

    with pytest.raises(ValueError):
        create_triangle.add_area(create_incorrect_triangle)
