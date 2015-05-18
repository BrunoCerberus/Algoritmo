'''
    Este exercicio utiliza a funcao de inicializacao de um objeto
    tambem chamada de construtor, a __init__().
    Ela server para inicializar os atributos ou variaveis de um
    determinado objeto, evitando assim o uso dos metodos de
    inicializacao.
'''

class Carro2:
    
    # Aqui sera a funcao __init__() na qual inicializara os atributos
    # ela tambem usa a chave self, pois usara de algum forma as variaveis
    # da propria classe
    # Como no exercicio anterior, cara carro tem um nome e o ano
    # usaremos o __init__() para nos poupar linhas de codigo desnecessarias.
    def __init__(self, nome, ano):
        self.__nome = nome
        self.__ano = ano

    # aqui virao os metodos para retornar os valores contidos na variaveis
    # essa tecnica de privatizar nomes se chama encapsulamento
    # e existem varias formas de encapsulamento
    def obterNome(self):
        return self.__nome
    
    def obterAno(self):
        return self.__ano
    
# A unica coisa diferente que acontecera aqui e que
# Na hora de inicializar o objeto, voce deve passar
# os dois valores como parametro dentro dos parenteses
# se nao havera um erro

carro1 = Carro2("Camaro","2010")
carro2 = Carro2("Gol","2005")
carro3 = Carro2("Fusca","1991")

# Vamos verificar a saida dos dados
print("Carro1:")
print("Nome:", carro1.obterNome())
print("Ano:", carro1.obterAno())

print("-"*10)

print("Carro2:")
print("Nome:", carro2.obterNome())
print("Ano:", carro2.obterAno())

print("-"*10)

print("Carro3:")
print("Nome:", carro3.obterNome())
print("Ano:", carro3.obterAno())

# carro4 = carro2() # isso claramente e um erro, pois faltam os argumentos
