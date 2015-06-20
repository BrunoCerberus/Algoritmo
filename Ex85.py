"""
	Faca um algoritmo (pseudocodigo) que leia um vetor (A) de 10 posicoes. Em seguida,
	compacte o vetor, retirando os valores 0(zero) e negativos, colocando apenas em um vetor
	B de 10 posicoes os valores validos de forma consecutiva, as posicoes nao utilizadas
	devem ficar ao final e com valor 0(zero).
	"""

from random import randint

A = []
B = []
x = 0
for i in range(0,10):
	A.append(randint(-100,100))

print(A)


while x < 5:
	for i in A:
		if i <= 0:
			B.append(i)
			A.remove(i)
	x+=1


print(A)
print(B)
