"""
	Programa que le um vetor de 16 posicoes e troca as posicoes dos
	8 primeiros pelos outros 8 e vice-versa
"""
from random import randint

vetor = []
vetor_auxiliar = []

for i in range(0,16): # 0 ~ 15
	vetor.append(randint(0,10))

for i in range(int((len(vetor))/2),len(vetor)):

	vetor_auxiliar.append(vetor[i])

for i in range(0,int(len(vetor)/2)):
	vetor_auxiliar.append(vetor[i])

print("Primeiro vetor=",vetor)
print("Vetor com posicoes trocadas=",vetor_auxiliar)
