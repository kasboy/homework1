from src.figure import Figure


class Rectangle(Figure):
    """
    Класс Прямоугольник. Конструктор принимает длину и ширину прямоугольника.
    """
    _name = 'Прямоугольник'

    def __init__(self, side1, side2):
        if not isinstance(side1, int) and not isinstance(side1, float) or side1 < 0:
            raise ValueError("Длинами сторон прямоугольника могут быть только положительные числа!")
        elif not isinstance(side2, int) and not isinstance(side2, float) or side2 < 0:
            raise ValueError("Длинами сторон прямоугольника могут быть только положительные числа!")
        self.side1 = side1
        self.side2 = side2
        print(f"'Rectangle' object with id = {id(self)} was created successfully")

    @property
    def figure_params(self):
        """
        Метод возвращает значение длин сторон прямоугольника.
        return:
        """
        return f"сторона_1 = {self.side1}, сторона_2 = {self.side2}"

    @property
    def perimeter(self):
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
    rectangle = Rectangle(1, 5)
    print("Имя фигуры = {}, {}".format(rectangle.get_name(), rectangle.figure_params))
    print("Периметр {}а = {}".format(rectangle.get_name(), rectangle.perimeter))
    print("Площадь {}а = {}".format(rectangle.get_name(), rectangle.area))
