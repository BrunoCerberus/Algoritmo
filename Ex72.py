"""
	Programa que le um vetor de 10 elementos e transfere os elementos negativos para outro vetor
	substituindo os anteriores por 1 no primeiro vetor
"""
from random import randint
vetor1, vetor2 = [], []
# simulando entrada de dados de um vetor por um usuario
for i in range(0,11):
	vetor1.append(randint(-100,100))

# verificando os elementos negativos e fazendo a transferencia
for i in vetor1:
	if i < 0:
		vetor2 += [i] 


print (vetor1)
print (vetor2)

for i in range(len(vetor1)):
        if vetor1[i] < 0:
                vetor1[i] = 1

print (vetor1)



