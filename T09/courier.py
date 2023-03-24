price = float(input("Enter the price of the package you would like to purchase: "))
print(f"you entered current cost {price}")

distance = float(input("Enter the total distance of the delivery in kms: "))

pref_one = input("Would you prefer air or freight: ")

if pref_one == "air":
    print(f"Adding {pref_one} cost : total cost = {price} + 0.36 * {distance}")
    total = price + 0.36 * distance
else:
    print(f"Adding default (freight) : total cost = {price} + 0.25 * {distance}")
    total = price + 0.25 * distance

print(f"Current cost is now {total}")

insurance = input("About insurance: would you prefer full or limited: ")

if insurance == "full":
    print(f"Adding {insurance} insurance : total cost = {total} + 50.00")
    total = total + 50.00
else:
    print(f"Adding (default) limited insurance: total cost = {total} + 25.00")
    total = total + 25.00
print (f"Current cost is now  {total}")

gift = input("Would you prefer a gift or no gift: ")

if gift == "gift":
    print("Gift will cost 15.00")
    total = total + 15.00
else:
    print ("No cost for gift")

print (f"Current cost is now  {total}")

delivery = input("About Delivery: Would you prefer a priority or standard ? ")

if delivery == "priority":
    print("Priority will cost you 100 quid more")
    total = total + 100.00
else:
    print("Standard or default one will cost you 20 quid more")
    total = total + 20.00

print(f"The total cost is {total}")
