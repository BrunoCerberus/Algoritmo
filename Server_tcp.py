import socket

host = '' #IP da maquina atual
port = 7000 #Porta que sera utilizada para conexao
recebe = "" #Variavel que recebera a mensagem
addr = (host, port) #Variavel contendo os valores de IP e porta

#Especificamos os tipos: AF_INET que declara a familia do protocolo; SOCKET_STREAM, indica que sera TCP/IP.
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Esta linha server para zerar o time wait do socket
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Define para qual IP e porta o servidor deve aguardar a conexao, que no nosso caso e qualquer IP, por isso o Host e ' '
serv_socket.bind(addr)

#Define o limite de conexoes
serv_socket.listen(10)

print "Aguardando conexao..."

#Tupla contendo dois valores, numero da conexao e endereco IP do cliente
# A linha de baixo apenas executara se o cliente estabelecer uma conexao
# com este servidor.
con, cliente = serv_socket.accept()
print "Conectado"
print "Aguardando mensagem"

#Enquanto a mensagem recebida for diferente de QSAIR o programa continuara recebendo mensagens.
while (recebe != "QSAIR"):
	recebe = con.recv(1024)#Aguarda um dado enviado pela rede de ate 1024 Bytes
	print "Mensagem recebida:",recebe,"- IP:",str(cliente[0])

serv_socket.close() #Encerra a conexao
