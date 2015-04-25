__author__ = 'bruno'
"""
    Programa que exibe o numero por extenso
"""

from sys import exit

numero_extenso = ["um","dois","tres","quatro","cinco","seis",
                    "sete","oito","nove","dez"]

try:
    numero = int(input("Insira um numero de 1 a 10: "))
except ValueError:
    print("Valor invalido foi inserido, saindo...")
    exit()

if numero >= 1 and numero <= 10 :
    print(numero_extenso[numero-1])
else:
    print("Numero digitado nao aceito!")
