x = int(input("How many students would you like to register ? "))
f = open("reg_form.txt", "w")

f.write("Students Registration form\n")
f.write("==========================\n\n")
f.write("ID  \tSignature\n\n")

for i in range(x):
    id = input("Please enter the ID number: ")
    f.write(id + "\t..........\n")
f.close()
