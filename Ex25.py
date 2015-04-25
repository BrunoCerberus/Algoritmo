"""
	Programa que le tres valores e os ordena de forma crescente
"""

num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))
num3 = int(input("Insira o terceiro valor: "))

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

if menor != "" and medio != "" and maior != "" :
	print("Ordem crescente:",menor,">",medio,">",maior)
else:
	print("Algo de errado aconteceu")
