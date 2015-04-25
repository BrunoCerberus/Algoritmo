"""
	Program that uses math, nothing more
"""

a = int(input("Type a value: "))
b = int(input("Type another value: "))

r = a ** 2 - 2 * a * b + b ** 2
s = a ** 2 + 2 * a * b + b ** 2

print ("(a - b)**2 =",r)
print ("(a + b)**2 =",s)
