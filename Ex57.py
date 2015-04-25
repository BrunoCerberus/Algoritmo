"""
	Programa que solicita 10 numeros inteiros e apresenta a media
	o maior e o menor
"""

from random import randint

cont = 0
acumulador = 0
numero = randint(0,1000)
maior = numero
menor = numero
while cont < 10:
	
	acumulador += numero

	if maior < numero:
		maior = numero
	if menor > numero:
		menor = numero
	numero = randint(0,1000)
	cont += 1

media = acumulador / cont

print("O maior numero inserido =",maior)
print("O menor numero inserido =",menor)
print("A media dos valores digitados =",media)

