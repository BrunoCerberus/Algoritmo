"""
	Este exercicio implementa em um objeto um classe
	tempo, que exibe um horario em dois formatos,
	o formato militar(24h) e o formato tradicional,
	AM e PM.
"""

class Tempo:
	"""Definicao de um tipo de dado abstrato(ADT)
	   Aqui fica o comentario de documentacao para
	   a classe, que pode ser usado para explicar
	   sobre a classe. Quase todas as classes vem
	   com uma string de documentacao. Para ver uma
	   String de documentacao basta importar a classe
	   a partir de um modulo 'from nome_modulo import Tempo'
	   e usar o seguinte comando, 'Tempo.__doc__'
	"""

	# inicializar hour, minute e second
	def __init__(self):
		self.__hour = 18
		self.__minute = 0
		self.__second = 0

	# Funcao responsavel por exibir o horario no formato
	# militar.
	def printMilitar(self):
		
		print("%.2d:%.2d:%.2d" % (self.__hour, self.__minute, self.__second))

	# Funcao responsavel por exibir o horario no formato
	# tradicional
	def printTradicional(self):
		
		tempoTradicional = ""

		if self.__hour == 0 or self.__hour == 12:
			tempoTradicional += "12:"

		else:
			tempoTradicional += "%d:" % (self.__hour % 12)

		tempoTradicional += "%.2d:%.2d" % (self.__minute, self.__second)

		# verificar a partir do horario militar
		# se o valor vai ser AM ou PM
		if self.__hour < 12:
			tempoTradicional += " AM"
		else:
			tempoTradicional += " PM"

		print(tempoTradicional)

	# Essa funcao executa a mesma tarefa que o
	# metodo toString() do Java
	def __str__(self):
		return "Sou um objeto da classe Tempo"

relogio = Tempo()

# Exibir os dois horarios
relogio.printMilitar()
relogio.printTradicional()
