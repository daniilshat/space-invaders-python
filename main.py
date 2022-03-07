from tkinter import S
import pygame
from ship import Ship
import control
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("space invaders")
    bg_color = (14, 21, 37)
    ship = Ship(screen)
    bullets = Group()

    while True:
        control.events(screen, ship, bullets)
        ship.ship_position()
        control.screen_update(bg_color, screen, ship, bullets)
        control.bullets_manage(bullets)


run()