x = []
p = []
total = 0

for i in range(3) :
     x.append(input(f"Enter product No {i+1}: "))

for i in range(3):
    p.append(int(input(f"What is the price of {x[i]}: ")))
    total = total + p[i]

avg = round(total/3)
print()
print(f"The total of {x[0]}, {x[1]}, {x[2]} is {total} and average price of the items  is {avg}")
