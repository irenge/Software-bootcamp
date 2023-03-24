sentence = input("Enter the sentence: ")

for i in range(len(sentence)):
    print(sentence[i], end="")
    if sentence[i] == " ":
        print()
print()

