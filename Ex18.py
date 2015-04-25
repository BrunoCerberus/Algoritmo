"""
	Program that converts real to dolar
"""

value = float(input("Type the value that you want to convert: "))
fee = int(input("Type the fee(0% ~ 100%): "))
fee /= 100

dolar = value - value * fee

print ("Now you have",dolar,"dolars ;)")

