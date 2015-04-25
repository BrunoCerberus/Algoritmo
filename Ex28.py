"""
	Programa que calcula a conta de um hotel mais servicos
"""
import sys
try:
	dias = int(input("Ja vai embora? Que pena! Deixe-me ver quantos dias voce ficou conosco: "))
	print("Voce ficou",dias,"conosco")
except ValueError:
	print("Voce inseriu um array ou um numero float, dias nao sao floats!")
	sys.exit()

if dias > 15 :
	taxas_de_servicos = 5.50 * dias
elif dias == 15 :
	taxas_de_servicos = 6.00 * dias
elif dias < 15 and dias > 0 :
	taxas_de_servicos = 8.00 * dias
else:
	print("Valor de dias inserido incoerente, fechando programa")
	sys.exit()

valor_total = 60.00 * dias + taxas_de_servicos

print("Segue o valor a ser pago:",valor_total)

