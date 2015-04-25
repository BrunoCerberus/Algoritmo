"""
	Programa que calcula o fatorial de um numero usando funcao recursiva
"""
# Uma funcao recursiva e uma funcao que invoca ela mesma, afim de "afundar" nos valores
# de retorno ate que esses valores comecem a retornar um por um de cima para baixo.
from random import randint

def factorial(number):
	if number <= 1:
		return 1
	else:
		return number * factorial(number - 1)

for i in range(13): # 0 ~ 12
	print (i,"! =",factorial(i))
