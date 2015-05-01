'''
Created on Apr 29, 2015

@author: bruno
'''
# este exercicio mostra o funcionamento de passagem de paramettros
# quando passamos um parametros, por exemplo, python Teste.py par1
# o primeiro parametros sempre sera o nome do arquivo e o segundo "par1"
# os parametros implicitamente sao passados para uma variavel tipo list 
# chamada 'argv' do modulo 'sys'. Para usa-las, tudo que precisamos fazer
# e usar o processo de unpacking(desempacotamento) para o mesmo numero de
# variaveis presentes na list.

# import argv do modulo sys 
from sys import argv

# declaremos as variaveis

nome, parametro1, parametro2, parametro3 = argv

# Ao executar esse script, caso vc passe um numero de parametros menor ou maior
# que o numero de variaveis, ocorrera um erro.

print("Nome do arquivo=",nome)
print("Primeiro parametro=",parametro1)
print("Segundo parametro=",parametro2)
print("Terceiro parametro=",parametro3)