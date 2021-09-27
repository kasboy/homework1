"""
Програма для расчета по ДЗ №1
Версия 1.0
Автор: Андрей Корниенко
"""

from figure import Figure
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle

if __name__ == "__main__":
    triangle = Triangle(13, 14, 15)  # Создаем треугольник

    # Проверяем, что если треугольник создать нельзя, то возврящаетя None
    # triangle = Triangle(1, 2, 6)
    if triangle is None:
        print(f'Triangle is None, type = {type(triangle)}')
    else:
        print(f"Not None, type = {type(triangle)}")

    print("Имя фигуры = {}, {}".format(triangle.get_name(), triangle.figure_params))
    print("Периметр {}а = {}".format(triangle.get_name(), triangle.perimetr))
    print("Площадь {}а = {}\n".format(triangle.get_name(), triangle.area))

    square = Square(10)  # Создаем квадрат
    print("Имя фигуры = {}, {}".format(square.get_name(), square.figure_params))
    print("Периметр {}а = {}".format(square.get_name(), square.perimetr))
    print("Площадь {}а = {}\n".format(square.get_name(), square.area))

    circle = Circle(10)  # Создаем круг
    print("Имя фигуры = {}, {}".format(circle.get_name(), circle.figure_params))
    print("Периметр {}а = {}".format(circle.get_name(), circle.perimetr))
    print("Площадь {}а = {}\n".format(circle.get_name(), circle.area))

    rectangle = Rectangle(4, 5)  # Создаем прямоугольник
    print("Имя фигуры = {}, {}".format(rectangle.get_name(), rectangle.figure_params))
    print("Периметр {}а = {}".format(rectangle.get_name(), rectangle.perimetr))
    print("Площадь {}а = {}\n".format(rectangle.get_name(), rectangle.area))

    # Проверяем сумму площадей cозданных фигур
    print(f"Сумма площадей {triangle.get_name()} + {square.get_name()} = {triangle.add_area(square)}")
    print(f"Сумма площадей {triangle.get_name()} + {circle.get_name()} = {triangle.add_area(circle)}")
    print(f"Сумма площадей {triangle.get_name()} + {rectangle.get_name()} = {triangle.add_area(rectangle)}")
    print(f"Сумма площадей {square.get_name()} + {rectangle.get_name()} = {square.add_area(rectangle)}")

    # Проверяем возможность создать экземпляр класса 'Figure'
    figure = Figure()

