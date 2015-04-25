# Aqui mostrarei um exemplo bem simples e pratico de tratamento de excecoes

import sys
import math
try:
    number = int(input("Desejas a raiz quadrada de qual numero?: "))
except ValueError:
    print("Foi inserido um valor nao inteiro, reinicie o programa!")
    sys.exit()# uma funcao que interrompe a execucao do resto do script
try:
    result = math.sqrt(number)

except ValueError:
    print ("Atencao! Transformando entrada de numero negativo para positivo")
    number = -number
    result = math.sqrt(number)


print ("Resultado =", result)

"""
Perceba, except Exception: ira agarrar QUALQUER excecao que Python atirar, pois Exception e a classe-base da qual todas as outras excecoes sao descendentes. Se voce quiser que a mensagem 'Atencao! Nao e poss?vel calcular a raiz quadrada de um numero negativo!' seja mostrada ao usuario apenas quando for passado um valor negativo a raiz quadrada, entao teremos que especializar o nosso tratamento de excecoes, isto e, especificar qual e a excecao que queremos tratar realmente. Como vimos anteriormente, a excecao que Python atira quando ocorre uma tentativa de cilculo de raiz quadrada de um valor negativo se chama ValueError.
"""
