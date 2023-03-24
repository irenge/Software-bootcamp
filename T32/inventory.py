from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost 
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"Shoe({self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity})"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data(shoe_list):
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    
    f = None
    try:
        f = open ("inventory.txt", "r")
        lines = f.readlines()[1:]
        for line in lines:
            line = line.strip().split(",")
            line[3] = int(line[3])
            line[4] = int(line[4])
            shoe_list.append(Shoe(line[0], line[1], line[2], line[3], line[4]))
    except FileNotFoundError:
        print("\nThe file that you are trying to open does not exist")
    finally:
        if f is not None:
            f.close()

# Check if database is loaded, if not load

def check(shoe_list):
    if len(shoe_list) <= 0:
        read_shoes_data(shoe_list)

def capture_shoes(shoe_list):
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    check(shoe_list) 

    while True:
        country = input("Enter your country: ")
        if len(country) > 1:
            break
        print("Please! ", end="")
    while True:
        code = input("Enter country code: ")
        if len(code) > 1:
            break
        print("Please! ", end="")
    while True:
        product = input("Enter product name: ")
        if len(product) > 1:
            break
        print("Please! ", end="")
    while True:
        try:
            cost = int(input("Enter the cost: "))
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again...")

    while True:
        try:
            quantity = int(input("Enter the quantity: ")) 
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
    
    x = Shoe(country, code, product, cost, quantity)
    
    shoe_list.append(x)
    print("Added to database")

    ## add to file 
    w = f"{x.country},{x.code},{x.product},{x.cost},{x.quantity}\n"
    f = open("inventory.txt", "a")
    f.write(w)
    f.close()

def view_all(shoe_list):
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    
    check(shoe_list)

    all_data = [["Country","Code","Product", "Cost", "Quantity"]]
    print("1. Viewing data as a list of object\n")
    for l in shoe_list:
        print(l)
        all_data.append([l.country,l.code,l.product,l.cost,l.quantity])
    print()
    print("2. Optionally: Viewing data on a table")
    print(tabulate(all_data,headers='firstrow',tablefmt='grid'))
    print()

def re_stock(shoe_list):

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    k = 0 
    check(shoe_list)
    minimum = shoe_list[k].get_quantity()
    for j in range(len(shoe_list)):
        if shoe_list[j].get_quantity() < minimum:
            minimum = shoe_list[j].get_quantity()
            k = j
    print("The below item needs restock:")
    print(shoe_list[k])
    while True:
        user_input = input("Would you want to add 50 shoes to restock? Yes/Y/N/No ").lower()
        if (user_input == "yes") or (user_input == 'y'):
            shoe_list[k].quantity += 50
            print("Added 50")
            f = open ("inventory.txt", "r")
            lines = f.readlines()[1:]
            lines[k] = f"{shoe_list[k].country},{shoe_list[k].code},{shoe_list[k].product},{shoe_list[k].cost},{shoe_list[k].quantity}\n"
            f = open("inventory.txt", "w")
            f.writelines(lines)
            f.close()
            break
        elif (user_input == "no") or (user_input == "n"):
            print("Ok")
            break
        else:
            print("Please answer Yes or No")

def search_shoe(code, shoe_list):

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    check(shoe_list)

    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    return None

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    check(shoe_list)

    table_cost = [["Shoe name","Cost","Quantity", "Total value"]]
    values = []
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        values.append(value)
        table_cost.append([shoe.product,shoe.get_cost(), shoe.get_quantity(), value])
    print(tabulate(table_cost,headers='firstrow',tablefmt='fancy_grid'))
    total = sum(values)
    print(f"Stock total Value : £{total}")


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    check(shoe_list)
    q = 0
    for shoe in shoe_list:
        if shoe.quantity > q:
            q = shoe.quantity
            for_sale = shoe
    print(for_sale)
    print(f"This {for_sale.product} is for sale")
#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    menu = input('''Select one of the following Options below:
l  - Load shoe database (automatic)
a  - Add shoe product to database(manual)
va - View all shoes in the stock/database
u  - Update lowest stock item
s  - Search for a shoe
v  - Value of each shoe in stock 
h  - Display shoe for sale - stock highest quantity 
e  - Exit
: ''').lower()
    if menu == 'l':
        read_shoes_data(shoe_list)
        print("Database loaded")
    elif menu == 'a':
        print()
        capture_shoes(shoe_list)
        print()
    elif menu == 'va':
        print()
        view_all(shoe_list)
        print()
    elif menu == 'u':
        re_stock(shoe_list)
    elif menu == 's':
        code = input("Enter the product code to search: ")
        found = search_shoe(code, shoe_list)
        if found == None:
            print("Not found")
        else:
            print(found)
            #print(f"{found.country},{found.code},{found.product},{found.cost},{found.quantity}")
            print()
    elif menu == 'v':
        print()
        value_per_item()
        print()
    elif menu == 'h':
        print()
        highest_qty()
        print()
    elif menu == 'e':
        print()
        print("Good bye!")
        break
    else:
        print()
        print("Invalid choice")
        print()
