# -*- coding: utf-8 -*-


class Test:
    def setsurname(self, surname):
        self.surname = surname


class FirstClass:
    def setname(self, name):
        self.name = name

    def display(self):
        return self.name


class SecondClass(FirstClass, Test):
    def display(self):
        return 'The name is %s' % self.name


class Person:
    def __init__(self, name=None, age=0, status='Teacher'):
        self.name = name
        self.age = age
        self.status = status
    
    def __str__(self):
        return '[Person name: %s, status: %s]' % (self.name, self.status)

    def change_status(self, new_status):
        self.status = new_status


class Student(Person):
    def __init__(self, name=None, age=0, status='Student'):
        self.name = name
        self.age = age
        self.status = status

    def add_klass(self, klass):
        self.klass = klass

    def show_klass(self):
        return self.klass

    #def __str__(self):
    #    return '[Student: %s, klass: %s]' % (self.name, self.klass)


class Teacher(Person):
    pass


class Worker(Person):
    pass

