import unittest
from calculate import calc, figs, funcs, sizes
from circle import area, perimeter
from rectangle import area, perimeter
from square import area, perimeter
from triangle import area, perimeter

class TestCalcFunction(unittest.TestCase):

    def test_circle_perimeter(self):
        result = calc('circle', 'perimeter', [5])
        self.assertAlmostEqual(result, 31.4159, places=4)  # Периферия круга = 2 * π * r

    def test_circle_area(self):
        result = calc('circle', 'area', [5])
        self.assertAlmostEqual(result, 78.5398, places=4)  # Площадь круга = π * r^2

    def test_square_perimeter(self):
        result = calc('square', 'perimeter', [4])
        self.assertEqual(result, 16)  # Периметр квадрата = 4 * a

    def test_square_area(self):
        result = calc('square', 'area', [4])
        self.assertEqual(result, 16)  # Площадь квадрата = a^2

    def test_invalid_figure(self):
        with self.assertRaises(ValueError):
            calc('triangle', 'perimeter', [5])  # Некорректная фигура

    def test_invalid_function(self):
        with self.assertRaises(ValueError):
            calc('circle', 'volume', [5])  # Некорректная функция

    def test_invalid_arguments_count(self):
        with self.assertRaises(ValueError):
            calc('circle', 'perimeter', [5, 10])  # Избыточное количество аргументов

        with self.assertRaises(ValueError):
            calc('square', 'area', [])  # Недостаточное количество аргументов

if __name__ == '__main__':
    unittest.main()

class TestCircle(unittest.TestCase):

    def test_area(self):
        # Тесты для функции, вычисляющей площадь круга
        self.assertAlmostEqual(area(2), 12.566370614359172)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(1), 3.141592653589793)

        # Проверка на недопустимые входные данные
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            area(-2.5)

    def test_perimeter(self):
        # Тесты для функции, вычисляющей периметр круга
        self.assertAlmostEqual(perimeter(2), 12.566370614359172)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(1), 6.283185307179586)

        # Проверка на недопустимые входные данные
        with self.assertRaises(ValueError):
            perimeter(-1)
        with self.assertRaises(ValueError):
            perimeter(-2.5)

if __name__ == '__main__':
    unittest.main()

class TestRectangle(unittest.TestCase):

    def test_area(self):
        # Тесты для функции, вычисляющей площадь
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(3, 7), 21)
        self.assertEqual(area(2.5, 4), 10.0)

        # Проверка на недопустимые значения
        with self.assertRaises(ValueError):
            area(-1, 10)
        with self.assertRaises(ValueError):
            area(5, -1)
        with self.assertRaises(ValueError):
            area(-2, -3)

    def test_perimeter(self):
        # Тесты для функции, вычисляющей периметр
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(0, 10), 20)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(3, 7), 20)
        self.assertEqual(perimeter(2.5, 4), 13.0)

        # Проверка на недопустимые значения
        with self.assertRaises(ValueError):
            perimeter(-1, 10)
        with self.assertRaises(ValueError):
            perimeter(5, -1)
        with self.assertRaises(ValueError):
            perimeter(-2, -3)

if __name__ == '__main__':
    unittest.main()

class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        # Тесты для функции, вычисляющей площадь
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(3), 9)

        # Провера на недопустимые входные данные
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter(self):
        # Тесты для функции, вычисляющей периметр
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(3), 12)

        # Проверка на недопустимые входные данные
        with self.assertRaises(ValueError):
            perimeter(-1)

if __name__ == '__main__':
    unittest.main()

class TestTriangleFunctions(unittest.TestCase):

    def test_area(self):
        # Тестируем корректные значения
        self.assertEqual(area(3, 4, 5), 6.0)
        self.assertEqual(area(5, 5, 5), 7.5)
        self.assertEqual(area(10, 10, 10), 15.0)

    def test_perimeter(self):
        # Тестируем корректные значения
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)
        self.assertEqual(perimeter(10, 10, 10), 30)

    def test_negative_values(self):
        # Тестируем недопустимые значения
        with self.assertRaises(ValueError):
            area(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            area(3, 4, -5)
        with self.assertRaises(ValueError):
            perimeter(-3, -4, -5)

if __name__ == '__main__':
    unittest.main()
