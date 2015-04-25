"""
	Programa que le um vetor de 12 elementos e solicita a entrada de 
	dois valores x e y por parte do usuario, ao quao ira somar
	os dois elementos do vetor das posicoes x e y
"""

from sys import exit
from random import randint

# simulando entrada de dados, pois estou com preguica kkkk
vetor = []

for i in range(0,13): # 0 ~ 12
	vetor.append(randint(0,10))

# solicitar entrada de dados

while True: # loop infinito
	
	try:
		x = int(input("Entre com um inteiro: "))
		y = int(input("Entre com outro inteiro: "))
	except ValueError:
		print("Valor n?o valido inserido, tente novamente....")
		continue

	break

print(vetor)
print("vetor[%d]= %d" % (x,vetor[x]))
print("vetor[%d]= %d" % (y,vetor[y]))
print()
print("A soma dos dois elementos e de",vetor[x]+vetor[y])
