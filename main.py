#!/usr/bin/python

#################################################################################################
#                         IMPORTING DATA-from different files to the main file
#                             Name : Faith Njuguna
#                             Date : 6/06/2022
#################################################################################################

import operations
from student import student
from teachers import Teachers
from classes import Classes

print(operations.add_numbers(3,5))
print(operations.sub_numbers(10,6))
print(operations.mult_numbers(111,4))
print(operations.div_numbers(75,15))

new_student = student("Faith","Playing chess","2003")
student.greet_student()

new_teacher = Teachers("Mr. John", +(int(7874)) ,"Literature", +(int(25000)))
print(new_teacher.get_tsc_no)

