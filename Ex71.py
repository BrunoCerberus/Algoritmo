"""
	Programa que exibe de forma invertida um vetor de 10 elementos digitados pelo usuario
"""

# simularei a entrada de dados com a funcao randint() do modulo random
from random import randint

vetor = []

# iniciando a entrada de 10 valores
for i in range(0,11):
	vetor.append(randint(-100,100))

# expor de forma como entrou
print(vetor)

# inverter os valores
vetor.reverse()

# exibir
print(vetor)
