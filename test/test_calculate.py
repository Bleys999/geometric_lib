import unittest
from programs.calculate import calc

class TestCalcFunction(unittest.TestCase):
    def test_circle_perimeter(self):
        '''Проверка функции calc для периметра круга.'''
        result = calc('circle', 'perimeter', [5])
        self.assertAlmostEqual(result, 31.4159, places=4)

    def test_circle_area(self):
        '''Проверка функции calc для площади круга.'''
        result = calc('circle', 'area', [5])
        self.assertAlmostEqual(result, 78.5398, places=4)

    def test_square_perimeter(self):
        '''Проверка функции calc для периметра квадрата.'''
        result = calc('square', 'perimeter', [4])
        self.assertEqual(result, 16)

    def test_square_area(self):
        '''Проверка функции calc для площади квадрата.'''
        result = calc('square', 'area', [4])
        self.assertEqual(result, 16)

    def test_rectangle_perimeter(self):
        '''Проверка функции calc для периметра прямоугольника.'''
        result = calc('rectangle', 'perimeter', [4, 6])
        self.assertEqual(result, 20)

    def test_rectangle_area(self):
        '''Проверка функции calc для площади прямоугольника.'''
        result = calc('rectangle', 'area', [4, 6])
        self.assertEqual(result, 24)

    def test_triangle_perimeter(self):
        '''Проверка функции calc для периметра треугольника.'''
        result = calc('triangle', 'perimeter', [3, 4, 5])
        self.assertEqual(result, 12)

    def test_triangle_area(self):
        '''Проверка функции calc для площади треугольника.'''
        result = calc('triangle', 'area', [3, 4, 5])
        self.assertAlmostEqual(result, 6, places=4)

    def test_invalid_figure(self):
        '''Проверка на некорректную фигуру.'''
        with self.assertRaises(ValueError):
            calc('pentagon', 'perimeter', [5])

    def test_invalid_function(self):
         with self.assertRaises(ValueError):
            calc('circle', 'volume', [5]) # Операция "volume" не поддерживается


    def test_invalid_arguments_count(self):
        '''Проверка на некорректное количество аргументов.'''
        with self.assertRaises(ValueError):
            calc('circle', 'perimeter', [5, 10])
        with self.assertRaises(ValueError):
            calc('square', 'area', [])
        with self.assertRaises(ValueError):
            calc('triangle', 'area', [3, 4])
        with self.assertRaises(ValueError):
            calc('circle', 'area', [])  # Передан пустой список аргументов

if __name__ == '__main__':
    unittest.main()
