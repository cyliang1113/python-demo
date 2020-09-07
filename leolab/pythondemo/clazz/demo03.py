# coding: utf-8


class Person(object):
    age = 0

    def __init__(self, name, sex="man"):
        self.name = name
        self.__sex = sex
        self.age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.__sex

    def get_age(self):
        return Person.age

    def get_age2(self):
        return self.age

p1 = Person("tom")

p2 = Person("jack")



Person.age = 4

print("p1 age:", p1.get_age())
print("p2 age:", p2.get_age())
print("p2 age:", p2.get_age2())

