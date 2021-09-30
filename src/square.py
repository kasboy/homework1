from src.figure import Figure


class Square(Figure):
    """
    Класс Квадрат. Конструктор принимает длину стороны квадрата.
    """
    _name = 'Квадрат'

    def __init__(self, side):
        try:  # Проверяем, задана ли сторона квадрата как число
            self.side = float(side)
        except Exception as e:
            print("Длиной стороны квадрата может быть только положительное число!!!")
            raise e

    @property
    def figure_params(self):
        """
        Метод возвращает значение длины стороны квадрата.
        return:
        """
        return f"сторона = {self.side}"

    @property
    def perimetr(self):
        """
        Метод вычисляет периметр квадрата
        :return:
        """
        return self.side * 4

    @property
    def area(self):
        """
        Метод вычисляет площадь квадрата по формуле S = a * a.
        :return: Площадь квадрата (float)
        """
        return self.side ** 2


if __name__ == "__main__":
    square = Square(10)
    print("Имя фигуры = {}, {}".format(square.get_name(), square.figure_params))
    print("Периметр {}а = {}".format(square.get_name(), square.perimetr))
    print("Площадь {}а = {}".format(square.get_name(), square.area))
