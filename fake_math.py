from math import inf


def divide(first, second):
    """Функция divide выдает ошибку при делении на "о".
       Она принимает два параметра first и second, Функция возвращает
       результат деления first на second, но когда в second записан 0 -
        возвращает 'Ошибку'"""
    if second == 0:
        return "Ошибка, на ноль делить нельзя!"
    else:
        result = first / second
        return result



