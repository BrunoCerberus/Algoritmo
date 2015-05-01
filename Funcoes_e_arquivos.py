"""
	Este exercicio mostra alguns exemplos simples de funcoes
	operando sobre um arquivo, mostrando duas funcoes de files
	seek(), readline() e read()
"""
from sys import argv, exit
from os.path import exists

try:
	script, input_file = argv
except ValueError:
	if len(argv) > 2:
		print("Voce excedeu a quantidade de argumentos!")
		print("Resolvendo problema...")
		script = argv[0]
		input_file = argv[1]
	else:
		print("Nome do arquivo nao inserido!")
		print("Saindo do programa...")
		exit()

if exists(input_file):

	def print_all(f):
		print(f.read())

	def rewind(f):
		f.seek(0)

	def print_a_line(line_number, f):
		print(line_number, f.readline())

	current_file = open(input_file)

	print("Primeiro irei imprimir o arquivo todo!")
	print_all(current_file)

	print("Agora vamos retroceder, como uma especie de fita!")
	rewind(current_file)

	print("Agora vamo imprimir tres linhas!")
	print_a_line(1, current_file)
	print_a_line(2, current_file)
	print_a_line(3, current_file)
else:
	print("O arquivo",input_file,"nao existe!")
	exit()
