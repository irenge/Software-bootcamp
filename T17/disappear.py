x = input("Enter a string: ")
print(f"You entered: {x}")
c = input("Which characters you would like to make disappear: ")
if (len(c) > 1):
    lst = list(c)
    for i in lst:
        x = x.replace(i, '')
else:
    x = x.replace(c,'')

print(x)
