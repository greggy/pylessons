# -*- coding: utf-8 -*-


a = [i ** 2 for i in range(1, 9)]
#print(a)


b = [i for i in range(-9, 9) if i <= 0]
#print(b)


c = [(i, j, k) for i in range(1, 5)
     for j in range(1, 5)
     for k in range(1, 5)]
#print(c)


def sqr(l):
    for i in l:
        yield i ** 2

#print(sqr(range(1, 9)))
#print(list(sqr(range(1, 9))))


d = (i ** 2 for i in range(1, 9))
#print(d)
#print(list(d))


f = sum(i ** 2 for i in range(1, 9))
#print(f)


g = sorted(i ** 2 for i in range(1, 9))
#print(list(g))


h = sorted((i ** 2 for i in range(1, 9)), reverse=True)
#print(list(h))


from math import pow

def mymap(fun, l):
    r = []
    for i in l:
        r.append(fun(i))
    return r

print(mymap(pow, range(1, 9)))
