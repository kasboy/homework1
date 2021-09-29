from figure import Figure


class Rectangle(Figure):
    """
    Класс Прямоугольник. Конструктор принимает длину и ширину прямоугольника.
    """
    _name = 'Прямоугольник'

    def __init__(self, side1, side2):
        try:  # Проверяем, задана ли сторона квадрата как число
            self.side1 = float(side1)
            self.side2 = float(side2)
        except Exception as e:
            print("Длинами сторон прямоугольника могут быть только положительные числа!!!")
            raise e

    @property
    def figure_params(self):
        """
        Метод возвращает значение длин сторон прямоугольника.
        return:
        """
        return f"сторона_1 = {self.side1}, сторона_2 = {self.side2}"

    @property
    def perimetr(self):
        """
        Метод вычисляет периметр прямоугольника
        :return:
        """
        return 2 * (self.side1 + self.side2)

    @property
    def area(self):
        """
        Метод вычисляет площадь прямоугольника по формуле S = a * b.
        :return: Площадь прямоугольника (float)
        """
        return self.side1 * self.side2


if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    print("Имя фигуры = {}, {}".format(rectangle.get_name(), rectangle.figure_params))
    print("Периметр {}а = {}".format(rectangle.get_name(), rectangle.perimetr))
    print("Площадь {}а = {}".format(rectangle.get_name(), rectangle.area))
