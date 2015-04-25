"""
	Algorithm that reads 3 numbers and calculate then with the follow 
	expressions.
	
	R = (A + B)**2

	S = (B + C)**2

	D = (R + S) / 2
"""

A = int(input("Type the first number: "))
B = int(input("Type the second number: "))
C = int(input("Type the third number: "))

R = (A + B)**2

S = (B + C)**2

D = (R + S) / 2


print ("The value of R is", R,"\n The value of S is", S,
	"\nThe value of D is",D)
