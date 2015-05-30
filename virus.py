import time
import pygame
import os
"""
	Este programa é um exemplo simples de um virus que a penas
	nao fecha quando se clica no ícone de fechar janela (x).
	Ele não danifica nenhuma parte de seu sistema de nenhuma forma.
"""
pygame.init()

screen = pygame.display.set_mode((250,150))
pygame.display.set_caption('message from Admin') # da um titulo ao programa
font = pygame.font.SysFont("Lucida Console", 20)
label = font.render("U R A MORON", 1, (0,0,0))
while True: # loop
	for event in pygame.event.get():
		if event.type==pygame.QUIT: # checks if the x is clicked
			pygame.quit()#exits
			time.sleep(0.10)

			screen = pygame.display.set_mode((250,150))
			pygame.display.set_caption('message from Admin')
			#starts the program all over again

	screen.fill((255,255,255)) # bota a janela de cor branca
	screen.blit(label, (50,50)) # prints U R A MORRON message

	pygame.display.update()
