"""
	Programa que simula a serie de fibonacci com funcao recursiva
	funcoes recursivas sempre envolvem algum pensamento matematico nesse padrao n(n-1)+ n(n-2) + n(n-3) + n(n-m)
	Algo que envolva algebra ....
"""
from sys import exit

def fibonacci (n):
	
	if n < 0:
		print("Nao se pode achar um termo negativo da serie fibonacci")
		exit()

	if n == 0 or n == 1:
		return n

	else:
		return fibonacci(n-1) + fibonacci(n-2)

numero = int(input("Entre com um inteiro: "))
resultado = fibonacci(numero)
print("fibonacci(%d) = %d" % (numero,resultado))
