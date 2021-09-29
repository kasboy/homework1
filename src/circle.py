from math import pi
from figure import Figure



class Circle(Figure):
    """
    Класс Круг. Конструктор принимает радиус окружности.
    """
    _name = 'Круг'

    def __init__(self, radius):
        try:  # Проверяем, задан ли радиус окружности как число
            self.radius = float(radius)
        except Exception as e:
            print("Радиусом круга может быть только положительное число!!!")
            raise e

    @property
    def figure_params(self):
        """
        Метод возвращает значение радиуса круга.
        return:
        """
        return f"Радиус = {self.radius}"

    @property
    def perimetr(self):
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
    circle = Circle(10)
    print("Имя фигуры = {}, {}".format(circle.get_name(), circle.figure_params))
    print("Периметр {}а = {}".format(circle.get_name(), circle.perimetr))
    print("Площадь {}а = {}".format(circle.get_name(), circle.area))
