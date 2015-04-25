"""
	Programa em que o usuario seleciona a ordem de seguencia de
	3 numero ao bel prazer.
"""

import sys

try:
	num1 = int(input("Insira o primeiro valor inteiro: "))
	num2 = int(input("Insira o segundo valor inteiro: "))
	num3 = int(input("Insira o terceiro valor inteiro: "))
except ValueError:
	print("Valor nao aceito inserido, finalizando programa....")
	sys.exit()

if num1 > num2 :
        maior = num1
        if num2 > num3 :
                medio = num2
                menor = num3
        else:
                medio = num3
                menor = num2

                if num1 > num3 :
                        medio = num3
                        menor = num2
                else:
                        maior = num3
                        medio = num1
else:
        maior = num2
        if num2 > num3 :
                if num1 > num3 :
                        medio = num1
                        menor = num3
                else:
                        medio = num3
                        menor = num1
        else:
                maior = num3
                medio = num2
                menor = num1

print("Em qual ordem voce deseja expor os dados?")
print("Ordem crescente - 1\nOrdem decrescente - 2\nMaior valor entre dois - 3")
try:
	opcao = int(input("> "))
except ValueError:
	print("Valor inserido invalido, finalizando programa....")
	sys.exit()

if opcao >=1 and opcao <=3:
	if opcao == 1:
		print(menor,"-",medio,"-",maior)
	elif opcao == 2:
		print(maior,"-",medio,"-",menor)
	else:
		print(menor,"-",maior,"-",medio)
else:
	print("Opcao invalida")
