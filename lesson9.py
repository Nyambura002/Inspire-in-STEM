#!/usr/bin/python


#################################################################################################
#                                   --LOOPS--
#                             Name : Faith Njuguna
#                             Date : 26/05/2022
#################################################################################################

#all even numbers between 0-10
for number in range(0,10):
    if (number % 2 ==0): 
        print(number)

#sum of all even numbers between 0-50
sum_nums = 0    #when you divide and the remainder is 0
prod_nums = 1   #when you divide and the remainder is 1
for number in range (0,50):
    if(number % 2 ==0):
        sum_nums = sum_nums + number
print(sum_nums)

#product of numbers between 0-20
for number in range (0,20):
    if(number % 2 == 1):
        prod_nums = prod_nums * number
print(prod_nums)

num = 0   #initialize the condition
while num < 10 :
    print(num)
    num = num+1

num = 10  #even numbers between 0-10
while num < 10:
    if (num % 2 == 0):
        print(num)
    num = num + 1