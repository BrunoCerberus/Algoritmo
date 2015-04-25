"""
	Este programa mostra o funcionamento de passagem 
	de uma lista para uma funcao
"""

def modifyList(aList):
	for i in range(len(aList)):
		aList[i] *= 2 # multiplicar cada elemento da lista por 2

def modifyElement(element):
	element *= 2

aList = [1,2,3,4,5]

print("Effects of passing a entire list:")
print("The values of the original list are:")

for item in aList:
	print (item)

modifyList(aList)

print("The values of the modified list are:")

for i in range(len(aList)):
	print(aList[i])

print("Effects of passing list element:")
print("aList[3] before modifyElement:", aList[3])
modifyElement(aList[3])
print("aList[3] after modifyElement:",aList[3])

print("Effects of passing slices of list:")
print("aList[2:4] before modifyList:", aList[2:4])
modifyList(aList[2:4])
print("aList[2:4] after modifyList:",aList[2:4])
