"""
	Programa que calcula o total de elementos separadamente
	por linha, e os exibe.
"""

a = [[1,2],[3,4,5],[6,7]]

total1, total2, total3 = 0,0,0

# percorre os elementos da primeira liha
for column in range(len(a[0])):
	total1 += a[0][column]
# percorre os elementos da segunda linha
for column in range(len(a[1])):
	total2 += a[1][column]
# percorre os elementos da terceira linha
for column in range(len(a[2])):
	total3 += a[2][column]

print("Total da primeira linha e",total1)
print("Total da segunda linha e",total2)
print("Total da terceira linha e",total3)
