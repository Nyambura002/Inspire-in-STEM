#!/usr/bin/python

#using if statements and for loops

#using a for loop in a list to print all vehicles
vehicles = ["bmw", "audi", "toyota", "mercedes", "jeep"]    #list
for vehicle in vehicles:    #vehicle is an element in the list
    print(vehicle.title())

#using an if statement
if (vehicle == "jeep"):       #for comparison use ==
    print(vehicle.upper())

#using indexes
print(vehicles[3].upper())



