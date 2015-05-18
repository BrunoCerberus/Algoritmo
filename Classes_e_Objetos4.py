"""
	Este exercicio e o mesmo que o anterior
	a penas obedecendo as convencoes comumente
	exigidas a programacao orientada a objetos,
	como encapsulamento, restricoes a acessos
	diretos de atributos e etc...

	Agora, o unico meio de acesso aos atributos
	seria pelos metodos de acesso, a tentativa
	de acessar algum atributo diretamente de fora
	da classe seria reconhecida como violacao, resultando
	em um erro de execucao.
"""

# a class header
class Time:
	"""Class Time with accessor methods"""

	def __init__(self, hour=0, minute=0, second=0):
		"""Time constructor initializes each data member to zero"""

		self.setTime(hour, minute, second)

	def setTime(self, hour, minute, second):
		"""Set values of hour, minute and second"""
		#Metodos de acessos aos atributos
		self.setHour(hour)
		self.setMinute(minute)
		self.setSecond(second)

	def setHour(self, hour):
		"""Set hour value"""

		if 0 <= hour < 24:
			self.__hour = hour
		else:
			raise (ValueError, "Invalid hour value: %d" % hour)

	def setMinute(self, minute):
		"""Set minute value"""

		if 0 <= minute < 60:
			self.__minute = minute
		else:
			raise (ValueError, "Invalid minute value: %d" % minute)

	def setSecond(self, second):
		"""set second value"""

		if 0 <= second < 60:
			self.__second = second
		else:
			raise (ValueError, "Invalid second value: %d" % second)

	def getHour(self):
		"""Get hour value"""
		return self.__hour

	def getMinute(self):
		"""Get minute value"""
		return self.__minute

	def getSecond(self):
		"""Get second value"""
		return self.__second


	def printMilitary(self):
		"""Prints time object in military format"""

		return "%.2d:%.2d:%.2d" % (self.__hour, self.__minute, self.__second)

	def printStandard(self):
		"""Prints time object in standard format"""

		standardTime = ""

		if self.__hour == 0 or self.__hour == 12:
			standardTime += "12:"
		else:
			standardTime += "%d:" % (self.__hour % 12)

		standardTime += "%.2d:%.2d" % (self.__minute, self.__second)

		if self.__hour < 12:
			standardTime += " AM"
		else:
			standardTime += " PM"

		return standardTime
		
"""
	Isso e a penas uma classe,
	faremos os teste da classe
	em outro arquivo python
	chamado 'Teste_Classes_e_Objetos4.py'
	mas por via das duvidas, execute o comando
	python nesta classe para averiguar erros.
"""
		
