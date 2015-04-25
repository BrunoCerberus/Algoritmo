"""
	Algorithm that converts a celsius temperature to Fahrenheit
"""

def celsius2fahrenheit(C):
	F = (9*C+160)/5
	return F

C = float(input("Enter with the celsius temperature: "))

# Note, the gloabal C is totally different to the C defined in function
F = celsius2fahrenheit(C)
print ("Celsius:", C, "\nFahrenheit:", F)

# Or

print ("Celsius:",C,"\nFahrenheit:",celsius2fahrenheit(C))

