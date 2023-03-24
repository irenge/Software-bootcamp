import math

while True:
    x = input("Enter 10 numbers separated by a space here: ")
    x = x.split(" ")
    if len(x) < 10:
        x = list(x)
        for i in range(len(x),10):
            x.append(input(f"Enter the number/decimal at position {i}: "))
            if i==9:
                print("Thank you")
    if len(x) == 10:
        break
    print("Please enter 10 numbers/decimals separated by a space !")

while '' in x:
    x.remove('')
while ',' in x:
    x.remove(',')

y = [float(i) for i in x]

# total of all the numbers and print the result
total = sum(y)
print(f"Total = {total}")

# Find the index of the maximum and print the result.

mx = max(y)
print(f"Maximum number/decimal = {mx}")

# Find the index of the maximum and print the result.

for i in range(len(y)):
    if y[i] == mx:
        j = i
        break
print(f"index of the maximum number = {j}")


# Calculate the average of the numbers and round off to 2 decimal places. Print the result.

average = round(total / len(y), 2)

print(f"Average = {average}") 

# Find the median number and print the result.
y = sorted(y)
midnum = len(y) // 2
median = (y[midnum] + y[~midnum]) / 2

#median = statistics.median(y)

print(f"Median number = {median}")


