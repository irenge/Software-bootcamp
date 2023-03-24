#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
from datetime import datetime
import calendar
from pathlib import Path
import math

# ========== Functions  ============

def reg_user():
    while True:
        user = input("Enter Username: ").lower()
        if user not in f_dict:
            break
        print("Username already existed. Please add a user with a different username")
    password = input("Enter password : ")
    conf_pass = input("Enter again your password to confirm: ")
    if password == conf_pass:
        f.write(user+", ")
        f.write(password +'\n')
        #track_usersg += 1
        return 1
    else:
        print("\nPasswords did not match !!!\n")
        return 0

def add_task():
    user = input("Enter the username: ")
    title_task = input("Enter the title of the task: ")
    desc_task = input("Enter the description of the task here: ")
    while True:
        date_entry = input('Enter the due date in DD/MM/YYYY format: ')
        if len(date_entry) < 10:
            print("Incorrect date")
        else:
            day, month, year = map(int, date_entry.split('/'))
            if (day > 31) or (day < 1):
                print("Please enter correct date")
            else:
                break
    due_date = f"{day} {calendar.month_abbr[month]} {year}"
    today = datetime.today().strftime('%d %b %Y')

    is_complete= input("Is the task complete? (Yes/No) ") or "No"
    g.write(user +", " + title_task + ", " + desc_task + ", " + due_date + ", " + today + ", " + is_complete + "\n")
    return 1
#f.close()

def view_all():
    f = open("tasks.txt", "r")
    line = f.readlines()
    for i in range(len(line)):
        line[i] = line[i].split(', ')
        print(f"Task:\t{line[i][1]}\nAssigned to:\t{line[i][0]}\nDate assigned:\t{line[i][4]}\nDue date:\t{line[i][3]}\nTask Complete?\t{line[i][5]}\nTask description:\n  {line[i][2]}")
        print()
    f.close()

def generate():
    t = open("task_overview.txt", "w")
    total_task = len(g_list)
    ccount = 0
    ucount = 0
    ocount = 0
    ovcount = 0
    for gr in g_list:
        if gr["Task Complete?"].strip() == 'Yes':
            ccount += 1
        else:
            ucount += 1
        if (datetime.strptime(gr["Due date"].strip(), '%d %b %Y')) < (datetime.strptime(gr["Date"].strip(), '%d %b %Y')):
            if gr["Task Complete?"].strip() == 'No':
                ocount += 1
            ovcount += 1
    pti = math.floor((ucount / total_task) * 100)
    ptov = math.floor((ovcount / total_task) * 100)
    t.write(f"Total number of tasks: {total_task}\n")
    t.write(f"Total number of completed tasks: {ccount}\n")
    t.write(f"Total number of incompleted tasks: {ucount}\n")
    t.write(f"Total overdue incompleted tasks: {ocount}\n")
    t.write(f"Percentage of incompleted tasks: {pti}\n")
    t.write(f"Percentage of overdue tasks: {ptov}\n")
    t.close()

    l = len(f_dict)
    u = open("user_overview.txt", "w")

    u.write(f"Total number of users: {l}\n")
    u.write(f"Total number of tasks: {total_task}\n")

    for k, v in f_dict.items():
        kcount = 0
        kccount = 0
        kucount = 0
        kocount = 0
        for gc in g_list:
            if gc['Assigned to'] == k:
                kcount += 1
                if gc["Task Complete?"].strip() == 'Yes':
                    kccount += 1
                else:
                    kucount += 1
                    if (datetime.strptime(gc["Due date"].strip(), '%d %b %Y')) < (datetime.strptime(gc["Date"].strip(), '%d %b %Y')):
                        kocount += 1
        u = open("user_overview.txt", "a")
        u.write(f"\nuser: {k}\n")
        u.write(f"Total number of tasks assigned :{kcount}\n")
        pk = round((kcount / total_task) * 100)
        u.write(f"Percentage of task assigned: {pk}\n")
        if kcount == 0:
            pct = 0
            pit = 0
            pcto = 0
        else:
            pct = math.floor((kccount/kcount) * 100)
            pit = math.floor((kucount/kcount) * 100)
            pcto = math.floor((kocount / kcount) * 100)

        u.write(f"Percentage of completed assigned task: {pct}\n")
        u.write(f"Percentage of still to be completed: {pit}\n")
        u.write(f"Percentage overdue not completed of assigned tasks: {pcto}\n")

        u.close()


