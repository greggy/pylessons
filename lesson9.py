x = 95
def fun1():
    print(x)

#fun1()


y = 64
def fun2():
    y = 'Test'
    print(y)

fun2()
#print(y)


z = 90
def fun3():
    global z
    z = 81

#print(z)
#fun3()
#print(z)


g = 0
def fun4():
    global g
    g = g + 3
    #print(g)

#fun3()
fun4()
#print(g)
fun4()
#print(g)


a = 88
def fun5():
    a = 99
    def fun():
        print(a)
        def f1():
            a = 'Fom'
            print(a)
        f1()
    fun()

#fun5()


def maker(n):
    def fun(m):
        return m ** n
    return fun

f = maker(2)
#print(f)
#print(f(4))
#print(f(5))

g = maker(3)
#print(g(2))


def fun6():
    x = 66
    def fun(x=x):
        print(x)
    fun()

#fun6()


def fun7():
    x = 3
    y = 5
    act = lambda n, m: x ** n + y - m
    return act

h = fun7()
#print(h(5, 7))


def fun8():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts

d = fun8()
print(d[0])
print(d[2](3))
print(d[0](56))
print(d[4](3))
