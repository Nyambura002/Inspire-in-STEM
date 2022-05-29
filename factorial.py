#!/usr/bin/python


#################################################################################################
#                                 FACTORIALS
#                             Name : Faith Njuguna
#                             Date : 27/05/2022
#################################################################################################

#factorials of numbers
number = (int(input("Enter the number")))
factorial = 1
if (int(number)) < 0:
    print("Factorial of -ve number does not exist")
elif number == 0:
    print("Factorial of 0 = 1")
else: 
    for i in range (1,(int(number))+1):
        factorial = factorial*i
print("Factorial of the number is:", factorial)
