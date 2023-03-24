from pathlib import Path
from datetime import datetime 
import sys
def printf(format, *args):
    sys.stdout.write(format % args)

'''def month_string_to_number(string):
    m = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr':4,
            'May':5,
            'Jun':6,
            'Jul':7,
            'Aug':8,
            'Sep':9,
            'Oct':10,
            'Nov':11,
            'Dec':12
        }
    s = string.strip()[:3]
    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')
        '''
i = 7
pi = 3.14159265359
printf("Hi there, i=%d, pi=%.2f", i, pi)

my_file  = Path("./task_overview.txt")
if not my_file.exists():
    print("Does not Exits")
else:
    print("Exist nah")
g = open("tasks.txt", "r+")
#line = g.readlines()
g_dict = {}

g_list = []
g_line = g.readlines()

for i in range(len(g_line)):
    print(i)
    g_line[i] = g_line[i].strip().split(',')
    g_dict = {"ID":i,"Task":g_line[i][1],"Assigned to":g_line[i][0],"Date":g_line[i][4],"Due date":g_line[i][3], "Task Complete?": g_line[i][5], "Task description": g_line[i][2]}
    g_list.append(g_dict)

print(g_line)
print(g_list)
print()
print()
for gc in g_list:
    if gc['Assigned to'] == 'charles':
        print(g_list[i])
ccount = 0
ucount = 0
for gr in g_list:
    print(gr["Date"])
    #print(gr["Due date"])
    #print(type(gr["Due date"]))
    #due_date = gr["Due date"].strip(" ").split(" ")
    print(datetime.strptime(gr["Due date"].strip(), '%d %b %Y'))
    print(datetime.strptime(gr["Date"].strip(), '%d %b %Y'))
    print((datetime.strptime(gr["Due date"].strip(), '%d %b %Y')) > (datetime.strptime(gr["Date"].strip(), '%d %b %Y')))

print() 
if gr["Task Complete?"].strip() == 'Yes':
    ccount += 1
else:
    ucount += 1

print (ccount)
print(ucount)
print(len(g_list))
