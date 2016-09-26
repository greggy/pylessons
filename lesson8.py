seq1 = 'SPAM'
seq2 = 'SRAM'

seq3 = [1, 2, 3]
seq4 = (2, 3, 4)


def fun1(x, y):
    res = []
    for a in x:
        if a in y:
            res.append(a)
    return res

a = fun1(seq1, seq2)
print(a)

b = fun1(seq3, seq4)
print(b)

c = fun1

d = c(seq1, seq2)
print d
x
