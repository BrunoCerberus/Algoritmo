"""
	Existe outro tipo de variavel de sequencia chamado Dicionario.
	Em outras linguagens tambem chamado de arrays associativos.
	Ao inves dos elementos serem associados aos indices, eles sao associados 
	a valores atribuidos pelo usuario.
	Perceba que ao expor o conteudp de um dicionario, ele exibe strings em
	aspas simples, nao ha nenhum motivo em particular nisso, e a penas o jeito
	do python.
"""
# criando, acessando e modificando dicionarios
emptyDictionary = {}
print("The value of emptyDictionary is:",emptyDictionary)

# cria e exibe dicionario com valores iniciais
grades = {"John":87, "Steve":76, "Laura":92, "Edwin": 89 }
print("All grades:",grades)

# acessando e modificando um dicionario existentem
print("Steve's current grade:", grades["Steve"])
grades["Steve"] = 90
print("Steve's new grade:",grades["Steve"])

# adicionando dados a um dicionario existente
grades["Michael"] = 93
print("Notas antes da modificacao:",grades)

# deletando dados de um dicionario
del grades["John"]
print("Dictionary grades after deletation:",grades)

print("The number of elemments in the dictionary is:",len(grades))
