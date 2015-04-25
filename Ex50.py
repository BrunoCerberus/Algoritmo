__author__ = 'bruno'
"""
    Programa em que calcula a quantidade de alunos acima de 30 anos
"""

from random import randint

contador = 0
acumulador = 0

while contador < 50:
    idade = randint(10,70)
    if idade > 30:
        acumulador += 1

    contador += 1

print("A quantidade de alunos maior que 30 anos e de",acumulador)