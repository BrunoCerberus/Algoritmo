"""
	Program that calculates a too late installment
"""

value = float(input("Type the value that you used: "))
fee = int(input("Type the fee that you accepted(0% ~ 100%): "))
time = int(input("How long are you late(days): "))

fee /= 100
installment = value + (value * (fee / 100)* time)

print ("This is the total value you will have to pay:", installment)
