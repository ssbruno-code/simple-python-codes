print("This software calculates the value of the bill for each person including the tip")


bill = float(input("What was the total bill?\n"))
tipPercentage = float(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
split = float(input("How many people to split the bill?\n"))

totalTip = (bill * tipPercentage) / 100
print(totalTip)
totalValue = (bill + totalTip) / 12
print(totalValue)






