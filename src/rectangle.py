from figure import Figure


class Rectangle(Figure):
    _name = 'Прямоугольник'

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    @property
    def figure_params(self):
        return f"сторона_1 = {self.side1}, сторона_2 = {self.side2}"

    @property
    def perimetr(self):
        """
        Функция вычисляет периметр прямоугольника
        :return:
        """
        return 2 * (self.side1 + self.side2)

    @property
    def area(self):
        """
        Функция считает площадь прямоугольника по формуле S = a * b.
        :return: Площадь прямоугольника (float)
        """
        return self.side1 * self.side2


if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    print("Имя фигуры = {}, {}".format(rectangle.get_name(), rectangle.figure_params))
    print("Периметр {}а = {}".format(rectangle.get_name(), rectangle.perimetr))
    print("Площадь {}а = {}".format(rectangle.get_name(), rectangle.area))
