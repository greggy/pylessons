# coding: utf-8


"""
while True:
    num = raw_input('Which number? > ')
    if num == 'stop':
        break
    elif not num.isdigit():
        print('Please, enter only numbers!')
    else:
        print(int(num)**2)
print('Buy!')
"""


while True:
    num = raw_input('Which number? > ')
    if num == 'stop':
        break
    try:
        int(num)
    except ValueError:
        print('Please, enter only numbers!')
    else:
        print(int(num)**2)
print('Buy!')
