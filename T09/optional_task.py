# Design a program for a department store to calculate the monthly wage
# for two different types of employees.

while True:
    x = input("Are you a salesperson or manager? ")

    if x == "salesperson":
        g = int(input("Please enter your gross sales for the month: "))
        salary = 2000 + (8*g/100)
        break
    if x == "manager":
        nh = int(input("Please enter the number of hours worked for the month: "))
        salary = 40 * nh
        break
    print("Please enter salesperson or manager. Thank you.")

print(f"Based on your current work as {x} your monthly wage is {salary}")

