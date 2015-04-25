"""
	Programa que processa tres notas e exibe a situacao do aluno
"""

nome = input("Insira seu nome: ")
nota1 = float(input("Insira A1: "))
nota2 = float(input("Insira A2: "))
nota3 = float(input("Insira A3: "))

media = (nota1 + nota2 + nota3)/3

print("Nome:",nome)
print("Media:",media)
print("Situacao....",)

if media >= 7 :
	print("Aprovado")
elif media >= 5 and media < 7 :
	print("Recuperacao")
else:
	print("Reprovado")
