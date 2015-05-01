"""
	Um programa que possui um array multidimensional que some os elementos
	de cada row e mostre o total da soma de todos elementos
"""

# array multidimensional
a = [[1,2],[3,4,5],[7,8]]
total = 0
for row in a:
	# row passa a assumir cada list da lista multidimensional
	for item in row:
		total += item

print("The total is %d" % total)
