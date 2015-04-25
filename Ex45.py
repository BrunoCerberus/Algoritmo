__author__ = 'bruno'

"""
    Programa de calculo do imposto de renda
"""

from sys import exit

try:
    nome = input("Insira seu nome: ")
    n_de_dependentes = int(input("Insira o numero de dependentes: "))
    renda_bruta_anual = float(input("Insira sua renda bruta anual: "))
except ValueError:
    print("Algo inexperado aconteceu, saindo do programa...")
    exit()

if n_de_dependentes >= 0:
    if renda_bruta_anual >= 0:
        renda_liquida_anual = renda_bruta_anual - n_de_dependentes*600

        if renda_liquida_anual >= 0 and renda_liquida_anual < 10000:
            ir = 0
        elif renda_liquida_anual >= 10000 and renda_liquida_anual < 30000:
            ir = 0.05 * renda_liquida_anual
        elif renda_liquida_anual >= 30000 and renda_liquida_anual < 60000:
            ir = 0.1 * renda_liquida_anual
        elif renda_liquida_anual >= 60000:
            ir = 0.15 * renda_liquida_anual
    else:
        print("Valor de renda bruta anual negativo inserido, programa encerrando...")
        exit()
else:
    print("Numero de dependentes menor que 0, saindo do programa...")
    exit()


print("Sua renda bruta anual foi de",renda_bruta_anual,"R$")
print("Rua renda liquida anual e de",renda_liquida_anual,"R$")
print("Seu IR =",ir,"R$")