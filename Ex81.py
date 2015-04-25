"""
	Programa que recebe 3 vetores de 10 posicoes cada e atribui
	todos eles a um quarto vetor de 30 posicoes de forma crescente:
	primeiro vetor, segundo vetor, terceiro vetor.
"""

from random import randint

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(0,10):
	vetor1.append(randint(0,100))
	vetor2.append(randint(0,100))
	vetor3.append(randint(0,100))

print("vetor1 =", vetor1)
print("vetor2 =", vetor2)
print("vetor3 =", vetor3)

vetor_total = []

for i in vetor1:
	vetor_total.append(i)

for i in vetor2:
	vetor_total += [i]

for i in vetor3:
	vetor_total.append(i)

print("O vetor total tem",len(vetor_total),"elementos!")
print(vetor_total)
