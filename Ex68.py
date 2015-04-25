"""
	Programa que faz a soma ate o oitavo termo de uma progressao geometrica
"""

from sys import exit

acumulador = 0

try:
	numero = int(input("Degite o numero= "))
	termo = int(input("Ate que termo= "))
except ValueError:
	print("Valor incorreto, reinicie o programa...")
	exit()

if numero >= 1 and termo >= 1:
	for i in range(1,termo+1):
		print(numero**i)
		acumulador += numero**i

	print("Soma ate o", termo, "termo =",acumulador)

else:
	print("Numeros negativos nao sao aceitaveis...")


