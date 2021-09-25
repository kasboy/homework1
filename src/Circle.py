from Figure import Figure
import math


class Circle(Figure):
    _name = 'Круг'

    def __init__(self, radius):
        self.radius = radius

    @property
    def perimetr(self):
        """
        Функция вычисляет длину окружности по формуле S = 2 * π * r
        :return:
        """
        return 2 * math.pi * self.radius

    @property
    def area(self):
        """
        Функция вычисляет площадь окружности по формуле S = π * r * r
        :return: Площадь окружности (float)
        """
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    circle = Circle(10)
    print("Имя фигуры = {}".format(circle.get_name()))
    print("Периметр {}а = {}".format(circle.get_name(), circle.perimetr))
    print("Площадь {}а = {}".format(circle.get_name(), circle.area))
