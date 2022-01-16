#Program to calculate the tips to be paid. Take the total billed amount,
#tips percentage and number of people to share the bill.

print("Welcome to the tip calculator.")
tot = float(input("what is the total bill? $"))
tipPercent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
finalAmount = "{:.2f}".format((tot + (tot * tipPercent/100))/people)
print(f"Each person should pay: {finalAmount}")