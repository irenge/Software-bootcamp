'''x = input("Type a string here: ")
print(x)
for i in range(0, len(x)):
    if i % 2 == 0:
        x = x[:i] + x[i:].capitalize()
print(x)
'''


# reads in a string and makes each alternate character an uppercase character and each other alternate character a lowercase character

y = input("Type a string: ")

print(''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(y)))

# making each alternative word lower and upper case

z = y.split(" ")

print(' '.join(c.upper() if i % 2 == 1 else c.lower() for i, c in enumerate(z)))

