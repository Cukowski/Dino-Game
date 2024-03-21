import random
import pygame
from pygame.locals import *
import time

pygame.init()
        
def game():
    screen = pygame.display.set_mode((750, 250))
    clock = pygame.time.Clock()

    # font

    check_point = pygame.mixer.Sound("assets/checkPoint.wav")
    death_sound = pygame.mixer.Sound("assets/die.wav")

    dino_icon = pygame.image.load("assets/dino.png")
    pygame.display.set_icon(dino_icon)

    pygame.display.set_caption("Dino Run")

    game_over = pygame.image.load("assets/game_over.png")
    replay_button = pygame.image.load("assets/replay_button.png")
    logo = pygame.image.load("assets/logo.png")

    GREY = (240, 240, 240)

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    game()