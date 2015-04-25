"""
	Programa que imprimi o menor de tres numero
"""

num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))
num3 = int(input("Insira o terceiro valor: "))

if num1 < num2 :
	menor = num1
else:
	menor = num2

if menor < num3 :
	pass
else:
	menor = num3

print("O menor numero digitado foi",menor)
