import pygame
import sys
from bullet import Bullet

from bullet import Bullet

def events(screen, ship, bullets):
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
                # fire 
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, ship)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                # movement to the right
                if event.key == pygame.K_d:
                    ship.mright = False
                # movement to the left
                elif event.key == pygame.K_a:
                    ship.mleft = False

def screen_update(bg_color, screen, ship, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.bullet_render()
    ship.render()
    pygame.display.flip()

def bullets_manage(bullets):
    # delete old bullets and manage all bullets
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)