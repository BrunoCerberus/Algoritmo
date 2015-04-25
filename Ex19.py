"""
	Programa que calcula o salario de um vendedo com base em suas vendas e percentuais
"""

valor_de_venda = float(input("Insira aqui o valor vendido ate agora: "))
percentual = int(input("Insira aqui seu percentual de venda(0% ~ 100%): "))
cod = input("Insira seu codigo de vendedo: ")
nome = input("Insira seu nome: ")
salario_fixo = float(input("Insira o seu salario fixo: "))
percentual /= 100

salario_final = salario_fixo + valor_de_venda * percentual

print("Vendedor:",cod,"----- Salario:",salario_final)
