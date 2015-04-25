__author__ = 'bruno'
"""
    Programa que soma todos os pares entre 0 < 1000
"""

acumulador = 0

for i in range(1000):
    if i % 2 == 0:
        acumulador += i
print("A soma dos pares entre 0 e 1000 e",acumulador)
