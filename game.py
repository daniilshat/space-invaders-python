from tkinter import S
import pygame
import sys
from ship import Ship

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("space invaders")
    bg_color = (14, 21, 37)
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        ship.render()
        pygame.display.flip()


run()