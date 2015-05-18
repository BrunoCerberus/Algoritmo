"""
	Este programa exemplifica o funcionamento
	de sobrecarga construtores. A sobrecarga
	em python nao e a mesma que em outras linguagens.
"""

# Criando a classe box
class Box:
	
	# Primeiro construtor e unico
	# Em outas linguagens, teriamos que definir varios construtores
	# cada um com um numero de parametros diferentes
	# no caso de python, usaremos parametros pre-definidos
	# caso nenum parametro seja passado junto com a criacao do objeto
	# esse construtor utilizara os valores padrao
	def __init__(self, altura = 1, largura = 1, comprimento = 1):
		self.__altura = altura
		self.__largura = largura
		self.__comprimento = comprimento


	# Retorna o volume da caixa
	# Ao inves de usar return, poderiamos ter usado o print()
	def Volume(self):
		return self.__altura * self.__largura * self.__comprimento

	def __str__(self):
		return "Esta e uma caixa"

	"""
		AVISO: Os parametros passados deverao SEMPRE seguir
		a mesma sequencia: Altura, Largura e Comprimento, porque
		os construtores recebem a penas nessa ordem.
		Um jeito de driblar esse problema seria usar parametros key-word
		ex: objetoCaixa = Box(altura=3, largura=2, comprimento=4).
	"""

# Quando nao passado nenhum parametro
# Lembrando quando nenhum parametro e passado
# todas as dimensoes serao configuradas para 1
Caixa_1 = Box()

# 3 de largura
Caixa_2 = Box(3)

# 3 de largura e 2 de comprimento
Caixa_3 = Box(3, 2)

# 3 de largura, 2 de comprimento e 4 de altura
Caixa_4 = Box(3, 2, 4)

# Retornando o volume das quatro caixas
print("Caixa 1 =", Caixa_1.Volume())
print("Caixa 2 =", Caixa_2.Volume())
print("Caixa 3 =", Caixa_3.Volume())
print("Caixa 4 =", Caixa_4.Volume())

# Aqui claramente havera um erro, pois __altura e privado,
# nao pode ser acessado diretamente de fora da classe
# print("Acessando a altura da caixa 1 =", Caixa_1.__altura)
