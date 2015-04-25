"""
	Programa que realiza a multiplicacao entre 2 numeros usando o operador de soma "+"
"""

from sys import exit

try:
    n1 = int(input("Insira o primeiro numero: "))
    n2 = int(input("Insira o segundo numero: "))
except ValueError:
    print("Valores invalidos foram inseridos, impossivel fazer o tratamento, saindo do programa")
    exit()
acumulador = 0
for i in range(n1):
    acumulador += n2

print(n1,"x",n2,"=",acumulador)
