#!/usr/bin/python

#################################################################################################
#                             Name : Faith Njuguna
#                             Date : 30/05/2022
#################################################################################################
#Task 1
#Write a program to check if a number is divisible by 5 or 7
input = input("Enter a number:")
x = int(input)
if (int(x%5==0)) and (int(x%7==0)):
    print(f"The number {x} is divisible by 5 or 7")
else:
    print(f"The number {x} is not divisible by either 5 or 7")


num = 20
num+= num    #num(20)+num(20)=40
print(num)

#Task 2
#Enter your name so we can customize the greetings
prompt = "Enter your name so we can customize the greetings"
prompt+= "\n Enter your name:"
print("Hello",input(prompt))


name = ['Luke']
email = ['luke27@gmail.com']
password = ['2013abcd']

person = { 
    'Name':[name],
    'Email-address':[email],
    'Password':[password]
}
print(person)
