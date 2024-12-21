import circle  # Импорт модуля circle, содержащего функции для работы с кругами
import square  # Импорт модуля square, содержащего функции для работы с квадратами
import rectangle  # Импорт модуля rectangle, содержащего функции для работы с прямоугольниками

# Списки доступных фигур и функций
figs = ['circle', 'square', 'rectangle']
funcs = ['perimeter', 'area']

# Словарь, определяющий количество аргументов, необходимых для каждой функции и фигуры
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1,
    'perimeter-rectangle': 2,
    'area-rectangle': 2,
}

def calc(fig, func, size):
    """
    Вычисляет результат для заданной фигуры и функции.

    :param fig: Название фигуры ('circle', 'square' или 'rectangle')
    :param func: Название функции ('perimeter' или 'area')
    :param size: Список аргументов для функции
    :return: Результат вычисления
    """
    if fig not in figs:
        raise ValueError(f"Неверная фигура: {fig}. Доступные фигуры: {figs}.")

    if func not in funcs:
        raise ValueError(f"Неверная функция: {func}. Доступные функции: {funcs}.")

    if len(size) != sizes[f"{func}-{fig}"]:
        raise ValueError(f"Неверное количество аргументов для {func} {fig}. "
                         f"Ожидалось: {sizes[f'{func}-{fig}']}.")

    if fig == 'circle':
        if func == 'perimeter':
            return circle.perimeter(size[0])
        elif func == 'area':
            return circle.area(size[0])
    elif fig == 'square':
        if func == 'perimeter':
            return square.perimeter(size[0])
        elif func == 'area':
            return square.area(size[0])
    elif fig == 'rectangle':
        if func == 'perimeter':
            return rectangle.perimeter(size[0], size[1])
        elif func == 'area':
            return rectangle.area(size[0], size[1])
