#!/usr/bin/python
# Name : Faith Njuguna      
# Date : 3/06/2022

# Creating a random password generator
import random
print("Welcome to our password generator!")
username = input("Enter your username: ")
email = input("Enter your e-mail: ")
phone_no = input("Enter your phone number: ")
character = str("Nyambu2003!##")
num_password = int(input("Enter the number of passwords you want to generate: "))
password_length = int(input("Enter the desired length of the password: "))
print("\n Here are your passwords: ")

for password in range(num_password):
    password = " "
    for c in range(password_length):
        password += random.choice(character)
        print(password)
