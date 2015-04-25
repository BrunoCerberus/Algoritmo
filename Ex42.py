__author__ = 'bruno'
"""
    Programa estacoes
"""

from sys import exit

try:
    mes = int(input("Entre com o mes(1~12): "))
except ValueError:
    print("Valor inserido incorreto, saindo...")
    exit()

if mes >= 1 and mes <= 12:
    if mes >=1 and mes <=3:
        print("Verao")
    elif mes >=4 and mes <= 6:
        print("Outono")
    elif mes >= 7 and mes <= 9:
        print("Inverno")
    else:
        print("Primavera")
else:
    print("Mes",mes,"nao existe!")