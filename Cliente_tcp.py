import socket
ip = raw_input('Digite o ip de conexao: ') #Le do usuario o IP do servidor com que fara conexao
port = 80 #Utilizando a porta 7000
mensagem = "" #Variavel que vai ler a mensagem a ser enviada
addr = ((ip, port)) #Tupla contendo os valores do ip e porta

#Especifica a familia do protocolo e que sera TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta o IP e porta que especificamos anteriormente
client_socket.connect(addr)

#Equanto a mensagem for difirente de QSAIR ele continuara com o envio
while (mensagem != "QSAIR"):
	mensagem = raw_input("Digite uma mensagem a enviar para o servidor: ")
	client_socket.send(mensagem)
	print "Mensagem enviada"

client_socket.close() #Encerra a conexao
