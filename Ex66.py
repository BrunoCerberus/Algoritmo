"""
	Programa que calcula a soma dos inteiros de 1 a 10
	O laco deve parar quando a soma assumir no minimo 11
"""

acumulador = 0
cont = 0

while acumulador <= 11:
	cont += 1
	acumulador += cont

print("valor=",acumulador)
