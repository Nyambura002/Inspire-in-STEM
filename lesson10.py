#!/usr/bin/python

#task on dictionaries
mary_fav_food = ['beef','chicken','vegetables']
jane_fav_food = ['rice','ugali','potato']
#Looping in a dictionary containing the above
fave_food = {
    'mary':mary_fav_food,
    'june':jane_fav_food
}
for key, value in fave_food.items():
    print(f"{key}:{value}")