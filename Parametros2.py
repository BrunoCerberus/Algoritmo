"""
	O exercicio anterios foi a penas uma introducao.
	Este exercicio mostra alguma utilidade para os processos
	de passagem de parametro e unpacking.
"""

from sys import argv
# importar a funcao exit do modulo sys para sair do programa
from sys import exit

# um tratamento simples de excecao, funciona basicamente como um if-else
try:
	file_name, user_name = argv
# se o usuario passar um numero maior ou menor de parametros faca
except ValueError:
	print("Caso voce nao insira um nome como parametro,\n"+
		"seu nome padrao sera \"Fulano\"!")

	cond = input("Voce aceita(y/n): ")

	if cond == "n" or cond == "N":
		print("Execute o programa novamente passando seu nome como\n"+
			"parametro!")
		exit() # isso finalizara o programa
	else:
		# configura as variaveis iniciais
		user_name = "Fulano"
		file_name = argv[0]

print("Ola %s! Meu nome e %s!" % (user_name,file_name))
print("Eu gostaria de lhe fazer algumas perguntas %s" % (user_name))
gostar = input("Voce gosta de mim?\n> ")
local = input("Onde voce vive "+user_name +"\n> ")
computador = input("Que tipo de computador voce tem "+user_name+"?\n> ")

print("""
Certo, entao voce disse %s sobre gostar de mim.
Voce vive em %s. Nao tenho certeza onde fica isso.
E voce tem um computador %s. Legal
	""" % (gostar, local, computador) )
