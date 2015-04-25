"""
	Programa que trabalhar com uma funcao com argumentos padrao
"""

def volume_caixa(l = 1, c = 1, a = 1):
	return l * c * a

print("O volume padrao da caixa e",volume_caixa())
print("O volume da caixa com largura 10 e",volume_caixa(10))
print("O volume da caixa com largura 10 e comprimento 5 e",volume_caixa(10,5))
print("O volume da caixa com largura 10, comprimento 5 e altura 2 e",volume_caixa(10,5,2))

# tambem posso inserir o comprimento ou a altura antes que a largura, porem terei de informar explicitamente isso ao interpretador
print("O volume da caixa apenas com a altura 5 e",volume_caixa(a=5))

