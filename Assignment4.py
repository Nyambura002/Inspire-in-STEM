#!/usr/bin/python

#Write a program to withdraw ksh 25,000 if account balance is btwn ksh 100,000 to 200,000 ; 30% if account balance is btwn 500,000 to 1,000,000 ; if above 1,000,000 deduct 15,000
acc_balance = (int(input ("What is your account balance?")))

if (int(acc_balance) > 100000 and int (acc_balance) < 200000):
    acc_balance = acc_balance - 25000
    print("Ksh 25,000 has been deducted from your account.\n")
elif (int(acc_balance) > 500000 and int (acc_balance) < 1000000):
    acc_balance = acc_balance - (0.3*acc_balance)
    print("We have deducted 30% from your account balance.")
elif (int(acc_balance) > 1000000):
    acc_balance = acc_balance - 15000
    print("Ksh 15,000 has been deducted from your account.")
    

    


