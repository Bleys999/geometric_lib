import unittest
from programs.rectangle import area, perimeter


class TestRectangle(unittest.TestCase):
    def test_area(self):
        '''Проверка функции area для прямоугольника.'''
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(3, 7), 21)
        with self.assertRaises(ValueError):
            area(-1, 10)

    def test_perimeter(self):
        '''Проверка функции perimeter для прямоугольника.'''
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(0, 10), 20)
        self.assertEqual(perimeter(3, 7), 20)
        with self.assertRaises(ValueError):
            perimeter(-1, 10)


if __name__ == '__main__':
    unittest.main()
