import unittest
from programs.circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area(self):
        '''Проверка функции area для круга.'''
        self.assertAlmostEqual(area(2), 12.5664, places=4)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(1), 3.1416, places=4)
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter(self):
        '''Проверка функции perimeter для круга.'''
        self.assertAlmostEqual(perimeter(2), 12.5664, places=4)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(1), 6.2832, places=4)
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == '__main__':
    unittest.main()
