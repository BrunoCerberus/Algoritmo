"""
	Programa que recebe um vetor de 20 posicoes e troca os seus elementos:
	primeiro pelo ultimo, segundo pelo penultimo, terceiro pelo anti-penultimo e assim por diante
"""

from random import randint

a = []

for i in range(0,20):
	a.append(randint(0,100))

print(a)

a.reverse()

print(a)
