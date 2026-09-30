monthly_salary = float(input("Enter your monthly salary: "))
monthly_bonus = float(input("Enter your monthly bonus: "))

total_monthly_income = monthly_salary + monthly_bonus
estimated_yearly_income = total_monthly_income * 12

print(f"Total monthly income: {total_monthly_income}")
print(f"Estimated yearly income: {estimated_yearly_income}")
