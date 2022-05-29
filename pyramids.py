#!/usr/bin/python

#################################################################################################
#                  PROGRAM FOR PRINTING A HALF PYRAMID OF STARS
#                             Name : Faith Njuguna
#                             Date : 27/05/2022
#################################################################################################

rows = (int(input("Enter the number of rows:")))
for i in range(rows):
    for j in range(i+1):
        print(" * ",end = " ")
    print("\n")


#################################################################################################
#                          FULL PYRAMID
#################################################################################################
K = 0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print( end = " ")
    while K!=(2*i-1):
        print("*", end = "")
        K+=1
    K=0
    print()
