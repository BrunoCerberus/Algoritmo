__author__ = 'bruno'
"""
    Programa que imprime os numero maiores que 0 e calcula e imprime a media dos valores menores que 0
"""

from random import randint

acumulador = 0
contador = 0
contador_negativo = 0
while contador < 20:
    i = randint(-100,100)
    if i > 0:
        print (i)
    else:
        acumulador+= i
        contador_negativo -=1

    contador += 1
media = acumulador/contador_negativo
print("A media =",media)