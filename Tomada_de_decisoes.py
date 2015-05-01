'''
Created on May 1, 2015

Este exercicio e uma simples pratica com if-else para
tomada de decisoes.

@author: bruno
'''

print("Voce entra em um quarto escuro com duas portas. Voce vai pela porta 1 ou pela 2?")
door = input("> ")

if door == "1":
    print("Ha um urso gigante aqui comendo um bolo de queijo. O que voce fara?")
    print("1. Pegar o bolo.")
    print("2. Gritar para afastar o urso.")
    
    bear = input("> ")
    
    if bear == "1":
        print("O urso arrancou sua cara. Parabens!")
    elif bear == "2":
        print("O urso arrancou suas pernas fora. Parabens!")
    else:
        print("Bem, fazendo a opcao %s provavelmente foi melhor. O urso fugiu!" % bear)
    
elif door == "2":
    print("Voce se depara diante do abismo infino da retina de Cthulhu!")
    print("1. Usar Mirtilos")
    print("2. Tampar os olhos")
    print("3. Cantar melodias")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Seu corpo sobreviveu ao ataque psiquico! Parabens")
    elif insanity == "3":
        print("A insanidade apodrece seus olhos a ponto de sair lama! Parabens")
    else:
        print("Voce se perdeu no vazio de sua mente! Parabens")
else:
    print("Voce esbarrou em alguma coisa e caiu sobre uma faca, voce esta morto. Parabens")