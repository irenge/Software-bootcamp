# Create a while loop that will display count down from 20 to 0.
i = 20
while i >= 0:
    print(i, end=" ")
    i -= 1
print()
print()
# create a loop (any) that will display all the even numbers between 1 and 20.
for j in range(1, 20):
    if j % 2 == 0:
        print(j, end=" ")

print()
print()
'''
z = ""
for k in range (1, 6):
    z = z + "*"
    print(z)
print()


print()
print()
'''
#  * printing
for i in range(6):
    for j in range(i+1):
        print("*", end="")
    print("\n")

# write the code to compute the greatest common divisor (GCD, or highest common factor) of two positive integers.
num1 = 1000000

num2 =  500255750

gcd = 1

for i in range (min(num1, num2), 0, -1):
     if num1 % i == 0 and num2 % i == 0:
         gcd = i
         break
print("GCD of", num1, "and", num2, "is", gcd)

