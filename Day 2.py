print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip = float("1." + input("What percentage tip would you like to give? 10, 12, or 15? "))
num_ppl = int(input("How many people will be splitting the bill? "))

total_payment = round(total_bill * tip / num_ppl, 2)
print(f"Each person should pay: ${total_payment}")
