#!/usr/bin/python

#################################################################################################
#                                    LISTS
#                             Name : Faith Njuguna
#                             Date : 20/05/2022
#################################################################################################

name = "Faith Njuguna"

msg = '''    QRST126XDG MPESA confirmed
          you have received ksh 2300 from
          James Muoki.
          18th May 2022
          Safaricom transparent for you
          '''
print(msg)


txt = """    Holla! I am Faith Njuguna
          I come from Kiambu county
          I love to read, write and dance. """
print(txt)

city = "Nairobi"
print(city[:5])
print(city[2:])
print(city[-1:])

town = "LasVegas"
print(town[:5])
print(town[:3])
print(town[-1])

f_name = "faith njuguna " # small letters
# .upper() convert to upper case
print (f_name.upper())

s_name = "GRACE NJUGUNA"  #capital letters
# .lower() convert to lower case
print (s_name.lower())

#concatination - converting from one data type to another
#int to float    float(x)
#float to int    int(x)
#int to string   str(x)
number = 7
print(str(number))

x = 4 #4 is an integer 
print(float(x))
print(str(x))

y = 7.883
print(int(y))

f_name = "James"
s_name = "Corden"
full_name = f_name + s_name
print(full_name)

#The replace() method replaces a string with another string
name = "Klaus Michaelson"
print(name.replace('a','e'))
name = "Brent Gooper"
print(name.replace('t','i'))



#The split() method splits the sentence into single words
msg = "Hello from Faith Njuguna how are you "
print(msg.split())
#to get the number of characters in each sentence
print(len(msg))
msg = "My name is Faith Njuguna and coding is really fun"
print(msg.split())
#to get the number of characters in each sentence
print(len(msg))
