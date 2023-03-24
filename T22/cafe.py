menu = ["vegan cheese", "chicken", "Cake", "Tea"]
stock ={"vegan cheese":3, "chicken":7, "Cake":9, "Tea":12}
price = {"vegan cheese":2, "chicken":6, "Cake":4, "Tea": 2}

total_worth = 0

for item in menu:
    total_worth += stock[item] * price[item]

print(f"The total worth is {total_worth})
