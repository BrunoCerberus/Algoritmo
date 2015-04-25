"""
	Programa de salarios de uma empresa, exibindo o maior e o menos salario
"""

nome_maior = ""
nome_menor = ""
maior_salario = -9999
menor_salario = 9999
salario = 1
contador = 0
acumulador = 0

while salario != 0:

	try:
		nome = input("Insira o nome: ")
		salario = float(input("Insira o salario: "))
	except ValueError:
		print("Algum valor foi inserido erroneamente, repita")
		continue

	if salario > 0:#se salario for valido
		
		acumulador+=salario
		contador+=1
		if salario > maior_salario:
			maior_salario = salario
			nome_maior = nome
		if salario < menor_salario:
			menor_salario = salario
			nome_menor = nome
	else:
		if salario < 0:
			print("Salario negativo, repita o processo")
			continue

print(nome_maior,"tem o maior salario de",maior_salario)
print(nome_menor,"tem o menor salario de",menor_salario)
print("Media dos salarios e de",acumulador/contador)
print("A empresa possui",contador,"funcionarios")
