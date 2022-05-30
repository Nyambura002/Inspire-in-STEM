#!/usr/bin/python

#Write a program to write numbers in reverse eg-100,99,998,97...
import re


i = int(input("Enter a number to find reverse:"))
rev=0
while(i > 0):
    r=i%10
    rev=rev*10+r
    i=i//10
print("The reverse of given number is:", rev)