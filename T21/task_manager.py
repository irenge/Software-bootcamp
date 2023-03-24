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
f = open("user.txt", "r")
f_dict = {}
for line in f:
   k, v = line.split(', ')
   f_dict[k] = v.strip('\n')
while True:
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if (username not in f_dict) and (password not in f_dict.values()):
        print("Incorrect username and  password")
    elif username in f_dict:
        correct_pass = f_dict.get(username)
        if correct_pass == password:
            break
        else:
            print("Incorrect password")
    else:
        print("Incorrect username: ")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - View Statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r' and username == 'admin':
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        user = input("Enter Username: ")
        password = input("Enter password : ")
        conf_pass = input("Enter again your password to confirm: ")
        if password == conf_pass:
            f = open("user.txt", "a")
            f.write(user+", ")
            f.write(password +'\n')
            f.close()
        else:
            print("\nPasswords did not match !!!\n")
    elif menu == 'r' and username != 'admin':
        print("You do not have admin privleges")
    elif menu == 'a':
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
        user = input("Enter the username: ")
        title_task = input("Enter the title of the task: ")
        desc_task = input("Enter the description of the task here: ")
        while True:
            date_entry = input('Enter the due date in DD/MM/YY format: ')
            if len(date_entry) < 8:
                print("Incorrect date")
            else:
                day, month, year = map(int, date_entry.split('/'))
                if (day > 31) or (day < 1):
                    print("Please enter correct date")
                else:
                    break
        due_date = f"{day} {calendar.month_abbr[month]} {year}"
        today = datetime.date.today().strftime('%d %b %Y')
        is_complete= input("Is the task complete? (Yes/No) ") or "No"
        f = open("tasks.txt", "a")
        f.write(user +", " + title_task + ", " + desc_task + ", " + due_date + ", " + today + ", " + is_complete + "\n")
        f.close()

    elif menu == 'va':
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
            line[i] = line[i].split(', ')
            print(f"Task:\t{line[i][1]}\nAssigned to:\t{line[i][0]}\nDate assigned:\t{line[i][4]}\nDue date:\t{line[i][3]}\nTask Complete?\t{line[i][5]}\nTask description:\n  {line[i][2]}")
            print()
            f.close()
            
    elif menu == 'vm':
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        
        f = open("tasks.txt", "r")
        #g = open("user.txt", "r")
        
        # Read a line from the file

        line = f.readlines()

        for i in range(len(line)):
            line[i] = line[i].strip().split(',')
            if username == line[i][0]:
                    print(f"Task:\t{line[i][1]}\nAssigned to:\t{line[i][0]}\nDate assigned:\t{line[i][4]}\nDue date:\t{line[i][3]}\nTask Complete?\t{line[i][5]}\nTask description:\n  {line[i][2]}")
        f.close()
    elif menu == 's':
        f = open('tasks.txt', 'r')
        g = open('user.txt', 'r')

        total_task = len(f.readlines())
        total_users = len(g.readlines())

        print(f"\nTotal tasks: {total_task}")
        print(f"Total users: {total_users}\n")

        f.close()
        g.close()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
