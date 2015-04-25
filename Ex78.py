"""
	Programa que recebe um vetor de 20 posicoes e um valor x qualquer
	O programa devera fazer uma busca de x no vetor, caso encontre, exibir
	a posicao do vetor juntamente com o valor, caso nao, mostrar uma mensa-
	gem de erro.
"""

from random import randint

vetor = []

for i in range(0,20):
	vetor.append(randint(-100,100))

print("O vetor tem",len(vetor),"elementos!")


while True:
	try:
		x = int(input("Selecione um valor inteiro: "))
	except ValueError:
		print("Valor invalido inserido, tente novamente!")
		continue

	break

if vetor.count(x): # se o valor x existir no vetor
	
	for i in range(len(vetor)):
		if vetor[i] == x:
			print("vetor[",i,"]=",vetor[i])
else:
	print("O valor",x,"nao existe no vetor")
	print(vetor)

