"""
	Ha ferramentas de fatiamento de variaveis de sequencia(strings, listas e tuplas).
	Este programa mostra como funciona tais tecnicas.
"""

# criando sequencias
sliceString = "abcdefghif"
sliceTuple = (1,2,3,4,5,6,7,8,9,10)
sliceList = ["I","II","III","IV","V",
		"VI", "VII", "VIII", "IX", "X"]

# expondo as variaveis
print("sliceString =",sliceString)
print("sliceTuple =",sliceTuple)
print("sliceList =",sliceList)

# fatiando
start = int(input("Enter start: "))
end = int(input("Enter end: "))

# expondo as fatias
print("sliceString[",start,":",end,"] =",
	sliceString[start:end])

print("sliceTuple[",start,":",end,"] =",
	sliceTuple[start:end])

print("sliceList[",start,":",end,"] =",
	sliceList[start:end])
