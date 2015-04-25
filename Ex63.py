"""
	Programa que recebe numeros indefinidamente e exibe o maior deles
"""
maior = -99999
numero = 0

while numero != 9999:
	print("Digite 9999 para sair do programa!")
	try:
		numero = int(input("Entre com um numero inteiro: "))
	except ValueError:
		print("Algum valor inexperado foi digitado, repita o processo...")
		continue

	if numero != 9999:
		if numero > maior:
			maior = numero

print("O maior numero digitado foi",maior)
