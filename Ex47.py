__author__ = 'bruno'

"""
    Programa que calcula a media por repeticao
"""

from random import randint

contador = 0
acumulador = 0

while contador < 20:
    acumulador += randint(1,100)
    contador += 1

media = acumulador / contador

print("Media =",media)