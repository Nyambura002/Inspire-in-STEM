




from tkinter import N


school = ["Joy", "Peace", "Hope", "Light"]
pupil = ["James", "John", "Luke", "Matthew"]

#Hard way
print(f"{pupil[0]} goes to {school[0]} school")
print(f"{pupil[1]} goes to {school[1]} school")
print(f"{pupil[2]} goes to {school[2]} school")
print(f"{pupil[3]} goes to {school[3]} school")

#Simpler way-using loops
for pupil in pupil:
   print(f"Hello I am pupil {pupil}")
for school in school:
    print(f"I go to {school}")
    
print("Number\tsquare")
print("===================")
for number in range(0,9):
   print(number)
   print(number**2)
   print("\t")




