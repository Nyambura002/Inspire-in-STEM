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
#Start with function definition
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

#Date : 3/06/2022
#Using default parameters-start by initializing the variable
def print_name(name = "Faith Nyambura"):
    print (name)
print_name("Othniel")

#Return from a function
def get_sum(num1 , num2):
    sum_num = num1 + num2
    return sum_num
print(get_sum(8,12))

#A function to get the powers of numbers
def powers(number , power):
    pow_num = number ** power
    return pow_num
print(powers(6,4))

#Getting a person's full names
def get_full_name(f_name , s_name):
    full_name = f_name + " " + s_name
    return full_name.title()
print(get_full_name("Faith", "Njuguna"))

#Returning a dictionary from a function
def create_full_name(first_name , second_name):
    person = {'first':first_name , 'second':second_name}
    return person
student = create_full_name("Faith","Nyambura")
print(student)

#Passing a list in a function
def greet_friends(names):
    for name in names:
        msg = "Hello!" + " " + name.title() + "!"
        print(msg)
friends = ['Mercy','Grace','Luke']     #create a list of friends
greet_friends(friends)