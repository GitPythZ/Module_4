from math import inf


def divide(first, second):
    """Функция divide умеет делить на "о".
           Она принимает два параметра first и second, Функция возвращает
           результат деления first на second, но когда в second записан 0 -
            возвращает бесконечность - inf"""
    if second == 0:
        return inf
    else:
        result = first / second
        return result
