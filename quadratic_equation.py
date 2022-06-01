#!/usr/bin/python

#################################################################################################
#                              QUADRATIC EQUATION
#                             Name : Faith Njuguna
#                             Date : 31/05/2022
#################################################################################################
import math

a = int(input("Enter the coefficient of the first term(a):"))
b = int(input("Enter the coefficient of the second term(b):"))
c = int(input("Enter the constant(c):"))
w = math.sqrt(b**2 - 4*a*c)

def find_roots(a,b,c):
    y_1 = ((-b + (w)) / (2*a))
    y_2 = ((-b - (w)) / (2*a))
    print("The roots of the quadratic equation are:",y_1,y_2)
find_roots(a,b,c)

