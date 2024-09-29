
# Program calculates employee producttivity bonus

# Initialize variables here
Bonus_1 = 50.00
Bonus_2 = 75.00
Bonus_3 = 100.00
Bonus_4 = 200.00



employeeName = input("Enter employee's name: ")
shiftString = input("Enter number of shifts: ")
transactString = input("Enter number of transactions: ")
dollarString = input("Enter transactions dollar value: ")

numShifts = float(shiftString)
numTransactions = float(transactString)
dollarValue = float(dollarString)

#write code here

ProductivityScore = (dollarValue/numTransactions)/numShifts
if ProductivityScore >= 200.00:
    bonus = Bonus_4
elif ProductivityScore >= 70 and ProductivityScore <= 199:
    bonus = Bonus_3
elif ProductivityScore >= 31 and ProductivityScore <= 69:
    bonus = Bonus_2
elif ProductivityScore <= 50:
    bonus = Bonus_1



# Output
print("Employee Name: " + employeeName)
print("Employee Bonus: $" + str(bonus))