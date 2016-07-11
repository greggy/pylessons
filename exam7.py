# coding: utf-8


# --------------------------------------------------
# Задача 1
# --------------------------------------------------
"""
Вспомните лекцию 7 и привидите пример итератора. Помните,
итерационный протокол имеют почти все встроенные типы данных,
которые можно использовать в циклах. Чем отличаются встроен-
ные функции range и xrange в Python 2.7?
"""


# --------------------------------------------------
# Задача 2
# --------------------------------------------------
"""
Напишите комплексный генератор списка, который вернёт
последовательность кортежей из 3-х элементов каждый и
где сумма цифр в кортеже не должны быть равной 6. 
Используйте список для l1 для генерации списка кортежей.
"""
l1 = range(1, 6)


# --------------------------------------------------
# Задача 3
# --------------------------------------------------
"""
Есть многострочная структура (см. пример) в виде цифр.
Найдите наибольшую сумму цифр идя с вершины пирамиды и
до её подножья, выбирая ТОЛЬКО соседние цифры из следующей
линии. Если выбрана цифра 6 из 3-ей линии, то в 4-ой можно
выбирать или 7 или 20.
Пример: 2 8 9 4 8 23 14, то есть наибольшая сумма равна
68.
Помните, тестовая структура может быть намного больше.
"""
s1 = """
2
5 8
7 1 9
21 6 3 4
11 7 20 1 8
5 4 0 12 23 2
17 3 6 5 14 1 9
"""


# --------------------------------------------------
# Задача 4
# --------------------------------------------------
"""
Есть двухмерная матрица чисел размером 6х6 (см. s2). И
есть меньшая структура "песочные часы", она имеет вид:
a b c
  d
e f g
Числа могут быть от -9 и до 9. Таких "песочных часов" на
данной матрице 16.
Необходимо найти наибольшую сумму цифр "песочных часов"
на матрице. В данном примере наибольшее число 19
2 4 4
  2
1 2 4
"""
s2 = """
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""


# --------------------------------------------------
# Задача 5
# --------------------------------------------------
"""
Необходимо написать реализацию консольной игры hangman.
В ней бот выбирает слово из словаря words.txt и выводит
его в виде "_ _ _ _ _", то есть мы знаем, что в слове 5
букв. Дальше бот нам даёт 7 попыток и мы пытаемся буква
за буквой угадать слово. Если буква угадана верно, то
счётчик попыток не уменьшается, если такой буквы нет в
слове, то счётчик уменьшается на 1. Игра считается
выигранной, если все буквы в слове угаданны и проигранной,
если попыток больше нет и остались неугаданные буквы.

См. архив hangman.zip
"""
