# program that calculates a person's BMI
weight = float(input("Enter their weight in kg: "))
height = float(input("Enter your hieght in m: "))

bmi = weight / (height * height)

if bmi >= 30:
    print("You are obese")
elif bmi >= 25:
    print("You are overweight")
elif bmi >= 18.5:
    print("You are normal")
else:
    print("You are underweight")


