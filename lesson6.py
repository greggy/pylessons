# coding: utf-8


def fun1():
    pass


i = 10
while i > 0:
    i -= 1
    if i % 2 != 0:
        continue
    print(i)


x = "abcds"
while x:
    if not x[0].isalpha():
        print("Yeah, it's not a letter.")
        break
    x = x[1:]
else:
    print("It has only letters.")



s1 = "pmsa"
s2 = "gmsp"
s3 = []
for l in s1:
    if l in s2:
        print(l, "was found")
        s3.append(l)
    else:
        print(l, "not found")



l1 = [1, 2, 3, 4, 5, 0]
l2 = [6, 7, 8, 9, 10]
l3 = [6, 7, 8]
print(list(zip(l1, l2, l3)))
