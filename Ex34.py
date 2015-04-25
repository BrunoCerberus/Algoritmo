"""
	Programa de banco que ira ceder um credito especial
	com base no saldo do ultimo ano
"""
import sys

try:
	saldo = float(input("Insira seu saldo do ultimo ano: "))
except ValueError:
	print("Foi inserido caracteres ou strings, reinicie o programa...")
	sys.exit()

if saldo >= 0 :
	if saldo >= 0 and saldo < 200 :
		percentual = 0 # 0%
	elif saldo >= 200 and saldo < 400 :
		percentual = 20
	elif saldo >= 400 and saldo < 600 :
		percentual = 30
	else:
		percentual = 40

	percentual /= 100
	credito_especial = saldo * percentual
	print("Saldo do ultimo ano:",saldo)
	print("Percentual especial e de",percentual*100,"%")
	print("Credito especial oferecido:",credito_especial)



else:
	print("Valor inserido nao e valido!!!")
