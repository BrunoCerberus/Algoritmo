"""
	Este programa mostra como e feita a operacao de escrita
	de um arquivo usando open() e alguns metodos como truncate()
	write() e close().
	Lembrando que, caso voce passe algum arquivo inexistente
	ele criara um nome arquivo com o nome do parametro que voce passou.
"""

from sys import argv, exit
try:
	script, filename = argv
except ValueError:
	if len(argv) > 1:
		print("Voce inseriu, argumentos de mais!")
		print("Mas tudo bem, o tratamento de excecoes esta aqui para isso!")
		script = argv[0]
		filename = argv[1]
	else:
		print("Voce esqueceu de fornecer o nome de um arquivo, volte e tente novamente!")
		exit()


print("Vou apagar o arquivo %s" % filename)
print("Se voce nao quer isso, pressione CTRL + C(^C)")
print("Se voce quer isso a penas pressione ENTER!")
try:
	input("?")
except KeyboardInterrupt:
	print("Saindo do programa...")
	exit()

print("Abrindo o arquivo....")

# Aqui estamos abrindo o arquivo para executar processos de escrita
# e nao de leitura ou execucao
# por padrao, quando nao e passado nenhum parametro desses, 'r' e
# incluido implicitamente para leitura
target = open(filename,'w')

print("Apagando o arquivo...adeus o/")
target.truncate()

print("Agora lhe pedirei que digite tres linhas.")
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("Agora eu irei escrever essas linhas no arquivo!")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("E isso que reside dentro do arquivo %s" % filename)
target = open(filename)
print(target.read())

print("Agora finalmente fecharei o arquivo!")
target.close()
