from math import pi
from src.figure import Figure


class Circle(Figure):
    """
    Класс Круг. Конструктор принимает радиус окружности.
    """
    _name = 'Круг'

    def __init__(self, radius):
        # Проверяем, задан ли радиус окружности как положительное число
        if not isinstance(radius, int) and not isinstance(radius, float) or radius < 0:
            raise ValueError("Радиусом круга может быть только положительное число!!!")
        self.radius = radius
        print(f"'Circle' object with id = {id(self)} was created successfully")

        # try:  # Проверяем, задан ли радиус окружности как число
        #     self.radius = float(radius)
        # except Exception as e:
        #     print("Радиусом круга может быть только положительное число!!!")
        #     raise e

    @property
    def figure_params(self):
        """
        Метод возвращает значение радиуса круга.
        return:
        """
        return f"Радиус = {self.radius}"

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
    circle = Circle(10)
    print("Имя фигуры = {}, {}".format(circle.get_name(), circle.figure_params))
    print("Периметр {}а = {}".format(circle.get_name(), circle.perimeter))
    print("Площадь {}а = {}".format(circle.get_name(), circle.area))
