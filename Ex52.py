"""
	Programa que soma todos 50 numeros some todos que sao positivos e expoe a quantidade daqueles que sao negativos
"""

from random import randint
contador = 0
acumulador_positivo = 0
quantidade_de_numeros_negativos = 0

while contador < 50:
	y = randint(-100,100)
	if y > 0:
		acumulador_positivo += y
	else:
		quantidade_de_numeros_negativos += 1
	contador += 1
print("A soma de todos positivos =",acumulador_positivo)
print("Quantidade de numeros negativos =",quantidade_de_numeros_negativos)
