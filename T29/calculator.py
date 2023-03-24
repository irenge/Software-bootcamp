from pathlib import Path

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
# this prints message if the number is divide by zero
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Division by zero is not allowed.\nThis will not be written to file"
def remainder(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "integer modulo by zero is not allowed.\nThis will not be written to file"

def calculate(num1, op, num2):
    if op == '+':
        return add(num1, num2)
    elif op == '-':
        return subtract(num1, num2)
    elif op == '*':
        return multiply(num1, num2)
    elif op == '/':
        return divide(num1, num2)
    elif op == '%':
        return remainder(num1, num2)

# Function that enters and  write data to file 
def manual_entry():
    # create a file in write mode
    f = open("input.txt", "a")
    # read numbers and operator
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again ...")
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again ...")
    cont = True
    while cont:
        try:
            operator = input("Enter operator: ")
            # if else statement to print the answer for the given operator
            if operator in ('+', '-', '*', '/', '%'):
                res = calculate(num1, operator, num2)
                break
            else:
                print("Please enter +, -, *, / or %")
        except UnboundLocalError:
            print("Oops! Enter correct operator")
    if isinstance (res, float):
        f.write(str(num1)+" "+operator+" "+str(num2)+"\n")
        f.close()


def file_entry():
    path = Path('./input.txt')
    ligne = []
    lignes = []
    if path.is_file():
        count = 0
        while True:
            xfile = input("Enter the name of the file: ")
            try:
                file = open(xfile, 'r')
                break
            except FileNotFoundError:
                print("The file that you are trying to open does not exist")
                count += 1
            if count > 11:
                raise Exception('Wrong file name entered {} times'.format(count))
        line = file.readlines()
        for lines in line:
            lines = lines.split(" ")
            for ln in lines:
                ln = ln.strip()
                ligne.append(ln)
            lignes.append(ligne)
            ligne = []
        sz = len(lignes)
        for i in range(sz):
            x = float(lignes[i][0])
            y = float(lignes[i][2])
            o = lignes[i][1]
            r = calculate(x,o,y)
            print(f"{x} {o} {y} = {r}")
        

    else:
        print("Consider choosing the first option first as the file to read from does not exist")

# Function that 
while True:
    print("Would you rather enter numbers and operator or read them from the stored file") 
    choice = input('''Press 
                1 (for manual entering data to process)
                2 (for reading from file)
                3 (to quit)
                ''')
    if choice == '1':
        manual_entry()
    elif choice == '2':
        file_entry()
    elif choice == '3':
        break
    else:
        print("Invalid choice")

    # chose whether to continue or not

    cont = input("Continue - Y / No - N: ")
    
    if cont == "N":
        break
    elif cont == "No":
        break
    elif cont == "Y":
        continue
    elif cont == "y":
        continue
    else:
        print("Invalid Choice: Restarting...\n")
