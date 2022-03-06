import pygame

class Ship():

    def __init__(self, screen):
        # gun initialization

        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def render(self):
        # gun rendering
        self.screen.blit(self.image, self.rect)