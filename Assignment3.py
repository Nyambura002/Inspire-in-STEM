#!/usr/bin/python

#Write a program that gets user input and adds ksh 10,000 to her account if she is btwn 25-30 yrs.
age = input("How old are you?")
account_balance = 0
if (int(age) > 25) and (int(age) < 30):
    account_balance = account_balance + 10000
    print("Confirmed. You have received ksh 10,000.")
else:
    print("Sorry. You are not eligible for this service.")
