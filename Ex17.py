"""
	Program that calculates the weight of the person
"""

weight = int(input("Type your weight here(kg): "))
weight_g = weight * 1000

print("Your have",weight_g,"g of weight")

gained = int(input("Do you gained weight(0% ~ 100%): "))

if gained == 0:
	print("Nothing to do")
else:
	gained /= 100
	new_weight = weight_g * gained + weight_g 
	print("You have now",new_weight,"g of weight")

