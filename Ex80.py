"""
	Programa que recebe um vetor de 40 posicoes e aribui o valor 0 
	a todos elementos negativos
"""

from random import randint

vetor = []

for i in range(0,40):
	vetor.append(randint(-100,100))

print("O vetor tem %d posicoes!" % len(vetor))
print(vetor)

for i in range(len(vetor)):
	if vetor[i] < 0:
		vetor[i] = 0

print(vetor)

