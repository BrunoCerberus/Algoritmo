"""
	Programa que imprime a tabuada de um determinado numero
"""

from sys import exit

try:
	numero = int(input("Insira um numero de 1 a 10: "))
except ValueError:
	print("Valor incorreto inserido, saindo....")
	exit()

if numero >= 1 and numero <= 10:
	
	for i in range(1,11): # 1 ~ 10
		print(numero,"x",i,"=",numero*i)
else:
	print("Foi inserido um numero negativo ou nulo!")
