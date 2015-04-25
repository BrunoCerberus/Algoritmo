"""
	Programa opcoes
"""
# sys e um modulo
from sys import exit

opcao = 0
print("### Utilize 666 para sair quando a opcao for solicitada ###")
try:
    valor = float(input("Insira qualquer valor: "))
except ValueError:
    print("O programa nao aceita tais valores, saindo....")
    exit()

while opcao != 666:
    print("101 - O dobro\n102 - A metade\n103 - 10% do numero\n104 - O triplo")
    try:
        opcao = int(input("> "))
    except ValueError:
        print("Valor nao aceito pelo programa, saindo....")
        exit()
    if opcao != 666 :

        if opcao == 101:
            print("O dobro de",valor,"=",valor*2)
        elif opcao == 102:
            print("A metade de",valor,"=",valor/2)
        elif opcao == 103:
            print("10% de",valor,"=",valor*0.1)
        elif opcao == 104:
            print("O triplo de",valor,"=",valor*3)
        else:
            print("Valor Invalido, tente novamente!")
            continue

        try:
            valor = float(input("Insira qualquer valor: "))
        except ValueError:
            print("O programa nao aceita tais valores, saindo...")
            exit()

