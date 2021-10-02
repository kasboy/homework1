import pytest
from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture
def create_circle():
    return Circle(5)

@pytest.fixture
def create_figure():
    return Figure()

@pytest.fixture
def create_rectangle():
    return Rectangle(4, 5)

@pytest.fixture
def create_square():
    return Square(4)

@pytest.fixture
def create_triangle():
    return Triangle(13, 14, 15)
