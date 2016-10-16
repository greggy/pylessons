# -*- coding: utf-8 -*-

# --------------------------------------------------
# Особенности для изменяемых обьектов
# --------------------------------------------------

h = 0

def num():
    h = 8

num()
#print(h)


l = ['a', 8, 'Test']

def lst():
    l2 = l[:]
    l2[1] = 88

lst()
#print(l)


# --------------------------------------------------
# Аргументы
# --------------------------------------------------

def fun1(a, b, c):
    print('fun1', a, b, c)

#fun1(2, 3, 4)


def fun2(a, b, c=0):
    print('fun2', a, b, c)

#fun2(5, 4, 6)
#fun2(9, 8)

#fun2(77, b=33, c=55)
#fun2(b=11, a=9)


def fun3(a, b, c):
    print('fun3', a, b, c)

#fun3(5, c=7, b=8)
#fun3(c=9, b=8, a=7)


f = [5, 6, 7]
fun1(*f)


def fun4(*args):
    print('fun4', args)

#fun4(5, 6, 7, 8, 9, 10)
#fun4(9, 2)
#fun4(['Test', 'Spam'])


def fun5(**kw):
    print(kw['b'])
    print('fun5', kw)

d = {'a': 5, 'b': 7, '9': 0}
#fun5(**d)


def fun6(s, g='Man', *args, **kw):
    print('fun6', s, g, args, kw)

fun6(9, 'Spam')
fun6(11)
fun6(6, 'Woman', *f, **d)

#fun6(99, 1, 2, 3)
#fun6(77, args=[])
