__author__ = 'bruno'
"""
    Programa que enumera a quantidade de digitos de um numero
"""
from sys import exit
digitos = 0

try:
    numero = int(input("Numero inteiro positivo maior que 1: "))
except ValueError:
    print("Valor incorreto inserido, saindo do progra...")
    exit()

if numero >=1:

    while numero >= 1:

        numero /= 10
        digitos += 1

    print("Digitos =",digitos)

else:
    print("Foi inserido um numero menor que 1!")