#!/usr/bin/python

#################################################################################################
#                                  FUNCTIONS
#                             Name : Faith Njuguna
#                             Date : 31/05/2022
#################################################################################################

#A function is a block of code which gets executed together(all at once)
#defining a function/initializing
#e.g 1:
def say_hello():
    print("Hello from JKUAT!")
    x = 4
    y = 7
    z = x + y
    print(z)
say_hello()

#e.g 2:
def bark():
    print("Dogs bark woof woof.")
def chirps():
    print("A bird chirps in the morning.")
def neigh():
    print("Horses neigh")
bark()
chirps()
neigh()

#Function parameters
#e.g 1:A function to add two numbers
def add_numbers(g,h):     #g and h are parameters
    sum_nums = g + h
    print("The sum of numbers:",sum_nums)
add_numbers(40,50)
add_numbers(100,300)
add_numbers(7,3)

#e.g 2:A function to multiply two numbers
def multiply_numbers(a,b):
    product_nums = a * b
    print("The product of the numbers are:",product_nums)
multiply_numbers(5,7)
multiply_numbers(12,4)
multiply_numbers(74,6)