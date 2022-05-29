#!/usr/bin/python

#################################################################################################
#                      GEOMETRIC PROGRESSION ASSIGNMENT
#                             Name : Faith Njuguna
#                             Date : 27/05/2022
#################################################################################################

#a = first number, d = common difference, n = number of terms
a = (int(input("Enter the first number:")))
r = (int(input("Enter the common ratio:")))
n = (int(input("Enter the number of terms:")))
for i in range (1,n+1):
    n_term = a*(r**(n-1))
    n_term = a*(r**(i-1))
    print(n_term)
