"""
	Este programa nao e um executavel.
	Ele consiste de funcoes nas quais importaremos
	a partir do interpretador interativo do python.
	
"""

# Esta funcao ela quebra uma frase ou sequencia em palavras
# para isso, usamos o metodo de strings chamado split()
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

# Esta funcao elea organiza as palavras de forma alfabetica
# usamos uma funcao global chamada sorted()
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

# Esta funcao imprime a primeira palavra de uma sequencia
# usamos uma funcao de string chamada pop()
# no qual remove alguma coisa de uma sequencia
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print(word)

# Esta funcao faz ao contrario da anterior
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word =  words.pop(-1)
	print(word)

# Agora comecaremos a aplicar funcoes dentro de outras funcoes
# Esta funcao recebe um frase inteira e quebra em palavras
# e logo em seguida as organiza de forma alfabetica
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)


# Esta funcao imprime a primeira e a ultima palavra
def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

# Esta funcao organiza as palavras de uma frase
# antes de imprimir a primeira e a ultima palavra
def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


# Pronto, agora para utilizar esse excercicio vc tera que fazer o seguinte
# no interpretador python modo interativo
"""
from Import_funcoes import *
sentence = "All good things come to those who wait."
words = break_words(sentence)
words
sorted_words = sort_words(words)
sorted_words
print_first_word(words)
print_last_word(words)
words
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words
sorted_words = sort_sentence(sentence)
sorted_words
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)

"""
