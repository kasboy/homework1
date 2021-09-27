from figure import Figure


class Square(Figure):
    _name = 'Квадрат'

    def __init__(self, side):
        self.side = side

    @property
    def figure_params(self):
        return f"сторона = {self.side}"

    @property
    def perimetr(self):
        """
        Функция вычисляет периметр квадрата
        :return:
        """
        return self.side * 4

    @property
    def area(self):
        """
        Функция вычисляет площадь квадрата по формуле S = a * b.
        :return: Площадь треугольника (float)
        """
        return self.side ** 2


if __name__ == "__main__":
    square = Square(10)
    print("Имя фигуры = {}, {}".format(square.get_name(), square.figure_params))
    print("Периметр {}а = {}".format(square.get_name(), square.perimetr))
    print("Площадь {}а = {}".format(square.get_name(), square.area))
