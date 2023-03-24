name = input("Enter your name: ")
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Not a valid number")

hair_colour = input("Enter your hair color: ")
eye_color = input("Enter your eye color: ")

class Adult:
    def __init__ (self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
    def can_drive(self):
        print(f"{self.name} is old enough to drive")

class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive")

if age >= 18:
    obj1 = Adult(name, age, hair_colour, eye_color)
else:
    obj1 = Child(name, age, hair_colour, eye_color)

obj1.can_drive()


