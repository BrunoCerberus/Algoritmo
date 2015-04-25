"""
	Programa que imprimi coisas conforme o valor de entrada
"""
import sys

try:
	N = int(input("Digite um valor inteiro: "))
except ValueError:
	print("Provavelmente vc inseriu algum caractere que nao e um numero ou",
		"com ponto flutuante!")
	sys.exit()

if N <= 10 :
	print("F1")
elif N > 10 and N <= 100 :
	print("F2")
else:
	print("F3")
