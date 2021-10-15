class Figure:
    """ Базовый класс геометрической фигуры (Figure). """

    _name = "Фигура"
    __counter = 0

    def __init__(self):
        # Запрещаем создавать экземпляры класса 'Figure'
        if self.__up_counter() > 0:
            raise Exception(f"It's impossible to create an instance of base class {self._name}!")

    @classmethod
    def __up_counter(cls):
        """ Метод класса 'Figure' считает количество созданных экземпляров класса. """

        cls.__counter += 1
        return cls.__counter

    def get_name(self):
        """ Метод выводит название геометрической фигуры. """

        return self._name

    @property
    def area(self):
        """ Метод вычисляет площадь фигуры. """

        pass

    @property
    def perimeter(self):
        """ Метод вычисляет периметр фигуры (сумму длин сторон или длину окружности). """

        pass

    def add_area(self, other):
        """ Метод принимает геометрическую фигуру и возвращает сумму площадей этих фигур.
        Если передана не геометрическая фигура, то выбрасывается ошибка 'ValueError' и
        сообщается, что передан неправильный класс. """

        if not isinstance(other, Figure):
            # Проверяем, является ли объект экземпляром класса Figure
            raise ValueError(
                f"Передан неправильный класс {type(other)}. Можно складывать площади только "
                f"объектов класса Figure и призводных от него")
        return self.area + other.area