'''

Display all tasks in a manner that is easy to read. Make sure that
each task is displayed with a corresponding number which can be
used to identify the task.

'''
def display(my_list):
    l = 1
    for j in my_list:
        print(f"Task No {l}")
        for k, v in j.items():
            print(f"\t{k}: {v}")
        l += 1
    print()
def view_mine(g_list, my_list, indices):
    for gc in g_list:
        if username == gc['Assigned to']:
            if len(my_list) == 0:
                my_list.append(gc)
            else:
                for i in range(len(my_list)):
                    indices.append(my_list[i]['ID'])
                if gc['ID'] not in indices:
                    my_list.append(gc)
    print()
    print()
    length = len(my_list)
    print(f"{length} task(s) allocated")
    print()

    display(my_list)
     
    while True:
        x = int(input('''
        
        Please select the task number you would like to work in:
        -1 or 0 to return to Main Menu

                      ''')
                )
        if x == -1 or x == 0:
            break
        x = x - 1
        if x >= length:
            print(f"Please select a maximum of {length}")
        elif x < length:
            for k, v in my_list[x].items():
                print(f"\t{k}: {v}")
            print()
        try:
            y = int(input('''Type either 1 or 2
                                 1 - mark the task as complete
                                 2 -  edit the task.
                              ''')
                        )
        except ValueError:
            print("Value error: Please enter number")
        if y == 1:
            my_list[x]["Task Complete?"] = "Yes"
            for k,v in my_list[x].items():
                print(k,':',v)
            break
        elif y == 2:
            if my_list[x]["Task Complete?"] == "Yes":
                print("Task can not edited as it s complete")
                break
            else:
                 my_list[x]["Assigned to"] = input("Enter the new username to assigned the task to: ")
        else:
            print("Invalid choice: Please enter 1 or 2")
        print()
        '''for j in my_list:
            for k, v in j.items():
                print(f"\t{k}: {v}")
            print()
            '''
    print()


#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

g = open("tasks.txt", "r+")
g_dict = {}
g_list = []
g_line = g.readlines()

track_tasksg = 0
track_usersg = 0

for i in range(len(g_line)):
    g_line[i] = g_line[i].strip().split(',')
    g_dict = {"ID":i,"Task":g_line[i][1],"Assigned to":g_line[i][0],"Date":g_line[i][4],"Due date":g_line[i][3], "Task Complete?": g_line[i][5], "Task description": g_line[i][2]}
    g_list.append(g_dict)

f = open("user.txt", "r+")
f_dict = {}
my_list = []
indices = []

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
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - View Statistics
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
        track_usersg += reg_user()
    elif menu == 'r' and username != 'admin':
        print("You do not have admin privleges")
    elif menu == 'a':
        track_tasksg += add_task()
    elif menu == 'va':
        view_all() 
    elif menu == 'vm':
        view_mine(g_list, my_list, indices)
    elif menu == 'ds':
        my_file  = Path("./task_overview.txt")
        
        if not my_file.exists():
            generate()
         
    
        f = open('task_overview.txt', 'r')
        g = open('user_overview.txt', 'r')

        tlines = f.readlines()
        ulines = g.readlines()
        print("TASKS")
        for line in tlines:
            print(line)
        print("USERS")
        for uline in ulines:
            print(uline)

        f.close()
        g.close()
    elif menu == 'gr':
        generate()
    elif menu == 'e':
        print('Goodbye!!!')
        f.close()
        g.close()
        exit()
    else:
        print("You have made a wrong choice, Please Try again")

