#!/usr/bin/python

#A dictionary is a collection of key value pairs
#syntax : dictionary = {'key':'value'}
from tkinter.font import names


colors = {'color':'red'}
vehicle = {'type':'Toyota' , 'plate_number':'KYZ404A'}
print(type(colors))
#print (type(names)) - we use the type method

#Accessing values of an element in a dictionary - we use the key 
print(vehicle['type'],vehicle['plate_number'])

#Person dictionary
person = {'name':'Faith' ,
          'id_numer':'7872' , 
          'phone_number':'0711223344' ,
          'address':'1406-777'}
print(person['name'],person['id_numer'],person['address'],person['phone_number'])
#Adding a key in a dictionary
person['age'] = '21'
person['favorite_artist'] = 'Bensone Moone'
person['favorite_color'] = 'Black'
print(type(person))
print(person)


#Deleting an element from a dictionary
print(person['name'],person['age'],person['favorite_color'])
del person['phone_number']
print(person)

#Looping in dictionaries - for arranging
for key, value in person.items():
    print(f"{key}:{value}")

colors = ["red", "green", "blue", "orange"]

i = 1
while i <len(colors):
    if(colors[0]=='red'):
        print(colors[0].upper())
        i +=1

i = 1
while i <len(colors):
    if(colors[1]=='green'):
        print(colors[1].upper())
        i +=1

i = 1
while i <len(colors):
    if(colors[2]=='blue'):
        print(colors[2].upper())
        i +=1

i = 1
while i <len(colors):
    if(colors[3]=='orange'):
        print(colors[3].upper())
        i +=1

        