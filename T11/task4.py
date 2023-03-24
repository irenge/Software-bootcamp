"""
Create a program that asks the user to enter an integer and determine if it
is:
divisible by 2 and 5,
divisible by 2 or 5,
not divisible by 2 or 5
Display your result
"""
x = int(input("Enter an integer: "))
if x % 2 == 0 and x % 5 == 0 :
    print("divisible by 2 and 5")
elif x % 2 == 0 or x % 5 == 0:
    print("divisible by 2 or 5")
elif x % 2 == 1 or x % 5 != 0:
    print("not divisible by 2 or 5")

