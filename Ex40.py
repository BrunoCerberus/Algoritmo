__author__ = 'bruno'
"""
    Programa que le o nome e a primeira letra do estado civil de uma pessoa
    e imprime seu estado
"""

from sys import exit

try:
    nome = input("Insira seu nome: ")
    estado = input("Insira a primeira letra do seu estado civil em minusculo: ")
except ValueError:
    print("Algum dado foi inserido inorretamente, saindo...")
    exit()

if estado == "s":
    print(nome,"e solteiro")
elif estado == "c":
    print(nome,"e casado")
elif estado == "v":
    print(nome,"e viuvo")
elif estado == "d":
    print(nome,"e divorciado")
else:
    print("Estado inexistente!")