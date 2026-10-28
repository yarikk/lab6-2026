"""
Юніт-тести для Лабораторної роботи № 6.

Студенти повинні доповнити цей файл тестами для своїх рішень.
"""
import unittest

# Імпортуємо модулі нашого пакета geometry_2d
from geometry_2d import rectangle, circle


class TestLab6(unittest.TestCase):

    def test_example(self):
        """Приклад тестового випадку."""
        self.assertEqual(2 + 2, 4)

    # Тести для модуля rectangle
    def test_rectangle_area(self):
        """Тестовий випадок для обчислення площі прямокутника."""
        self.assertEqual(rectangle.area(3, 4), 12)
        self.assertEqual(rectangle.area(2.5, 2), 5.0)

    def test_rectangle_perimeter(self):
        """Тестовий випадок для обчислення периметра прямокутника."""
        self.assertEqual(rectangle.perimeter(3, 4), 14)
        self.assertEqual(rectangle.perimeter(2.5, 2), 9.0)

    def test_rectangle_edge_cases(self):
        """Тестування граничних випадків для прямокутника."""
        with self.assertRaises(ValueError):
            rectangle.area(-1, 5)
        with self.assertRaises(ValueError):
            rectangle.perimeter(3, -2)

    # Тести для модуля circle
    def test_circle_area(self):
        """Тестовий випадок для обчислення площі круга."""
        self.assertAlmostEqual(circle.area(1), 3.1415926535, places=5)
        self.assertEqual(circle.area(0), 0.0)

    def test_circle_circumference(self):
        """Тестовий випадок для обчислення довжини кола."""
        self.assertAlmostEqual(circle.circumference(1), 6.283185307, places=5)
        self.assertEqual(circle.circumference(0), 0.0)

    def test_circle_edge_cases(self):
        """Тестування граничних випадків для кола."""
        with self.assertRaises(ValueError):
            circle.area(-3)
        with self.assertRaises(ValueError):
            circle.circumference(-5)


if __name__ == '__main__':
    unittest.main()