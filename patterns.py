#!/usr/bin/python

#################################################################################################
#                  PROGRAM FOR PRINTING A PATTERN OF NUMBERS
#                             Name : Faith Njuguna
#                             Date : 27/05/2022
#################################################################################################

rows = (int(input("Enter the number of rows:")))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end = " ")
    print("\n")
