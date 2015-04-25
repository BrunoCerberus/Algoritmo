"""
	Programa que calcula o preco de vendas
"""

import sys

try:
    nome = input("Nome do cliente: ")
    valor = 0
    cod_prod = input("Insira o codigo do produto: ")

except ValueError:
    print("Valores incorretos foram inseridos, encerrando programa...")
    sys.exit()

while cod_prod != "9999" :
    print("***Insira o valor 9999 para sair***")

    try:
        quantidade = int(input("Insira a quantidade do produto "+cod_prod+": "))
    except ValueError:
        print("Valores incorretos foram inseridos, tente novamente!")
        continue

    if cod_prod == "1001" :
        valor = valor + 5.32 * quantidade
    elif cod_prod == "1324" :
        valor = valor + 6.45 * quantidade
    elif cod_prod == "6548" :
        valor = valor + 2.37 * quantidade
    elif cod_prod == "0987" :
        valor = valor + 5.62 * quantidade
    elif cod_prod == "7623" :
        valor = valor + 6.40 * quantidade
    else:
        print("Codigo do produto inexistente")

    cod_prod = input("Insira o codigo do produto: ")

print ("Nome:",nome)
print("Total a pagar:",valor)
