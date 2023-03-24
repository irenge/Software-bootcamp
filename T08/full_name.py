full_name = input("Enter your full name: ")
if  len(full_name) == 0:
    print("You haven’t entered anything. Please enter your full name")
if len(full_name) <= 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
if len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
if len(full_name.split()) <= 1:
    print("Please enter  at least two names: name and surname")
else:
    print("Thank you for entering your full name ")


