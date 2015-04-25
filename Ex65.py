"""
	Programa que separa os pares e os impares exibe a quantidade de pares e
	impares.
"""

numero = 0
cont_par = 0
cont_impar = 0

while numero != 9999:

	print("Digite 9999 para sair!")
	try:
		numero = int(input("Entre com um numero: "))
	except ValueError:
		print("Algum dado foi inserido erroneamente, recomece...")
		continue

	if numero != 9999:
		if numero % 2 == 0 or numero == 0:
			cont_par+=1
		else:
			cont_impar+=1

print("Pares=",cont_par) 
print("Impares=",cont_impar)
