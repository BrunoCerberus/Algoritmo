"""
	Programa que exibe o conceito de um aluno com base na nota
"""

import sys

try:
	nota = int(input("Insira sua nota(0~100): "))
except ValueError:
	print("Valor inserido invalido, encerrando programa....")
	sys.exit()

if nota >=0 and nota <= 100:

	print("Nota:",nota)

	if nota >= 0 and nota <= 49:
		print("Conceito: Insuficiente")
	elif nota >= 50 and nota <= 64:
		print("Conceito: Regular")
	elif nota >= 65 and nota <= 84:
		print("Conceito: Bom")
	else:
		print("Conceito: Otimo")
else:
	print("Valor da nota fora de escala!")
