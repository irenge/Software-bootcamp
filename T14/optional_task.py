x = int(input("Enter a number less than or equal to 100: "))

while x > 100:
    x  = int(input(f"You entered {x} \nPlease enter a number less than or equal to 100: "))

if x % 2 == 0:
    x *= 2
else:
    x *= 3
print (f"result: {x}")

