# Desempacotamento

# Criando uma lista, tupla e uma string

aString = "abc"
aList = [1,2,3]
aTuple = "a", "A", 1

# tanto a lista e a tupla possuem exatamente as mesmas operacoes
# sendo a unica diferenca as tuplas serem umitaveis
# por convensao, a listas sao usadas para dados homogeneos
# e a tuplas sao usadas para dados heterogemeos, ou seja, dados de tipos
# diferentes misturados.

# Operacao de desempacotamento, a quantidade de variaveis a esquerda
# tem de ser o mesmo numero da quantidade de elementos das sequencias.

print("Unpacking string...")
first, second, third = aString
print("String values:",first,second,third)

print("Unpacking list...")
first, second, third = aList
print("List values:",first,second,third)

print("Unpacking tuple...")
first, second, third = aTuple
print("Tuple values:",first,second,third)

# trocando dois valores de duas variaveis sem a nacessidade de uma auxiliar
x = 3
y = 4

print("Before swapping: x = %d, y = %d" % (x,y))
x, y = y, x # trocar as variaveis
print("After swapping: x = %d, y = %d" % (x,y))

# Claramente a execucao do script abaixo e um erro
#first, second, third, forth = aList
# pois aList so possui 3 elementos, e nao quatro.
