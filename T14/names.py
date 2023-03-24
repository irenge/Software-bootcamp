i = 0
while True:
    name = input(f"Enter pupil name {i} (Type Stop to end) in your class: ")
    if name == "Stop":
        break
    i += 1
print(f"You entered {i} names")


