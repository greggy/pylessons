# -*- coding: utf-8 -*-

from math import pow

def mymap1(fun, l):
    res = []
    for i in l:
        res.append(fun(i))
    return res

#print(mymap1(str, [3, 1, 7, 4, 6, 9]))


def mymap2(fun, *l):
    res = []
    for i in zip(*l):
        print(i)
        res.append(fun(*i))
    return res

#print(mymap2(lambda a, b, c: a+b+c, [3, 1, 7, 4, 6], [6, 3, 8, 5, 9], [2, 5, 2, 4, 5]))


def mymap3(fun, *l):
    for i in zip(*l):
        print(i)
        yield fun(*i)

print(mymap3(pow, [3, 1, 7, 4, 6, 9], [1, 5, 7, 3, 2, 1]))
print(list(mymap3(pow, [3, 1, 7, 4, 6, 9], [1, 5, 7, 3, 2, 1])))
