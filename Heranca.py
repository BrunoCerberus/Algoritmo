'''
    Este exercicio mostra o funcionamento basico
    de heranca, em que uma classe filha herda um atributo
    da classe pai.
'''

# classe pai
class ClassePai:
    var1 = "Atributo da classe pai"

# Para a haver heranca, preciso especificar o nome
# da classe pai como parametro dentro da definicao
# da classe filha.
class ClasseFilha(ClassePai):
    var2 = "Atributo da classe filha"

# Conceito de heranca simples, a filha herda os atributos 
# do pai, e o pai nao consegue acessar os atributos da filha.

pai = ClassePai()
filha = ClasseFilha()

# Teste
print("Dentro de pai")
print(pai.var1)

print("-"*10)

print("Dentro de filha")
print(filha.var2)
print(filha.var1)

# print(pai.var2) # isso e um erro

