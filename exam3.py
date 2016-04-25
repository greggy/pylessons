# coding: utf-8

##---------------------------------------------------------------------
## Задание 1
##---------------------------------------------------------------------
"""
У строки есть методы find, index, split, lower, isdigit и т. д. Почитать
как они работают и привести пример использования пяти строковых методов
на произвольной строке.
"""


##---------------------------------------------------------------------
## Задание 2
##---------------------------------------------------------------------
"""
Расшифровать строку используя функцию chr и вывести строку.
"""
s1 = '89, 111, 117, 32, 97, 114, 101, 32, 97, 32, 99, 111, 111, 108, 32, 112, 114, 111, 103, 114, 97, 109, 109, 101, 114, 33'


##---------------------------------------------------------------------
## Задание 3
##---------------------------------------------------------------------
"""
Используя встроенную функцию enumerate и конструкцию for обработать
последовательность случайных чисел и вывести тот-же список, где каждый
третий элемент возведён в степень 2.
"""
l1 = [84, 25, 56, 55, 57, 41, 39, 77, 23, 45, 56, 23, 75, 45, 39, 9, 93, 80, 94, 49, 70, 86, 90, 60, 27, 20, 23, 82, 40, 81, 20, 74, 34, 40, 30]


##---------------------------------------------------------------------
## Задание 4
##---------------------------------------------------------------------
"""
Отформатируйте строку с вашими данными: имя, фамилия и email. Используйте
raw_input.
"""


##---------------------------------------------------------------------
## Задание 5
##---------------------------------------------------------------------
"""
Импортируйте модуль (скрипт) test3.py и поиграйтесь с его переменными
и функциями. Помните, что-бы скрипт был успешно импортирован, необходимо
запускать питон шелл (python) из дериктории, где лежит файл test3.py
"""


##---------------------------------------------------------------------
## Задание 6
##---------------------------------------------------------------------
"""
Написать функцию подсчёта сколько придётся платить по кредиту.
"""
def calcCredit(years, amount, perc):
    print("Calculation of a credit for %d with amount %d and interest %f" % (years, amount, perc))
    "Your code goes here"
    return

print(calcCredit(2, 100000, 0.135))
print(calcCredit(2, 2350000, 0.4))
print(calcCredit(2, 25000, 0.25))
