import pygame
import sys

def events(ship):
    # Handling Game Events

    # close game window
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # ship move
            elif event.type == pygame.KEYDOWN:
                # movement to the right
                if event.key == pygame.K_d:
                    ship.mright = True
                # movement to the left
                elif event.key == pygame.K_a:
                    ship.mleft = True
            elif event.type == pygame.KEYUP:
                # movement to the right
                if event.key == pygame.K_d:
                    ship.mright = False
                # movement to the left
                elif event.key == pygame.K_a:
                    ship.mleft = False