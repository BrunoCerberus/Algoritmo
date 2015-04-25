__author__ = 'bruno'
"""
    Programa para o departamento de transito
"""

from sys import exit
control = "n"
menor_de_21_anos = 0
total_de_pessoas = 0
mulheres_da_capital = 0
mot_interior_maior_de_60_anos = 0
mulher_mot_maior_que_60_anos = False

while control != "s" :
    try:
        ano = int(input("Insira o ano de nascimento: "))
        sexo = input("Insira o sexo(M ou F): ")
        procedencia = int(input("Procedencia: 0 - Capital, 1 - Interior, 2 - Outro Estado: "))
    except ValueError:
        print("Algum valor foi inserido incorretamente, saindo do programa....")
        exit()

    if sexo == "M" or sexo == "F":
        if procedencia >= 0 and procedencia <= 2:

            if 2015 - ano < 21:
                menor_de_21_anos += 1
            if sexo == "F" and procedencia == 0:
                mulheres_da_capital += 1
            if 2015 - ano > 60 and procedencia == 1:
                mot_interior_maior_de_60_anos += 1
            if sexo == "F" and 2015 - ano > 60:
                mulher_mot_maior_que_60_anos = True

            total_de_pessoas += 1
            try:
                control = input("Gostaria de sair do programa?(s/n): ")
            except ValueError:
                print("Valor inserido invalido, continuando processo!")
                control = "n"
        else:
            print("Procedencia inserida nao existe! Repita o processo")
            continue
    else:
        print("Sexo inexistente repita o processo")
        continue

print("A quantidade de pessoas registradas foi de", total_de_pessoas,"pessoas")
print("A porcentagem de motoristas menores de 21 anos e",(menor_de_21_anos*100)/total_de_pessoas,"%")
print("O numero de mulheres que sao da capital e de",mulheres_da_capital)
print("O numero de motoristas do interior do estado e que sao maiores de 60 anos e de",mot_interior_maior_de_60_anos)
print("Existe alguma mulher acima de 60 anos?:", mulher_mot_maior_que_60_anos)