"""
	Este exercicio mostra o funcionamento basico
	do conceito POO(Programacao orientada a objetos)
	
"""
# Toda Classe começa com a chave class
# O uso da chave 'self' e um pouco estranha, com um pouco de pratica
# tudo fara sentido, sua definicao e um pouco complicada
# a penas imagine que a chave self e usada quando o metodo fara uso
# de algum atributo da propria classe, seria igual ao 'this' do Java.

class Carro:
	
	# aqui vem os metodos
	# resumindo, aqui ficara as operacoes as quais esse determinado
	# objeto fara. Voce pode imaginar que um objeto e um trabalhador
	# voce tem que ditar o que esse trabalhador fara.
	
	# Todo carro tem um nome, logo, faremos um metodo 
	# que atribuira um nome ao nosso carro
	def criarNome(self, nome):
		self.__nome = nome
	
	# todo carro tem um ano de fabricacao
	def criarAno(self, ano):
		self.__ano = ano
		
	# O que adianta funcoes para atribuir dados sem funcoes
	# para exibir dados?
	# Criaremos duas funcoes, uma que retorna o nome do carro
	# e a outra que retorna o ano
	def obterNome(self):
		return self.__nome
	
	def obterAno(self):
		return self.__ano
	
	# Lembrando que em python, nao e obrigatorio a declaracao da variavel
	# antes de seu uso, voce simplesmente pode cria-la durante alguma operacao
	# como nos casos de 'nome' e 'ano' .
	# Perceba tambem que, antes das variaveis da classe, existe um duplo undescore
	# isso significa que a variavel e privada e nao pode ser acessada de fora da classe
	# a penas por metodos da propria classe.
	
			
# Aqui entra os codigos para testar nossa classe
# para fazer uso da classe precisamos instanciar a classe
# ela passa a ser um objeto, tendo sua caracteristicas proprias
# criaremos 3 carros
	
carro1 = Carro()
carro2 = Carro()
carro3 = Carro()
	
# Agora acrescentaremos os dados aos 3 carros
	
carro1.criarNome("Camaro")
carro1.criarAno("2010")
	
carro2.criarNome("Gol")
carro2.criarAno("2005")
	
carro3.criarNome("Fusca")
carro3.criarAno("1991")
	
# Agora imprimiremos os dados acrescentados aos objetos
print("Carro1:")
print("Nome:", carro1.obterNome())
print("Ano:", carro1.obterAno())
	
print("-"*10)
	
print("Carro2:")
print("Nome:", carro2.obterNome())
print("Ano:", carro2.obterAno())
	
print("-"*10)
	
print("Carro3:")
print("Nome:", carro3.obterNome())
print("Ano:", carro3.obterAno())

# print(carro3.__nome) # aqui seria um erro, pois __nome e privada
