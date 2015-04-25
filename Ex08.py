"""
	Algorithm that calculates the final average of an student
"""

n1 = float(input("Type your first test score: "))
n2 = float(input("Type your second test score: "))
n3 = float(input("Type your last test score: "))

final_average = (n1 * 2.3 + n2 * 2.3 + n3 * 5) / (2.3 + 2.3 + 5)

print ("Your final average is",final_average)
