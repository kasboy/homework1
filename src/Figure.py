# from ABC import
"""
Базовый класс геометрической фигуры (Figure)
"""

# Исходные данные


class Figure:
    _name = None

    def __init__(self):
        pass

    def get_name(self):
        return self._name

    @property
    def area(self):
        """
        Функция вычисляет площадь фигуры
        :return:
        """
        pass

    @property
    def perimetr(self):
        """
        Функция вычисляет периметр фигуры (сумму длин сторон или длину окружности)
        :return:
        """
        pass

    # def __add__(self, other):
    #     """
    #     Функция принимает другую геометрическую фигуру и возвращает сумму площадей этих фигур.
    #     Если передана не геометрическая фигура, то выбрасывается ошибку (raise ValueError) и сообщается,
    #     что передан неправильный класс.
    #     :return:
    #     """
    #     if not isinstance(other, Figure):  # Проверяю, является ли объект экземпляром класса Figure
    #         raise ValueError("Можно складывать площади только объектов класса Figure!")
    #     return self.area + other.area

    def add_area(self, other):
        """
        Функция принимает другую геометрическую фигуру и возвращает сумму площадей этих фигур.
        Если передана не геометрическая фигура, то выбрасывается ошибку (raise ValueError) и сообщается,
        что передан неправильный класс.
        :return:
        """
        if not isinstance(other, Figure):  # Проверяю, является ли объект экземпляром класса Figure
            raise ValueError("Можно складывать площади только объектов класса Figure!")
        return self.area + other.area
