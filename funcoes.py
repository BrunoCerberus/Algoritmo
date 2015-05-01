"""
	Este exercicio mostra operacoes com funcoes 
	mostrando que funcoes podem retornar valores.
"""

def add(a, b):
	print("Somando %d + %d" % (a, b))
	return a + b

def subtract(a, b):
	print("Subtracao %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("Multiplicando %d X %d" % (a, b))
	return a * b

def divide(a, b):
	print("Dividindo %d / %d" % (a, b))
	return a / b


print("Vamos praticar um pouco de matematica com essas funcoes!")

idade = add(20,4)
altura = subtract(80, 2)
peso = multiply(34, 2)
cachorros = divide(4, 2)

print("""
Idade: %d
Altura: %d
Peso: %d
Cachorros: %d
""" % (idade, altura, peso, cachorros))
