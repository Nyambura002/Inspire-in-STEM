#!/usr/bin/python

#################################################################################################
#                           ACCESSING AND EDITING TEXT FILES
#                             Name : Faith Njuguna
#                             Date : 6/06/2022
#################################################################################################

f = open("lesson.txt") 

#Creating a new file
#f = open("lesson1.txt",'x') 

#Reading the file:
print(f.read())
f.close

#Opening and editing the new file: (w)
with open("lesson1.txt",'w') as f:
    f.write("This is the new file\n")
    f.write("I live in Edenville\n")
    f.write("Coding is an interesting skill :) \n")
    f.write("To a great week ahead!")

#Reading line by line
f = open("lesson1.txt")
print(f.readline())


print(f.seek())
print(f.read())
print(f.tell())