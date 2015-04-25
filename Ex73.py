"""
	Programa que multiplica todos os vite elementos de um vetor
	por um valor dado pelo usuario
"""

from sys import exit
from random import randint
vetor = []

for i in range(0,21):
	vetor.append(randint(0,100))

try:
	a = int(input("Entre com um valor: "))
except ValueError:
	print("Algum valor foi inserido erroneamente, saindo...")
	exit()

for i in vetor:
	print(a,"x",i,"=",a*i)
