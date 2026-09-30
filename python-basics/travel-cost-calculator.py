distance = float(input("input distance of the trip in kilometers: "))
efficiency = float(input("input fuel efficiency of the car in kilometers per liter: "))
fuel_price = float(input("input price of fuel per liter: "))

fuel_needed = distance / efficiency
total_cost = fuel_needed * fuel_price

print(f"distance: {distance} km")
print(f"fuel needed: {fuel_needed} liters")
print(f"total fuel cost: ${total_cost}")