#!/usr/bin/python

#lesson on methods
name = "Faith Njuguna"
name = "Ada Lovelace"
user_name= "Lovelace"
age = 18
age = 55
person = "I am " +str(name) + " and my age is " +str(age)
print (person)


# the format () method one
#print ( "My name is {} and I am {} years old " .format(name,age))
print ("My name is {} and I am {} years old ".format(name,age))
#method two
print(f"My name is {name} and I am {age} years old")


#new line \n and tab \t
print(f"My \t name is {name} \n and I am {age} years old")
print(name, age)

print(user_name.rstrip())
print(user_name.lstrip())

print("Monday\tTuesday\tWednesday\tThursday\tFriday\tSaturday\tSunday")
print("Kisumu\nNyeri\nKiambu")


