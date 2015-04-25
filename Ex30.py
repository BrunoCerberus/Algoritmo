"""
	Programa que analisa o estado de um triangulo
"""

import sys

try:
	L1 = int(input("Insira o valor do primeiro lado: "))
	L2 = int(input("Insira o valor do segundo lado: "))
	L3 = int(input("Insira o valor do terceiro lado: "))

except ValueError:
	print("Valor com ponto flutuantes ou caracteres foram inseridos, fechado programa....")
	sys.exit()

# condicao de existencia de um triangulo
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2 :
	if L1==L2==L3 :
		print("O triangulo e equilatero, possui todos os lados iguais")

	elif L1==L2 or L2==L3 or L1==L3 :
		print("O triangulo e isosceles, possui pelo menos dois lados iguais")

	else:
		print("O triangulo e escaleno, possui todos os lados diferentes")

else:
	print("O triangulo nao existe com esses lados!")
