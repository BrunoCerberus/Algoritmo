__author__ = 'bruno'
"""
    Programa que retorna o nome do dia entre 0 ~ 7
"""

from sys import exit

dias_da_semana= ["segunda","terça","quarta","quinta","sexta","sabado","domingo"]

try:
    dia = int(input("Insira aqui o dia da semana(1 ~ 7): "))
except ValueError:
    print("Algo de errado aconteceu, saindo do programa...")
    exit()

if dia >=1 and dia <= 7:
    print(dias_da_semana[dia-1])
else:
    print("Dia da semana incorreto!")