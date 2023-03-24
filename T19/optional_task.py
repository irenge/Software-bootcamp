f = open('input.txt', 'r+', encoding='utf-8')
lines = f.readlines()
number_of_lines = len(lines)
number_of_words = 0
lst = []
number_of_characters = 0
count = 0

for i in range(number_of_lines):
    lines[i] = lines[i].strip('\n').split()
    number_of_words = number_of_words + len(lines[i])
    for j in range(len(lines[i])):
        lst.append(list(lines[i][j]))
for i in range(len(lst)):
    number_of_characters = number_of_characters + len(lst[i])
    for j in range(len(lst[i])):
        if lst[i][j] == 'a' or lst[i][j] == 'e' or lst[i][j] == 'i' or lst[i][j] == 'o' or lst[i][j] == 'u':
            count += 1
print(f"number of characters = {number_of_characters}, words = {number_of_words}, lines = {number_of_lines} and number of vowels is {count}")
