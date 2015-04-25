"""
	Este programa mostra as operacoes basicas sobre listas ou arrays
	Listas so podem ter valores homogeneos, de mesmo tipo para todos
	os elementos.
"""

aList = [] # criando uma lista, sem tipo ainda
bList = [] # criando outra lista, tambem sem um tipo

# adicionando valores a lista aList
for i in range(1,11):
	aList += [i]

# adicionando valores a lista bList
for i in range(1,11):
	bList.append(i)

# lembrando que, nao ha esta maneira de inserir valores em uma lista
# usado de forma generica em pseudocodigo e em outras linguagens.

# for i in range(1,11):
#	cList[i] = i+2 # esse meio de atribuicao generico nao existe em python


# a tres formas de imprimir uma lista

print("Primeira lista",aList)

# outra forma

for i in bList:
	print(i)

# forma mais generica, usada em outras linguagens de programacao
# acesso direto pelos indeces
for i in range(len(aList)):
	print(aList[i])

# exibindo os indices em conjunto com seus valores
for i in range(len(bList)):
	print("%d  %d" % (i, bList[i]))

# modificando listas
print("Modificando um valor de uma lista....")
print("Valores da lista antes da modificacao",aList)
aList[0] = -100
aList[-3] = 19 # o anti-penultimo termo da lista
print("Valores da lista apos a modeificacao:",aList)
