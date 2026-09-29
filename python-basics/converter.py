usd = float(input("Enter the amount in USD: "))
conversion_rate = float(input("Enter the conversion rate to your local currency: "))
local_currency = usd * conversion_rate
print(f"The amount in your local currency is: {local_currency}")