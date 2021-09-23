from Figure import Figure
from Square import Square
import math


class Triangle(Figure):
    _name = 'Треугольник'

    def __init__(self, side1, side2, side3):
        try:
            self.side1 = float(side1)
            self.side2 = float(side2)
            self.side3 = float(side3)
        except Exception as e:
            print("Длинами сторон треугольника могут быть только положительные числа!!!")
            raise e
        if self.is_triangle() != "Yes":
            return None  # Таким образом вернуть None не получается, нужен другой способ

    def get_triangle_sides(self):
        """
        Функция возвращает значение сторон треугольника
        :return:
        """
        # print(f"Стороны треугольника =  {self.side1}, {self.side2}, {self.side3}")
        return self.side1, self.side2, self.side3

    @property
    def area(self):
        """
        Функция вычисляет площадь треугольника по формуле Герона.
        Сначала необходимо подсчитать разность полупериметра и каждой его стороны. Потом найти произведение полученных
        чисел, умножить результат на полупериметр и найти корень из полученного числа.
        S = √ p * (p − a) * (p − b) * (p − c), где a, b, c — стороны, p — полупериметр, который можно найти по формуле:
        p = (a + b + c) / 2

        :return: Площадь треугольника (float)
        """
        if self.is_triangle() == "Yes":
            halfperimetr = self.perimetr / 2
            return math.sqrt(
                halfperimetr * (halfperimetr - self.side1) * (halfperimetr - self.side2) * (halfperimetr - self.side3))
        elif self.is_triangle() == "No":
            return None
        else:
            raise ValueError

    @property
    def perimetr(self):
        """
        Функция вычисляет периметр треугольника по формуле S = a + b + c
        :return:
        """
        return self.side1 + self.side2 + self.side3

    # Данная функция сейчас никак не используется
    def is_triangle_sides_available(self):
        """
        Функция проверяет все ли стороны треугольника заданы
        :return:
        """
        flag = 0
        if not self.side1:
            print(f"У треугольника не задана сторона 1")
            flag += 1
        if not self.side2:
            print(f"У треугольника не задана сторона 2")
            flag += 1
        if not self.side3:
            print(f"У треугольника не задана сторона 3")
            flag += 1
        if flag != 0:
            print(f"Треугольник создать нельзя так как не задано {flag} стороны")
            return None
        else:
            return self.get_triangle_sides()

    def is_triangle(self):
        """
        Функция проверяет является ли фигура треугольником по формуле: сумма длин 2х строн должна быть больше третьей

        :return: Yes, No (str)
        """
        # Убрать проверку 'if self.is_triangle_sides_available() != None'
        if self.is_triangle_sides_available() != None and (self.side1 + self.side2 > self.side3) and (
                self.side1 + self.side3 > self.side2) and (
                self.side2 + self.side3 > self.side1):
            # print(f"Треугольник со сторонами {self.get_triangle_sides()} существует")
            return "Yes"
        else:
            # print(f"Треугольник со сторонами {self.get_triangle_sides()} не существует")
            return "No"


if __name__ == "__main__":
    # side1 = input("Введите длинну 1ой стороны треугольника: ")
    # side2 = input("Введите длинну 2ой стороны треугольника: ")
    # side3 = input("Введите длинну 3ой стороны треугольника: ")

    # triangle = Triangle(side1, side2, side3)
    # triangle = Triangle(13, 14, 15)
    triangle = Triangle(13, 14, 15)
    if triangle is None:
        print('None')
    else:
        print('Not None')

    # triangle.is_triangle()

    print("Имя фигуры = {}".format(triangle.get_name()))
    print("Периметр {}а = {}".format(triangle.get_name(), triangle.perimetr))
    print("Площадь {}а = {}".format(triangle.get_name(), triangle.area))

    square = Square(10)
    print("Имя фигуры = {}".format(square.get_name()))
    print("Периметр {}а = {}".format(square.get_name(), square.perimetr))
    print("Площадь {}а = {}".format(square.get_name(), square.area))

    # print(f"Сумма площадей {triangle.get_name()} + {square.get_name()} = {triangle + square}")
    print(f"Сумма площадей {triangle.get_name()} + {square.get_name()} = {triangle.add_area(square)}")
