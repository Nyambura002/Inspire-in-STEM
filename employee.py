#!/usr/bin/python
# Name : Faith Njuguna      
# Date : 2/06/2022
#employee assignment

class Employee:
    def __init__(self, _name, _ID, _salary):
        self.name = _name
        self.ID = _ID
        self.salary = _salary

    def sayHi(self):
        print('Hello, my name is '+str(self.name) + ' and my ID number is '+str(self.ID) + ', my salary is Ksh '+str(self.salary))
employee1 = Employee('Faith' ,7872234 , 26500)
employee1.sayHi()

