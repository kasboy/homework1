from math import pi
from src.figure import Figure


class Circle(Figure):
    """
    Класс Круг. Конструктор принимает радиус окружности.
    """
    _name = 'Круг'

    def __init__(self, radius):
        # Проверяем, задан ли радиус окружности как положительное число
        assert isinstance(radius, int) or isinstance(radius, float), "Радиус должен быть числом!"
        assert radius > 0, "Радиус должен быть больше нуля!"
        self.__radius = radius

    @property
    def radius(self):
        """
        Метод возвращает значение радиуса круга.
        return:
        """
        return self.__radius

    @property
    def perimeter(self):
        """
        Метод вычисляет длину окружности по формуле S = 2 * π * r
        :return:
        """
        return 2 * pi * self.radius

    @property
    def area(self):
        """
        Метод вычисляет площадь окружности по формуле S = π * r * r
        :return: Площадь окружности (float)
        """
        return pi * self.radius ** 2


if __name__ == "__main__":
    circle = Circle(1)
    print("Имя фигуры = {}, Радиус = {}".format(circle.get_name(), circle.radius))
    print("Периметр {}а = {}".format(circle.get_name(), circle.perimeter))
    print("Площадь {}а = {}".format(circle.get_name(), circle.area))
