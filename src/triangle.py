import math

from src.figure import Figure


class Triangle(Figure):
    """
    Класс Треугольник. Конструктор принимает длины 3х сторон треугольника. Если треугольк создать
    нельзя, возвращаетя 'None'.
    """
    _name = 'Треугольник'

    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        print(f"'Triangle' object with id = {id(self)} was created successfully")

    @staticmethod
    def __new__(cls, *args):
        """
        Метод проверяет является ли создаваемая фигура треугольником по формуле: сумма длин 2х
        строн должна быть больше третьей. Если условие не выполняется, объект не создается,
        возвращается 'None'.
        """
        # Проверяем, заданы ли стороны треугольника как положительные числа
        for i, arg in enumerate(args):
            # print(f"arg[{i + 1}] = {arg}")
            assert isinstance(arg, (float, int)), "Длина стороны треугольника должна быть числом!"
            assert arg > 0, "Длина стороны должна быть больше нуля!"

        # Проверяем условие существования тругольника
        if not ((args[0] + args[1] > args[2]) and (args[0] + args[2] > args[1])
                and (args[1] + args[2] > args[0])):
            print("Создаваемая фигура не являтся треугольником")
            return None
        # Возврящаем объект
        return super(Triangle, cls).__new__(cls)

    @property
    def sides(self):
        """
        Метод возвращает значение сторон треугольника.
        return:
        """
        return self.__side1, self.__side2, self.__side3

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
        halfperimeter = self.perimeter / 2
        return math.sqrt(
            halfperimeter * (halfperimeter - self.__side1) * (halfperimeter - self.__side2) *
            (halfperimeter - self.__side3))

    @property
    def perimeter(self):
        """
        Метод вычисляет периметр треугольника по формуле S = a + b + c
        :return:
        """
        return self.__side1 + self.__side2 + self.__side3


if __name__ == "__main__":
    # side1 = input("Введите длинну 1ой стороны треугольника: ")
    # side2 = input("Введите длинну 2ой стороны треугольника: ")
    # side3 = input("Введите длинну 3ой стороны треугольника: ")
    # triangle = Triangle(side1, side2, side3)

    triangle = Triangle(13, 14, 15)
    print("Имя фигуры: {}, стороны: {}".format(triangle.get_name(), triangle.sides))
    print("Периметр {}а = {}".format(triangle.get_name(), triangle.perimeter))
    print("Площадь {}а = {}".format(triangle.get_name(), triangle.area))
