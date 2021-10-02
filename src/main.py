"""
Домашня работа №1 "ООП и Pytest на практике"
Версия 1.0
Автор: Андрей Корниенко

Домашнее задание:
ООП и Pytest на практике

Цель:
Научиться писать код в ООП стиле и покрывать его тестами.

Создать базовый класс геометрической фигуры (Figure).
Реализовать классы геометрических фигур Треугольник, Прямоугольник, Квадрат, Круг (Triangle,
Rectangle, Square, Circle).

Каждый класс должен располагаться в отдельном файле с соответствующим названием
(например class Triangle => Triangle.py). Все файлы с классами должны находиться в папке src/ в
корне репозитория. Треугольник должен задаваться тремя сторонами, если треугольник создать нельзя,
то класс должен вернуть None

1 Часть.
Каждая фигура должна иметь атрибуты:
name - название фигуры,
area (вычисляемое!) - площадь,
perimeter (вычисляемое!) - периметр (сумма длин сторон или длину окружности)

Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур
(никакого хардкода значений). Каждая фигура должна реализовать метод add_area(figure) который
должен принимать другую геометрическую фигуру и возвращать сумму площадей этих фигур. Если передана
не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError) и сообщать что передан
неправильный класс.

Опционально (необязательно):
Запретить создавать экземпляры базового класса Figure.

Пример работы с одним из классов фигуры:
square = Square(10) # Так создаем квадрат со стороной 10
square.area
100
triangle = Triangle(13, 14, 15) # Так создаем треугольник со сторонами 13, 14, 15
triangle.area
84
triangle.add_area(square)
184

Часть.
Написать тесты с использованием pytest на эти классы.
Глубину покрытия и объем определить самостоятельно, но минимум проверить реализацию всех указанных
требований для каждого класса. Все тесты должны располагаться в папке tests/ в корне репозитория.

Критерии оценки:
Будет оцениваться глубина использования парадигмы ООП.
Встроенные декораторы, наследование, отсутствие дублирования кода.
Если какой-то метод выполняет одно и тоже во всех классах наследниках, то он должен принадлежать
родительскому классу.
Задание сдавать в формате pull-request.
Соблюдение минимального кодстайла.
Никаих print'ов, закомментированного кода и лишних файлов быть не должно.
"""

from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle

if __name__ == "__main__":
    triangle = Triangle(13, 14, 15)  # Создаем треугольник

    # Проверяем, что если треугольник создать нельзя, то возврящаетя None
    # triangle = Triangle(1, 2, 6)
    if triangle is None:
        print(f'Triangle is None, type = {type(triangle)}')
    else:
        print(f"Not None, type = {type(triangle)}")

    print("Имя фигуры = {}, {}".format(triangle.get_name(), triangle.figure_params))
    print("Периметр {}а = {}".format(triangle.get_name(), triangle.perimeter))
    print("Площадь {}а = {}\n".format(triangle.get_name(), triangle.area))

    square = Square(10)  # Создаем квадрат
    print("Имя фигуры = {}, {}".format(square.get_name(), square.figure_params))
    print("Периметр {}а = {}".format(square.get_name(), square.perimeter))
    print("Площадь {}а = {}\n".format(square.get_name(), square.area))

    circle = Circle(10)  # Создаем круг
    print("Имя фигуры = {}, {}".format(circle.get_name(), circle.figure_params))
    print("Периметр {}а = {}".format(circle.get_name(), circle.perimeter))
    print("Площадь {}а = {}\n".format(circle.get_name(), circle.area))

    rectangle = Rectangle(4, 5)  # Создаем прямоугольник
    print("Имя фигуры = {}, {}".format(rectangle.get_name(), rectangle.figure_params))
    print("Периметр {}а = {}".format(rectangle.get_name(), rectangle.perimeter))
    print("Площадь {}а = {}\n".format(rectangle.get_name(), rectangle.area))

    # Проверяем сумму площадей cозданных фигур
    print(f"Сумма площадей {triangle.get_name()} + {square.get_name()} = "
          f"{triangle.add_area(square)}")
    print(f"Сумма площадей {triangle.get_name()} + {circle.get_name()} = "
          f"{triangle.add_area(circle)}")
    print(f"Сумма площадей {triangle.get_name()} + {rectangle.get_name()} = "
          f"{triangle.add_area(rectangle)}")
    print(f"Сумма площадей {square.get_name()} + {rectangle.get_name()} = "
          f"{square.add_area(rectangle)}")

    # Проверяем возможность создать экземпляр класса 'Figure'
    # figure = Figure()
