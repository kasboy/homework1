import math
from figure import Figure


class Triangle(Figure):
    """
    Класс Треугольник. Конструктор принимает длины 3х сторон треугольника. Если треугольк создать
    нельзя, возвращаетя 'None'.
    """
    _name = 'Треугольник'

    def __init__(self, side1, side2, side3):
        try:  # Проверяем, все ли стороны треугольника заданы как числа
            self.side1 = float(side1)
            self.side2 = float(side2)
            self.side3 = float(side3)
        except Exception as e:
            print("Длинами сторон треугольника могут быть только положительные числа!!!")
            raise e

    @staticmethod
    def __new__(cls, *args):
        """
        Метод проверяет является ли фигура треугольником по формуле: сумма длин 2х строн должна быть
        больше третьей. Если условие не выполняется, объект не создается, возвращается 'None'.
        """
        if not ((args[0] + args[1] > args[2]) and (args[0] + args[2] > args[1])
                and (args[1] + args[2] > args[0])):
            return None
        else:
            # Возврящаем объект
            return super(Triangle, cls).__new__(cls)

    @property
    def figure_params(self):
        """
        Метод возвращает значение сторон треугольника.
        return:
        """
        return f"сторона_1 = {self.side1}, сторона_2 = {self.side2}, сторона_3 = {self.side3}"

    @property
    def area(self):
        """
        Метод вычисляет площадь треугольника по формуле Герона.
        Сначала необходимо подсчитать разность полупериметра и каждой его стороны. Потом найти
        произведение полученных чисел, умножить результат на полупериметр и найти корень из
        полученного числа.
        S = √ p * (p − a) * (p − b) * (p − c), где a, b, c — стороны, p — полупериметр,
        который можно найти по формуле: p = (a + b + c) / 2

        :return: Площадь треугольника (float)
        """
        if self.is_triangle() == "Yes":
            halfperimetr = self.perimetr / 2
            return math.sqrt(
                halfperimetr * (halfperimetr - self.side1) * (halfperimetr - self.side2) *
                (halfperimetr - self.side3))
        elif self.is_triangle() == "No":
            return None
        else:
            raise Exception

    @property
    def perimetr(self):
        """
        Метод вычисляет периметр треугольника по формуле S = a + b + c
        :return:
        """
        if self.is_triangle() == "Yes":
            return self.side1 + self.side2 + self.side3
        elif self.is_triangle() == "No":
            return None
        else:
            raise Exception

    def is_triangle(self):
        """
        Метод проверяет является ли фигура треугольником по формуле: сумма длин 2х строн должна
        быть больше третьей.
        :return: Yes (str), No (str)
        """
        if (self.side1 + self.side2 > self.side3) and (
                self.side1 + self.side3 > self.side2) and (
                self.side2 + self.side3 > self.side1):
            # print(f"Треугольник со сторонами: {self.figure_params} существует")
            return "Yes"
        else:
            # print(f"Треугольник со сторонами: {self.figure_params} не существует")
            return "No"


if __name__ == "__main__":
    side1 = input("Введите длинну 1ой стороны треугольника: ")
    side2 = input("Введите длинну 2ой стороны треугольника: ")
    side3 = input("Введите длинну 3ой стороны треугольника: ")

    triangle = Triangle(side1, side2, side3)
    print(triangle.is_triangle())

    print("Имя фигуры = {}, {}".format(triangle.get_name(), triangle.figure_params))
    print("Периметр {}а = {}".format(triangle.get_name(), triangle.perimetr))
    print("Площадь {}а = {}".format(triangle.get_name(), triangle.area))
