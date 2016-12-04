# -*- coding: utf-8 -*-

from tools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, age=0, status='Teacher'):
        self.name = name
        self.age = age
        self.status = status
    
    # def __str__(self):
    #     return '[Person name: %s, status: %s]' % (self.name, self.status)

    def raise_age(self):
        self.age += 1

    def set_age(self, value):
        self.age = value    

    def change_status(self, new_status):
        self.status = new_status


class Student(Person):
    def __init__(self, name, age=0):
        Person.__init__(self, name, age, 'Student')

    def add_klass(self, klass):
        self.klass = klass

    def show_klass(self):
        return self.klass


class Employer(Person):
    def __init__(self, name, salary, status, age=0):
        Person.__init__(self, name, age=age, status=status)
        self.salary = salary
        
    def get_salary(self):
        return self.salary

    def raise_salary(self, percent):
        self.salary += percent * self.salary / 100
    
    
class Teacher(Employer):
    def __init__(self, name, salary, age):
        Employer.__init__(self, name, salary, 'Teacher', age)



class Worker(Employer):
    pass


if __name__ == '__main__':
    bob = Student('Bob Doe')
    joe = Person('Joe Smith')
    anna = Person('Anna Woo', age=18)
    print(bob.name == 'Bob Doe')
    print(joe.name == 'Joe Smith')
    print(anna.name == 'Anna Woo')
    print(anna.age == 18)
    anna.raise_age()
    print(anna.age == 19)
    bob.set_age(23)
    print(bob.age == 23)
    art = Teacher('Allan Po', 10000, 41)
    print(art.salary == 10000)
    art.raise_salary(10)
    print(int(art.salary) == 11000)
