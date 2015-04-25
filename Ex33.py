"""
	Programa que le dois valores e os compara para saber se sao multiplos entre si
"""

import sys

try:
	A = int(input("Insira um valor inteiro a A: "))
	B = int(input("Insira um valor inteiro a B: "))
except ValueError:
	print("Valores nao validos inseridos, fechado programa...")
	sys.exit()

if A > B :
	menor = B
	maior = A
else:
	menor = A
	maior = B

if maior % menor == 0:
	print(maior,"e multiplo de",menor)
else:
	print(maior,"nao e multiplo de",menor)
