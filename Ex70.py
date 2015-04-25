"""
	Programa que divide sucessivamente um valor por dois ate que este
	seja menor que 1
"""

from sys import exit
contador = 0
try:
	valor = int(input("Entre com um valor: "))
except ValueError:
	print("Valor nao valido inserido, reinicie o programa")
	exit()
if valor != 0:
	while True:
		valor /= 2
		contador+=1

		if valor < 1:
			break
	print("Resultado =",valor)
	print("numero =",contador)

else:
	print("0 foi digitado, repita o programa")
	
