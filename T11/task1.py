num1 = 4
num2 = 7 
num3 = 2

if num1 > num2:
    print(num1)
else:
    print(num2)
if num1 % 2 != 0:
    print(f"{num1} is odd")
else:
    print(f"{num1} is even")
#sort
if num1 > num2 and num2 > num3:
    print(f"{num1},{num2}, {num3}")
elif num1 > num3 and num3 > num2:
    print(f"{num1},{num3}, {num2}")
elif num2 > num1 and num1 > num3:
    print(f"{num2}, {num1}, {num3}")
elif num2 > num3 and num3 > num1:
    print(f"{num2},{num3}, {num1}")
elif num3 > num1 and num1 > num2:
    print(f"{num3}, {num1}, {num2}")
else:
    print(f"{num3},{num1}, {num2}")

