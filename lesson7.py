#!/usr/bin/python
#####################################################################################
#                             Dictionaries
#                             Name : Faith Njuguna
#                             Date : 23/05/2022
#####################################################################################

# Initializing dictionaries

student = {"Name":"Faith", "age": 24 , "gender": "Female", "Hobby":"Swimming"}
print(student["Name"])
print(student["Hobby"])
print(student["age"])
print(student["gender"])

student["IdNo"] = "7872"
student["Hobbies"] = "Reading"
student["colour"] = "Black"
print(student["IdNo"])
print(student["colour"])
print(student["Hobbies"])
print(student)

student = {}
student["fave_food"] = "Fries"
student["home_city"] = "Nairobi"
print(student["home_city"])
print(student)

#Modifying values
student["Name"] = "Luke"
print(student["Name"])

#Removing values
del student["fave_food"]
print(student)

