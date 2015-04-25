"""
	Programa que recebe numeros ate que o valor sentinela seja ativado
	Imprime sua soma e sua media.
"""

cont = 0
numero = 0
acumulador = 0

while numero != 9999:
	print("Digite 9999 para sair!")
	try:
		numero = int(input("Insira um numero inteiro: "))
	except ValueError:
		print("Algum valor nao esperado foi inserido, tente novamente.")
		continue
	
	if numero != 9999:

		cont += 1
		acumulador += numero

if cont != 0:

	print("A quantidade de numeros digitados foi",cont)
	print("A soma de todos eles e de",acumulador)
	print("A media e de",(acumulador/cont))		
