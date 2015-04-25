"""
	Programa que le 3 numeros e imprime o maior deles
"""
import sys
try:
	num1 = int(input("Insira o primeiro valor: "))
	num2 = int(input("Insira o segundo valor: "))
	num3 = int(input("Insira o terceiro valor: "))

except ValueError:
	print("Valor inserido invalido, fechando programa....")
	sys.exit()

if num1 > num2 :
	maior = num1
	if num1 > num3 :
		pass
	else:
		maior = num3
else:
	maior = num2
	if num2 > num3 :
		pass
	else:
		maior = num3

print ("O maior valor digitado foi",maior)
