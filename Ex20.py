"""
	Programa que calcula a resistencia equivalente paralela de 3 resistores
"""

R1 = float(input("Entre com o valor do primeiro resistor: "))
R2 = float(input("Entre com o valor do segundo resistor: "))
R3 = float(input("Entre com o valor do terceiro resistor: "))

Req = 1/R1 + 1/R2 + 1/R3
Req = 1 / Req

print("A resistencia equivalente paralela e",Req,"Ohms")
