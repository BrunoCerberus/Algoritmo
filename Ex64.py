"""
	Programa que imprime o quociente e o resto de uma divisao de dois numeros
	apenas usando as operacoes basicas de + e -
	Esse foi o mais complicado que ja fiz de logica x.x
"""

from sys import exit

quociente = 0
resto = 0
cont = 0
try:
	dividendo = int(input("Entre com o dividendo: "))
	divisor = int(input("Entre com o divisor: "))
except ValueError:
	print("Algum dado incorreto inserido, reinicie o programa...")
	exit()

while True:

	if cont == dividendo:
		break

	if cont > dividendo:
		resto = ((cont - dividendo)-divisor)* -1
		quociente-=1
		break

	cont+= divisor
	quociente+=1

print("Quociente =",quociente)
print("Resto =",resto)
