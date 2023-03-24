year = int(input("What year do you want to start with? "))
number = int(input("How many years do you want to check? "))
for i in range(year, year + number):
    if i % 4 == 0:
        print(f"{i} is a leap year")
    else:
        print(f"{i} isn't a leap year")
