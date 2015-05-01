"""
	Este exercicio importaremos uma funcao do modulo 'os.path'
	chamada 'exists', ela retorna True caso um determinado
	arquivo exista. Este programa tambem copia o conteudo
	de um arquivo para outro.
"""

from sys import argv, exit
from os.path import exists

try:
	script, from_file, to_file = argv
except ValueError:
	if len(argv) > 3:
		print("Voce excedeu o numero de argumentos!")
		print("Sem problema, tradando excecao...")
		script = argv[0]
		from_file = argv[1]
		to_file = argv[2]
	else:
		print("Ficou faltando alguns ou um parametro, repita o programa!")
		exit()

print("Copiando conteudo do arquivo",from_file,"para",to_file)

in_file = open(from_file)
# copia todo o texto de from_file para a variavel indata
indata = in_file.read()

print("O arquivo de entrada",from_file,"tem",len(indata),"bytes")

print("O arquivo de saida",to_file,"existe?:",exists(to_file))
print("Pronto, continuar pressione ENTER, sair ^C")

try:
	input("?")
# se apertar CTRL + C ele imprime uma mensagem e sai do programa
except KeyboardInterrupt:
	print("\nSaindo do programa...")
	exit()

out_file = open(to_file,'w')
out_file.write(indata)

print("Pronto, tudo certo!")
print("Conteudo de",from_file,":")
print(indata)
print()
print("Conteudo de",to_file,":")
# abrindo to_file novamente pois a outra estava a penas disponivel
# para processos de escrita, agora queremos ler
out_file.close()
out_file = open(to_file)
print(out_file.read())

# Por questoes de seguranca, devemos fechar os arquivos abertos
in_file.close()
out_file.close()
