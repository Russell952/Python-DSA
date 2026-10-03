print("Grade checker")

score = float(input("Enter your score: "))

if score >= 90:
    print("you got an A")

elif score >= 70:
    print("your grade is B")

elif score >= 50:
    print("your grade is C")

elif score >= 30:
    print("your grade is D")

elif score >= 10:
    print("your grade is E")

else:
    print("you failed")