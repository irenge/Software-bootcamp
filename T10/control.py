# Write code to take in a user’s age using input() and store their age in an integer variable called age.
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough!")
elif age >= 16:
    print("“Almost there”")
else:
    print("You’re just too young!")
