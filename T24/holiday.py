'''
This function will take the number of nights a user
will be staying at a hotel as an argument, and return a total cost for
the hotel stay (You can choose the price per night charged at the
hotel).
'''

def hotel_cost(nights, cost_per_night = 20):
    return cost_per_night * nights

'''
This function will take the city you are flying to as an
argument and return a cost for the flight (Hint: use if/else if
statements in the function to retrieve a price based on the chosen
city).
'''

def plane_cost(city):
    if city == "london":
        plane = 1000
    elif city == "paris":
        plane = 950
    elif city == "kyiv":
         plane =  560
    elif city == "Moscow":
        plane = 700
    else:
        plane = 500
    return plane

'''
This function will take the number of days the car will
be hired for as an argument and return the total cost of the car
rental.
'''

def car_rental(days, rent_cost = 50):
    return days * rent_cost
'''

This function will take three arguments: the number of nights a user will be staying in a hotel, the city the user will be flying to, and the number of days that the user will be hiring a car for. Using these three arguments, you can call all three of the above functions with respective arguments and finally return a
total cost for your holiday

'''

def holiday_cost(nights, city, days):
    return (hotel_cost(nights) + plane_cost(city) + car_rental(days))

#while True:


city = input("Which city are you travelling to ? ")

nights = int(input("How many nights will you be staying at the hotel? "))

days = int(input("For how many days will you be renting a car? "))

print("Your holiday Cost ")
print(" ==================")
print("You are travelling to "+ city)
print(f"Your plane cost is {plane_cost(city)}")
print(f"{nights} in hotel is{hotel_cost(nights, cost_per_night = 20)}")
print(f"{days} days renting car is {car_rental(days)}")

print(f"Holiday cost is {holiday_cost(nights, city, days)}")

