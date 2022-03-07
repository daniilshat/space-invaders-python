from tkinter import S
import pygame
from ship import Ship
import control


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("space invaders")
    bg_color = (14, 21, 37)
    ship = Ship(screen)

    while True:
        control.events(ship)
        ship.ship_position()
        screen.fill(bg_color)
        ship.render()
        pygame.display.flip()


run()