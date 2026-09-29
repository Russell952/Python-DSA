print("Bill Calculator")
food_price = float(input("Please enter food price: "))
drink_price = float(input("Please enter drink price: "))
dessert_price = float(input("Please enter dessert price: "))
subtotal_price = food_price + drink_price + dessert_price

service_charge = subtotal_price * 0.1
total_price = subtotal_price + service_charge

print(f"Subtotal price: ${subtotal_price}")
print(f"Service charge (10%): ${service_charge}")
print(f"Total price: ${total_price}")