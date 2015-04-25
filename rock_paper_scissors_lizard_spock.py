"""
	Um jogo que representa o jogo pedra, papel, tesoura, lagarto e spock
"""
from random import randint
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
	if name == "rock":
		return 0
	elif name == "spock":
		return 1
	elif name == "paper":
		return 2
	elif name == "lizard":
		return 3
	elif name == "scissors":
		return 4
	else:
		return 5


def number_to_name(number):
    # delete the following pass statement and fill in your code below
	if number == 0:
		return "rock"
	if number == 1:
		return "spock"
	if number == 2:
		return "paper"
	if number == 3:
		return "lizard"
	if number == 4:
		return "scissors"
	else:
		return "Nao encontrado"

    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
	print()

    # print out the message for the player's choice
	print("Voce escolheu",player_choice)
    # convert the player's choice to player_number using the function name_to_number()
	player1 = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
	computer_choice = randint(0,4)
    # convert comp_number to comp_choice using the function number_to_name()
	print("A escolha do computador foi",number_to_name(computer_choice))
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

	if player1 == 0:
		if computer_choice == 0:
			print("Empate!")
		if computer_choice == 1:
			print("Spock pulveriza a pedra, jogador perdeu!")
		if computer_choice == 2:
			print("Papel envolve pedra, jogador perdeu!")
		if computer_choice == 3:
			print("Pedra esmega lagarto, jogador venceu!")
		if computer_choice == 4:
			print("Pedra quebra tesoura, jogador venceu!")
	elif player1 == 1:
		if computer_choice == 0:
			print("Spock pulveriza a pedra, jogador venceu!")
		if computer_choice == 1:
			print("Empate!")
		if computer_choice == 2:
			print("Spock e desaprovado pelo papel, jogador perdeu!")
		if computer_choice == 3:
			print("Spock e envenenado pelo lagarto, jogador perdeu!")
		if computer_choice == 4:
			print("Spock quebra a tesoura, jogador ganhou!")
	elif player1 == 2:
		if computer_choice == 0:
			print("O papel envolve a pedra, jogador venceu!")
		if computer_choice == 1:
			print("O papel desaprova Spock, jogador venceu!")
		if computer_choice == 2:
			print("Empate!")
		if computer_choice == 3:
			print("Papel e comido pelo lagarto, jogador perdeu!")
		if computer_choice == 4:
			print("Papel e cortado pela tesoura, jogador perdeu!")
	elif player1 == 3:
		if computer_choice == 0:
			print("Lagarto e esmagado pela pedra, jogador perdeu!")
		if computer_choice == 1:
			print("Lagarto envenenou Spock, jogador venceu!")
		if computer_choice == 2:
			print("Lagarto come papel, jogador venceu!")
		if computer_choice == 3:
			print("Empate!")
		if computer_choice == 4:
			print("Lagarto e decapitado pela tesoura, jogador perdeu!")
	elif player1 == 4:
		if computer_choice == 0:
			print("Tesoura e quebrada pela pedra, jogador perdeu!")
		if computer_choice == 1:
			print("Tesoura e esmagada pelo Spock. jogador perdeu!")
		if computer_choice == 2:
			print("Tesoura corta papel, jogador venceu!")
		if computer_choice == 3:
			print("Tesoura decapita o lagarto, jogador venceu!")
		if computer_choice == 4:
			print("Empate!")
	else:
		print("Opcao escolhida pelo jogador invalida!")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



