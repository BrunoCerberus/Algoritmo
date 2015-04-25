"""
	Programa que imprime todos os pares entre 85 e 907 e efetua sua soma
"""

acumulador = 0

for i in range(85,907):
	if i % 2 == 0:
		print(i)
		acumulador += i

print("Soma=",acumulador)
