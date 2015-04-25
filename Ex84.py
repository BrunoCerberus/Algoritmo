"""
	Programa que recebe um vetor k de 15 elementos e cria um vetor p contendo
	todos os elementos primos do vetor k.
"""

from random import randint
k = []
p = []

for i in range(0,15):
        k.append(randint(0,100))


for i in k:
	teste = True
	if i == 2:
		p += [i]
	elif i != 1:
		if i % 2 != 0:
			for j in range(3,i):

				if i % j == 0:
					teste = False
			
			if p.count(i) == 0:
				if teste == True:
					p += [i]
			

print("k:",k)
print("Primos de k:",p)
