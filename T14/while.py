avg = 0.0
total = 0.0
i = 0
while True:
    x = input("Enter a number: ")
    if x == "-1":
        break
    x = int(x)
    total += x
    i += 1
avg = total/i
print(f"Average is {avg:.2f}")

