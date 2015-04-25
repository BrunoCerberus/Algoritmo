"""
	Este exercicio mostra alguns metodos de objetos dictionarys
	items()
	keys()
	values()
	clear()
	
"""

monthsDictionary = {1:"January", 2:"February", 3:"March",
		    4:"April", 5:"May", 6:"June", 7:"July",
		    8:"August", 9:"September", 10:"October",
		    11:"November", 12:"December"}
# items() retorna uma lista de tuplas com pares chave-valor
print("The dictionary itens are:")
print(monthsDictionary.items())

# keys() retorna a penas as chaves e nao seus valores
print("The dictionary keys are:")
print(monthsDictionary.keys())

# values() retorna os valores e nao suas chaves
print("The dictionary values are:")
print(monthsDictionary.values())

# uma iteracao simples pelas chaves de monthsDictionary
for key in monthsDictionary.keys():
	print("monthsDictionary[",key,"] =", monthsDictionary[key])

# clear() limpa todo dicionario
print("Cleaning the dictionary:")
monthsDictionary.clear()
print("monthsDictionary after clear() method is:",monthsDictionary)
