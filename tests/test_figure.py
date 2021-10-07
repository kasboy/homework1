"""Тесты на класс Figure."""
import pytest

from src.figure import Figure


def test_triangle_create_instance():
    """Проверяем, что объект класса 'Figure' создать нельзя (возникает исключение)"""

    with pytest.raises(Exception):
        figure = Figure()
