#print('Hello World')
#print(23 * 643)


"""
name = input('What is your name? ')
print('Hello ' + name + '! Nice to meet you.')

"""


from random import choice

my_choice = choice([1,2])
your_choice = input('Which side of the coin falls? [1 or 2] ')
if my_choice == your_choice:
    print('You won!')
else:
    print('Nope, my side was ' + str(my_choice))
