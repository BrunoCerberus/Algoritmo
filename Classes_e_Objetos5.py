"""
	Este exercicio mostra o funcionamento
	de um destrutor de uma classe __del__()
	em um atributo de classe, que sao variaveis
	que pertence a classe, nao apenas dedicada
	para cada objeto.
"""

class Employee:
	"""Represents an employee"""

	count = 0 # um atributo da classe
	
	# o construtor
	def __init__(self, first, last):
		"""Initializes firstName, lastName and increments count"""

		self.__firstName = first
		self.__lastName = last

		Employee.count +=1 # incrementas o atributo da classe

		print "Employee constructor for %s, %s" % (self.__lastName, self.__firstName)

	def __del__(self):
		"""Decrements count and prints message"""

		Employee.count -= 1 # decrementa o atributo da classe

		print "Employee destructor for %s, %s" % (self.__lastName, self.__firstName)

# aqui se inicia os testes da classe
# criando objetos Employee

empregado1 = Employee("Susa", "Baker")
empregado2 = Employee("Robert", "Jones")
empregado3= empregado1

print "Exibindo primeiro o numero de empregados inicializados", Employee.count

# Explicitamente deletando os objetos Employee
del empregado1
del empregado2
del empregado3

print"Numero de empregados inicializados apos a exclusao", Employee.count

"""
	Os destrutores servem para executarem certas tarefas
	quando a vida util do objeto acaba e ele e convocado
	pelo Garbage Collector. Nessa classe, pediomos para
	que o destrutor decremente em 1 cada objeto da classe
	Employee inicializado.
"""
