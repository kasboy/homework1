class Figure:
    """
    Базовый класс геометрической фигуры (Figure)
    """
    _name = "Figure"
    __counter = 0

    def __init__(self):
        # Запрещаем создавать экземпляры класса 'Figure'
        if self.__up_counter() > 0:
            raise Exception(f"It's impossible to create an instance of base class {self._name}!")

    @classmethod
    def __up_counter(cls):
        cls.__counter += 1
        return cls.__counter

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

    def add_area(self, other):
        """
        Функция принимает другую геометрическую фигуру и возвращает сумму площадей этих фигур.
        Если передана не геометрическая фигура, то выбрасывается ошибку (raise ValueError) и
        сообщается, что передан неправильный класс.
        :return:
        """
        if not isinstance(other, Figure):  # Проверяю, является ли объект экземпляром класса Figure
            raise ValueError(
                "Передан неправильный класс. Можно складывать площади только объектов класса"
                " Figure и призводных от него")
        return self.area + other.area
