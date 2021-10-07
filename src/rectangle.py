from src.figure import Figure


class Rectangle(Figure):
    """
    Класс Прямоугольник. Конструктор принимает длину и ширину прямоугольника.
    """
    _name = 'Прямоугольник'

    def __init__(self, side1, side2):
        assert isinstance(side1, (float, int)) and isinstance(side2, (float, int)), \
            "Длина стороны прямоугольника должна быть числом!"
        assert side1 > 0 and side2 > 0, "Длина стороны должна быть больше нуля!"
        self.__side1 = side1
        self.__side2 = side2

    @property
    def sides(self):
        """
        Метод возвращает значение длин сторон прямоугольника.
        return:
        """
        return self.__side1, self.__side2

    @property
    def perimeter(self):
        """
        Метод вычисляет периметр прямоугольника
        :return:
        """
        return 2 * (self.__side1 + self.__side2)

    @property
    def area(self):
        """
        Метод вычисляет площадь прямоугольника по формуле S = a * b.
        :return: Площадь прямоугольника (float)
        """
        return self.__side1 * self.__side2


if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    print("Имя фигуры = {}, стороны: {}".format(rectangle.get_name(), rectangle.sides))
    print("Периметр {}а = {}".format(rectangle.get_name(), rectangle.perimeter))
    print("Площадь {}а = {}".format(rectangle.get_name(), rectangle.area))
