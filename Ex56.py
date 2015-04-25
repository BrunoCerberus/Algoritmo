"""
	Programa que acha o valor de um termo da serie fibonacci
"""

from sys import exit

def fibonacci(x):
	if x < 0:
		print("Valor menor que 0 inserido!")

	if x == 0 or x == 1:
		return x

	if x > 1:
		return fibonacci(x-1)+fibonacci(x-2)

try:
	n = int(input("Insira o termo no qual deseja: "))
except ValueError:
	print("Algo inexperado aconteceu, saindo do programa...")
	exit()

print("O valor de fibonacci no",n,"termo =",fibonacci(n))
