#!/usr/bin/python
# Name : Faith Njuguna      
# Date : 3/06/2022

#Create a class vehicle with two instances:maximum speed and mileage
class Vehicle:
    def __init__(car, max_speed, mileage):
        car.speed = max_speed
        car.mileage = mileage

    def v_details(car):
        print('This vehicle has a maximum speed of '+str(car.speed) + ' km/h' + ' and a mileage of '+str(car.mileage))

toyota = Vehicle(420, 75)  
toyota.v_details()

print(toyota.speed, toyota.mileage)