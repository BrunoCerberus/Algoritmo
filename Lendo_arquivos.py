"""
	Este programa mostra como funciona a leitura de arquivos
	usando a funcao global de Python chamada open()
"""

from sys import argv, exit

try:
	name, file_name = argv
except ValueError:
	if len(argv) > 2:
		print("Voce colocou parametros de mais, reexecute o programa!")
		exit()
	else:
		print("Voce esqueceu de botar o nome do arquivo!")
		exit()

# passando o conteudo do arquivo para um variavel
txt = open(file_name)

print("Aqui esta o seu arquivo:",file_name)
# le o arquivo
print(txt.read())

# ao inves de passar o nome do arquivo para a execucao do programa
# voce tambem pode passar durante a execucao

print("Digite o nome do arquivo...")
file_name = input("> ")

txt = open(file_name)

print(txt.read())
