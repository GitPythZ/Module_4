# import module_2 as m_2
#
# print(dir(m_2))
# print("Привет, я из модуля_1")
# # print(module_2.a)
# # module_2.say_hi()
# print(m_2.b)

# Чтобы сделать значения из другого модуля "глобальными" - мы пишем имя файла и
# переменныеЮ/элементы через запятую либо воспользуемся *, что значит импорт всех элементов

# from module_2 import a, b, say_hi
#
# print(a)
# print(b)
# print(say_hi())

import module_2 as m_2

print("hi module_1")

print(m_2.__name__)

