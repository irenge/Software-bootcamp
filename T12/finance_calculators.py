import math

user_choice = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
""").lower()

if ((user_choice != "investment") and  (user_choice != "bond")):
    print("Invalid input: Please enter either 'investment' or 'bond'")
elif user_choice == "investment":
    amount = float(input("How much money are you depositing: "))
    rate = float(input("Enter the interest rate: "))
    rate_p = rate/100
    years = int(input("How many years are you planning to invest ? "))
    interest_type = input("Would you like a simple or compound interest? ").lower()
    if interest_type == "simple":
        a = amount * (1 + rate_p * years)
        print(f"The total amount with interest applied is {a:.2f}")
    elif interest_type == "compound":
        a = amount * math.pow((1 + rate_p), years)
        print(f"The total amount with interest applied is {a:.2f}")
    else:
        print(f" {interest_type} is NOT a valid interest type")
elif user_choice == "bond":
    housev = float(input("Enter the value of the house: "))
    annual = float(input("Enter the annual interest rate: "))
    monthly = annual / 12 / 100
    months = int(input("Enter number of month you plan to repay the bond: "))
    x = (monthly * housev) / (1 - (math.pow((1 + monthly), (-months))))
    print(f"Each month, you will pay {x:.2f}")
