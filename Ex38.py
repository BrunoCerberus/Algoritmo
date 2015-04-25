"""
	Programa que imprime a quantidade de dias em um mes
	Os anos bissextos serao considerados
"""

import sys

mes_ano_bisexto = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
mes_ano_nao_bisexto = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

try:
    ano = int(input("Insira o ano: "))
    mes = int(input("Insira o mes(1 ~ 12): "))
except ValueError:
    print("O programa nao trabalha com esses valores, saindo....")
    sys.exit()

if ano % 4 == 0 and ano % 100 != 0 :
    print(ano,"e bisexto!")
    print(mes_ano_bisexto[mes],"dias")
    sys.exit()

elif ano % 400 == 0 :
    print(ano,"e bisexto!")
    print(mes_ano_bisexto[mes],"dias")
    sys.exit()
else:
    print(ano,"nao e bisexto!")
    print(mes_ano_nao_bisexto[mes],"dias")
