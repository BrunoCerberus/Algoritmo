"""
	Programa que recebe o nome e o salario de um numero indeterminado
	de funcionarios mostrando assim aqueles com o maior e o menor
	salario
"""

from sys import exit

try:
	nome = input("Insira o nome: ")
	salario = float(input("Insira o salario: "))
except ValueError:
	print("Algo de errado aconteceu, saindo do programa....")
	exit()

maior_nome = nome
menor_nome = nome
maior_salario = salario
menor_salario = salario
cond = False

if salario > 0:

	while salario != 0:
		
		cond = True
		if salario > maior_salario:
			maior_nome = nome
			maior_salario = salario
		if salario < menor_salario:
			menor_nome = nome
			menor_salario = salario
		
		try:
			nome = input("Insira o nome: ")
			salario = float(input("Insira o salario: "))
		except ValueError:
			print("Algo de errado aconteceu, repita o procedimento...")
			continue

else:
	print("Valor 0 ou negativo inserido!")

if cond == True:
	print("Maior salario....\nNome:",maior_nome,"salario:",maior_salario)
	print("Menor salario...\nNome:",menor_nome,"salario:",menor_salario)
