# The tip calculator

print("Welcome to the tip calculator")
bill = float(input("What is the total amount ? $"))
tip = int(input("What percentage would you like to give? 10, 12, 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount} ")
