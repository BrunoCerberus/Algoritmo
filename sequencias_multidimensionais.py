"""
	O programa abaixo exemplifica o uso de sequencias(listas, tuplas e dicionarios) multidimensionais.No python, e permitido um numero maior de elementos por row
"""

# listas multidimensionais
# primeira row possui os elementos "1,2,3"
# segunda row possui os elementos "4,5,6"
table1 = [[1,2,3],[4,5,6]]

# tuplas multidimensionais
# perceba que na segunda row, ha uma virgula apos o "3"
# isso e obrigatorio em tuplas para 1 elementos
# pois se nao houvesse seria meramente uma expressao
table2 = ((1,2),(3,),(4,5,6))

# iteracao for para sequencias multidimensionais
print("Values in table1 by row are:")
for row in table1:
	for item in row:
		print(item)
	print("-"*10)

print("Values in table2 by row are:")
for row in table2:
	for item in row:
		print(item)
	print("-"*10)
