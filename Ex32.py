"""
	ALgoritmo que mostra a rela??o entre dois valores A e B
"""
import sys
try:
	A = int(input("Entre com um valor inteiro para A: "))
	B = int(input("Entre com um valor inteiro para B: "))
except ValueError:
	print("Foi inserido um valor caractere ou flutuante, programa fechando.....")
	sys.exit()

if A == B :
	print("Os valores A e B sao iguais!")
else:
	print("Os valores A e B sao diferentes!")
	
	if A > B :
		print("Sendo A maior que B!")
	else:
		print("Sendo B maior que A!")
