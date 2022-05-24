#!/usr/bin/python
#################################################################################################
#                                    SQUARES
#                             Name : Faith Njuguna
#                             Date : 24/05/2022
#################################################################################################


squares = [ ]   #Initializing squares as an empty list
for number in range(0,10):
    square = number**2
    squares.append(square)
print(squares)

cubes = [ ]  #Initializing cubes as an empty list
for number in range(0,10):
    cube = number **3
    cubes.append(cube)
print(cubes)

#sums
sum = 0
for number in range(1,100):
    sum = number + sum
print(sum)
