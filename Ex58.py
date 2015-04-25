"""
	Programa que calcula um fatorial
"""
from sys import exit

def fatorial(x):
	if x < 0:
		return False

	if x == 0:
		return 1
	if x == 1:
		return x

	if x > 1:
		return x * fatorial(x-1)

try:
	n = int(input("Insira um valor inteiro maior que 0: "))
except ValueError:
	print("Valor incorreto inserido, saindo....")
	exit()

print("%d! = %d" % (n, fatorial(n)))
