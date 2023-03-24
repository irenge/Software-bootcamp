#This program will be used to calculate the area that the foundation of a building covers
# Import math Library
import math

x = input("Enter the shape of the building (square, rectangular or round): ")
if x == "square":
    y = float(input("Enter the length of a side: "))
    area = y * y
elif x == "rectangular":
    a = float(input("Enter the length: "))
    b = float(input("Enter the side: "))
    area = a * b
elif x == "round":
    r = float(input("Enter the radius: "))
    area = math.pi * r * r
else:
    print(f"Please enter the correct shape, you entered {x}")
if x == "square" or x == "rectangular" or x == "round":
    print(f"The area of {x} is {area}")

