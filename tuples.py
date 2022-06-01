#!/usr/bin/python


#################################################################################################
#                       TUPLES-similar to lists but is immutable
#                             Name : Faith Njuguna
#                             Date : 31/05/2022
#################################################################################################

#list
fruits = ['mango','grapes','orange','lemon']
#replace 'orange with apple'
fruits[2]='apple'
print(fruits)

#tuple-to access use the index
new_fruits = ('Mango','Grapes','Apple','Lime')
print(new_fruits[1])

#cars example-editing a tuple
cars = ('audi','bmw','vw','toyota')
cars = ('nissan','bmw','vw','toyota')
print(cars)

#favorite foods example-accessing a tuple using a for loop
fave_foods = ('fries','pizza','chicken','rice','chapati')
for fave_food in fave_foods:
    print(fave_food)
