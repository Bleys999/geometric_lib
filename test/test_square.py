import unittest
from programs.square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        '''Проверка функции area для квадрата.'''
        self.assertEqual(area(2), 4)
        self.assertEqual(area(3), 9)
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter(self):
        '''Проверка функции perimeter для квадрата.'''
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(3), 12)
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == '__main__':
    unittest.main()
