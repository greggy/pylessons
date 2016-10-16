# -*- coding: utf-8 -*-


def mysum(l):
    print(l)
    if not l:
        return 0
    else:
        return l[0] + mysum(l[1:])

#print(mysum([2, 3, 4, 5, 6]))


def mysum2(l):
    return 0 if not l else l[0] + mysum2(l[1:])

#print(mysum2([2, 3, 4, 5, 6]))


x1 = lambda x, y, z: x + y + z
#print(x1)
#print(x1(5, 2, 9))


x2 = lambda a='foo', b='bar', c='dar': a + b + c
#print(x2('wee'))
#print(x2())


def echo(mess):
    print(mess)

x3 = echo
#x3('Hi there!')


def inderect(func, message):
    func(message)

#inderect(x3, 'And there!')


def calc(func, x, y):
    print func(x, y)

import operator

#calc(operator.add, 3, 5)
#calc(operator.sub, 13, 5)
#calc(operator.mul, 4, 5)
#calc(operator.div, 18, 3)


l2 = '123456789'
#print(map(int, l2))
#[int(i) for i in l2]


#print(filter(lambda x: x < 0, range(-6, 6)))


l3 = [1, 2, 3, 4, 5]
#print(reduce(lambda x, y: x + y, l3))
#print(reduce(lambda x, y: x * y, l3))


def chk(i):
    return i.startswith('ab')

print(filter(chk, ['abc', 'bcd', 'abd']))


def red(l):
    k = 0
    for i in l:
        k += i
    print(k)

#red(l3)
