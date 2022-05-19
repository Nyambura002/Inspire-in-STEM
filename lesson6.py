#Learning about lists
motorcycle = ["honda", "yamaha", "suzuki"]
print(motorcycle)

#accessing lists using index
print(motorcycle[0])
print(motorcycle[2])

#changing an element inside a list
motorcycle[0]= "Bugatti"
print(motorcycle)

print("I love "+str(motorcycle[1]))
print("I prefer a "+str(motorcycle[2]))

#adding an element in a list-can only add one item 
motorcycle.append("prado")
print(motorcycle)

#removing an item from a list-use the index to access each item individually
plate_number = ["H1234", "Y1234", "S1234", "P7742"]
print(plate_number[0])
print(plate_number[2])
print(plate_number[1])
print(plate_number[3])
print("My number plate is "+str(plate_number[1]))

#deleting an item from a list-use del before the variable
del motorcycle[0]
print(motorcycle)
del motorcycle[2]
print(motorcycle)

#removing the last item from your list
popped_motorcycle = motorcycle.pop()
print(motorcycle) 

#printing the last item only
print(popped_motorcycle)

#print a statement: My name is Mojo Jojo and I own a motorcycle plate number
motocycle_owner = "Mojo Jojo"
#format
print(f"My name is {motocycle_owner} and I own a {motorcycle[0]} plate number {plate_number[0]}")

#removing an item from a list
motorcycle = ["honda", "yamaha", "suzuki"]
motorcycle.remove("suzuki")
print(motorcycle)