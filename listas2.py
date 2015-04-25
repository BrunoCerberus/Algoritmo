"""
	Segunda parte de introducao a listas ou arrays
"""

values = [] # lista de valores

print("Entre com 10 valores:")

for i in range(10): # 0 ~ 9
	newValue = int(input("Entre com um inteiro %d: " % (i+1)))
	values += [newValue]

# criando um histograma
print("Criando um histograma dos valores:")
print("%s   %s   %s" % ("Elemento","Valor","Histograma"))

for i in range(len(values)):
	print("%d            %d        %s" % (i, values[i],"*"*values[i]))
