import math

y =[]

k = 1
while k < 11:
    y.append(float(input(f"Enter number {k} at index {k - 1}: ")))
    k += 1

# total of all the numbers and print the result
total = sum(y)
print(f"Total = {total}")

# Find the index of the maximum and print the result.

mx = max(y)
print(f"Maximum number/decimal = {mx}")

# Find the index of the maximum and print the result.

for i in range(len(y)):
    if y[i] == mx:
        print(f"index of the maximum number = {i}")
        break


# Calculate the average of the numbers and round off to 2 decimal places. Print the result.

average = round(total / len(y), 2)

print(f"Average = {average}") 

# Find the median number and print the result.
y = sorted(y)
midnum = len(y) // 2
median = (y[midnum] + y[~midnum]) / 2

#median = statistics.median(y)

print(f"Median number = {median}")


