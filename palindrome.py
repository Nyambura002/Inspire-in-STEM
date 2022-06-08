#!/usr/bin/python

#################################################################################################
#                             Name : Faith Njuguna
#                             Date : 8/06/2022
#                      Program to check if a number or letter is a palindrome
#################################################################################################

from audioop import reverse
#Method 1
str = input("Enter the number/word: ")
rev = reversed(str)
if list(str)==list(rev):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

