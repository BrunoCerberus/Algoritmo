"""
	Programa que testa media para aprovacao
"""

nome = input("Insira aqui seu nome: ")
n1 = float(input("Insira aqui  primeira nota: "))
n2 = float(input("Insira aqui a segunda nota: "))
n3 = float(input("Insira aqui a terceira nota: "))

media = (n1 + n2 + n3) / 3

print("Nome:",nome)
print("Media:",media)
if media >= 8 :
	print("Voce foi aprovado!")
else:
	print("Se fodeu otario, vai repetir mais um ano")

