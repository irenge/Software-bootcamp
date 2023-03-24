contents = ""
with open('DOB.txt', 'r+') as f:
    line = f.readlines()
    for i in range(len(line)):
        line[i] = line[i].strip('\n').split()
    
    print("Name")
    for i in range(len(line)):
        for j in range(2):
            print(line[i][j], end=" ")
        print()
    print()
    print("Birthdate")
    for i in range(len(line)):
        for j in range(2,4):
            print(line[i][j], end=" ")
        print()

f.close()
