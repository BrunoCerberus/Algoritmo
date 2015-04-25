"""
	A banking program
"""

deposit = float(input("Type the value that you want to deposit: "))
fee = float(input("Type the value of the fee (0% ~ 100%): "))
fee /= 100

yield_deposit = deposit - deposit * fee

print("The yield value is", yield_deposit)
