incorrect = []
while (x := input("Enter your name: ")).lower() != "john":
    incorrect.append(x)
if incorrect:
    print(f"Incorrect names: {incorrect}")
else:
    print(x)
