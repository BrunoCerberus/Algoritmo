"""
	Programa que faz uma pesquisa para uma universidade
"""
numero = 0
contador_geral = 0
contador_a = 0
contador_b = 0
contador_c = 0

while numero != 9999:
	
	try:
		numero = int(input("Quantas vezes vc foi no restaurante?: "))
	except ValueError:
		print("Valor invalido inserido, tente novamente...")
		continue


	if numero >= 0 and numero != 9999:
		contador_geral += 1

		if numero < 10:
			contador_a+=1
		elif numero >= 10 and numero <= 15:
			contador_b+=1
		else:
			contador_c+=1
		

	else:
		print("Nao existe um numero negativo de vezes, tente novamente...")
		continue

print("Quantidade de alunos =",contador_geral)
print("a)",int((contador_a*100)/contador_geral),"%")
print("b)",int((contador_b*100)/contador_geral),"%")
print("b)",int((contador_c*100)/contador_geral),"%")
