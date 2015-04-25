"""
	Programa que recebe um vetor de 40 posicoes e conta quantos pares
	existem no vetor
"""
from random import randint

cont_par = 0
vetor = []

for i in range(0,40):
	vetor.append(randint(1,100))

print("O vetor tem",len(vetor),"posicoes!")

for i in vetor:
	if i % 2 == 0:
		cont_par +=1

print("O vetor tem",cont_par,"pares")
print(vetor)
