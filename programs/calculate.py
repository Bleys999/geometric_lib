from programs.circle import area as circle_area, perimeter as circle_perimeter
from programs.rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from programs.square import area as square_area, perimeter as square_perimeter
from programs.triangle import area as triangle_area, perimeter as triangle_perimeter

# Импорт функций area и perimeter из circle, rectangle, square, triangle

# Списки доступных фигур и функций
figs = ['circle', 'square', 'rectangle', 'triangle']
funcs = ['perimeter', 'area']

# Словарь, определяющий количество аргументов, необходимых для каждой функции и фигуры
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1,
    'perimeter-rectangle': 2,
    'area-rectangle': 2,
    'perimeter-triangle': 3,
    'area-triangle': 3,
}

import math

def calc(shape, operation, size):
    if shape == 'circle' and operation == 'area':
        if len(size)!=1:
            raise ValueError("Для вычисления площади нужно только 1 значение - радиус")
        return circle_area(size[0])
    elif shape == 'circle' and operation == 'perimeter':
        if len(size)!=1:
            raise ValueError("Для вычисления периметра нужно только 1 значение - радиус")
        return circle_perimeter(size[0])
    elif shape == 'rectangle' and operation == 'area':
        if len(size)!=2:
            raise ValueError("Для вычисления площади нужно 2 значения")
        return rectangle_area(size[0], size[1])
    elif shape == 'rectangle' and operation == 'perimeter':
        if len(size)!=2:
            raise ValueError("Для вычисления периметра нужно 2 значения")
        return rectangle_perimeter(size[0], size[1])
    elif shape == 'square' and operation == 'area':
        if len(size)!=1:
            raise ValueError("Для вычисления площади нужно только 1 значение")
        return square_area(size[0])
    elif shape == 'square' and operation == 'perimeter':
        if len(size)!=1:
            raise ValueError("Для вычисления периметра нужно только 1 значение")
        return square_perimeter(size[0])
    elif shape == 'triangle' and operation == 'area':
        if len(size)!=3:
            raise ValueError("Для вычисления площади нужно 3 значения")
        return triangle_area(size[0], size[1], size[2])
    elif shape == 'triangle' and operation == 'perimeter':
        if len(size)!=3:
            raise ValueError("Для вычисления периметра нужно 3 значения")
        return triangle_perimeter(size[0], size[1], size[2])
    else:
        raise ValueError("Неверная фигура или операция")
