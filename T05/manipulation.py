str_manip = input("Enter a sentence: ")

# calculate and display the length

length = len(str_manip)
print(length)

l = length -1
last_letter = str_manip[length - 1]

print("Last letter: "+last_letter)

rep_str_manip = str_manip.replace(last_letter, "@")
print(rep_str_manip)

# print the last 3 characters in str_manip backwards

print(str_manip[l:l-3:-1])

# create a five-letter word

five_letter = str_manip[:3] + str_manip[l-1:]

print(five_letter)

# display each word on new line

print(str_manip.replace(" ", "\n"))
