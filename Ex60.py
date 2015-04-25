"""
	Programa que calcula dados de uma turma de 45 alunos
"""

from random import randint
from sys import exit

alunos_menores_170 = 0
cont_alunos_menos_170 = 0
cont_alunos_maior_20_anos = 0
alunos_maiores_20_anos = 0
for i in range(45):

    try:
        idade = int(input("Insira a idade: "))
        altura = float(input("Insira a altura: "))
    except ValueError:
        print("Valor inserido invalido, tente novamente!")
        continue

    if altura < 0.5:
        print("HAhahaha nao existe ninguem desse tamanho, repita!")
        continue
    if idade <= 0:
        print("Valor de idade negativo ou 0, tente novamente!")
        continue

    if idade > 20:
        cont_alunos_maior_20_anos += altura
        alunos_maiores_20_anos += 1
    else:
        if altura < 1.70:
            cont_alunos_menos_170 += idade
            alunos_menores_170 += 1

if alunos_menores_170 == 0:
    alunos_menores_170 = 1
if alunos_maiores_20_anos == 0:
    alunos_maiores_20_anos = 1

media_menor = cont_alunos_menos_170 / alunos_menores_170
media_maior = cont_alunos_maior_20_anos / alunos_maiores_20_anos
print("Idade media dos alunos com menos de 1,70m =",media_menor)
print("Altura media dos alunos com mais de 20 anos =",media_maior)
