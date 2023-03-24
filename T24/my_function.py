import calendar

# Create your own function that prints all the days of the week.

def print_days():
    for i in range(7):
        print(calendar.day_name[i], end="")
        if i < 6:
            print(end = ", ")
        else:
            print()

# Create your own function that takes in a sentence and replaces every second word with the word “Hello”.

def sentence_replace(word):
    x = word.split(" ")
    y = len(x)
    for i in range(y):
        if i % 2 == 1:
            x[i] = "Hello"
    return " ".join(x)

print(" === TESTING === ")
print("first function")
print_days()
print("second function")

sample = "William Shakespeare was an English playwright, poet and actor. He is widely regarded as the greatest writer in the English language and the world's pre-eminent dramatist. He is often called England's national poe"

#print(sample)
#print("================After replacing ============")
print(sentence_replace(sample))
