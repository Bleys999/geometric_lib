import unittest
from programs.triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        '''Проверка функции area для треугольника.'''
        self.assertEqual(area(3, 4, 5), 6.0)
        self.assertEqual(area(5, 5, 5), 7.5)

    def test_perimeter(self):
        '''Проверка функции perimeter для треугольника.'''
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)

    def test_negative_values(self):
        '''Проверка на некорректные значения для треугольника.'''
        with self.assertRaises(ValueError):
            area(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)


if __name__ == '__main__':
    unittest.main()
