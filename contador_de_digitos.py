"""
	Programa que conta quantos digitos possui um valor
"""

num = int(input("Enter a value: "))
times = 0

while (num > 1):
	num = num / 10
	times += 1

print ("The value have",times,"digits!")
