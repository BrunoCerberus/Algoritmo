"""
	programa que recebe dois vetores x e y e produz um vetor z para as 
	seguintes operacoes:
	a)diferenca entre os elementos de x e y
	b)soma entre os elementos de x e y
	c)produo |||||||
"""

from random import randint

x = []
y = []
z = []

for i in range(0,10):
	x.append(randint(0,100))
	y.append(randint(0,100))

print("x:",x)
print("y:",y)

for i in range(0,10):
	z += [x[i]-y[i]]

print("a) Diferenca:",z)

z = []

for i in range(0,10):
	z.append(x[i]+y[i])

print("b) Soma:",z)

z = []

for i in range(0,10):
	z += [x[i]*y[i]]

print("c) Produto:",z)
