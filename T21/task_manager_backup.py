#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
import calendar

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
#  Read user.txt file
f = open("user.txt", "r")

users = []
passwords = []
is_correct = False

# read files and save in variable lines 
lines = f.readlines()
for line in lines:
    line = line.strip('\n')
    line = line.strip(' ')
    line = line.split(', ') # split a line into a list
    
    for i in range(len(line)):
        if i % 2 == 0:
            users.append(line[i]) # save usernames
        else:
            passwords.append(line[i]) # save password for usernames


for i in range(len(passwords)):
    print(passwords[i])
    #print(f"{i}  {users[i]}  {passwords[i]}")
   
while(True):
    x = input("Enter username: ")
    y = input("Enter your password: ")
    for i in range(len(users)):
        if x == users[i] and y == passwords[i]:
            print("log in allowed")
            is_correct = True
            a = 3
            break;
        elif x == users[i] and y != passwords[i]:
            a = 1 #print("incorrect password")
            break
        elif x != users[i] and y == passwords[i]:
            a = 2 #print("Incorrect username")
            break
        else:
            a= 4 #print("incorrect username and password")

    if a == 3:
        break
    elif a == 1:
        print("incorrect password")
    elif a == 2:
        print("Incorrect username")
    else:
         print("incorrect username and password")

    #for i,l in zip(users, passwords):
     #   if y == l:
            #print("correct pass")
           # print(f" {i} {l}")
        #if x == i:
         #   print("Log in allowed")
         #if y == l:
          #  print("correct pass")


'''
    for user, password in zip(usernames, passwords):
        print(user)
        print(password)
        if x == user and y == password:
            z = True
            break
        elif x == user  and y != password:
            print("You entered a wrong password")
            continue
        elif x != user and y == password:
            print("Wrong username")
            continue
        else:
            print("Wrong Username and Wrong password")
            continue
'''
while is_correct:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        username = input("Enter Username: ")
        password = input("Enter password : ")
        conf_pass = input("Enter again your password to confirm: ")
        if password == conf_pass:
            f = open("user.txt", "a")
            f.write(username+", ")
            f.write(password +'\n')
            f.close()
        else:
            print("\nPasswords did not match !!!\n")


    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
           
        username = input("Enter the username: ")
        title_task = input("Enter the title of the task: ")
        desc_task = input("Enter the description of the task here: ")
        date_entry = input('Enter the due date in DD/MM/YY format: ')
        day, month, year = map(int, date_entry.split('/'))
        due_date = f"{day} {calendar.month_abbr[month]} {year}"
        today = datetime.date.today().strftime('%d %b %Y')
        is_complete= input("Is the task complete? (Yes/No) ")

        f = open("tasks.txt", "a")
        f.write(username +", " + title_task + ", " + desc_task + ", " + due_date + ", " + today + ", " + is_complete + "\n")
        f.close()

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        f = open("tasks.txt", "r")
        line = f.readlines()
        for i in range(len(line)):
            line[i] = line[i].strip().split(',')
            print(f"Task:\t{line[i][1]}\nAssigned to:\t{line[i][0]}\nDate assigned:\t{line[i][4]}\nDue date:\t{line[i][3]}\nTask Complete?\t{line[i][5]}\nTask description:\n  {line[i][2]}")
            print()
            f.close()
            
    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        
        f = open("tasks.txt", "r")
        g = open("user.txt", "r")
        # Read a line from the file
        uline = g.readlines()
        line = f.readlines()

        for i in range(len(line)):
            line[i] = line[i].strip().split(',')
            for ln in uline:
                ln = ln.split(", ")
                if ln[0] == line[i][0]:
                    print(f"Task:\t{line[i][1]}\nAssigned to:\t{line[i][0]}\nDate assigned:\t{line[i][4]}\nDue date:\t{line[i][3]}\nTask Complete?\t{line[i][5]}\nTask description:\n  {line[i][2]}")
                    continue

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
