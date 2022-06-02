#!/usr/bin/python
#################################################################################################
#                                    CLASSES
#                             Name : Faith Njuguna
#                             Date : 2/06/2022
#################################################################################################


class Person:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def sayHi(self):
        print('Hello, my name is '+str(self.name) + ' and I am '+str(self.age) +' years old')
person1 = Person('Bobby',16)
person1.sayHi() 
person2 = Person('James',22)
person2.sayHi()
