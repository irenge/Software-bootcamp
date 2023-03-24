f = open("user.txt", "r")
lines = f.read()

print(lines)
f_dict = {}

for line in f:
   k, v = line.split(', ')
   f_dict[k] = v.strip('\n')

print(f_dict)

while True:
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if (username not in f_dict) and (password not in f_dict.values()):
        print("Wrong username and password")
    elif username in f_dict:
        correct_pass = f_dict.get(username)
        if correct_pass == password:
            print("Log in")
        else:
            print("Please enter the correct password")
    else:
        print("Please enter a correct username: ")

   #line)
'''
f = open("user.txt", "r+")
line = f.readlines()
users = []
password = []

for ln in line:

    print(ln)
    ln = ln.strip(' ')
    print(" ===")
    print(ln)
    ln = ln.split(', ')
    print("+++++")
    print(ln)
    
    for i in range(len(ln)):
        if i % 2 == 0:
            users.append(ln[i])
        else:
            password.append(ln[i])

for i in range(len(users)):
    print(f"{i}  {users[i]}  {password[i]}")



print(len(users))

x = input("Enter username")
if x == "admin":
    print("Logged in ")
f.close()
'''
