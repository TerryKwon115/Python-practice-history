print("Welcome to the Tip Calculator.")
bill = float(input("What was your total bill?\n$"))
tip = int(input("How much tip would you like to give? 10% / 12% / 15%\n"))
number_of_people = int(input("How many people to split the bill?\n"))

tip_percent = tip * 0.01
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / number_of_people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay : ${final_amount}")

# In short

amount_of_bill = round((bill + bill * (tip * 0.01)) / number_of_people , 2)
print(f"Each person should pay : ${amount_of_bill}")
