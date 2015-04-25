"""
	Programa que calcula o fatorial de um numero
"""

from sys import exit

try:
	numero = int(input("Insira um numero inteiro positivo: "))
except ValueError:
	print("Valores incorretos foram inseridos, saindo do programa...")
	exit()

if numero > 0:
	fatorial = 1
	for i in range(1, numero+1):
		fatorial *= i

	print("O fatorial de",numero,"=",fatorial)
else:
	print("Um numero negativo ou 0 foi inserido, tente novamente!")
