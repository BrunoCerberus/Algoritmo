"""
	Programa que define uma categoria para um atleta
"""

import sys

try:
    nome = input("Inseira seu nome: ")
    idade = int(input("Insira sua idade: "))
except ValueError:
    print("Valores invalidos foram inseridos, fechando programa...")
    sys.exit()

print("!!!As idades inseridas devem ser entre 5 ha 25 anos!!!")

if idade < 5 or idade > 25 :
    print("Valor idade invalido!")
else:
    if idade >= 5 and idade <= 10 :
        print("Categoria: Infantil")
    elif idade >= 11 and idade <= 15 :
        print("Categoria: Juvenil")
    elif idade >= 16 and idade <= 20 :
        print("Categoria: Junior")
    else:
        print("Categoria: Profissional")
