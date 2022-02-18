print('Welcome to the tip calculator!')
bill = int(input('What was the total bill $'))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
billed = bill * (1 + tip_percent/100) /people
print("Each person should pay: $", round(billed))
