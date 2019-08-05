import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class used to define alien and its operations"""

    def __init__(self, ai_settings, screen):
        """init the alien and set their position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien's avatar
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # init aliens at top left cornor
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the position of an alien
        self.x = float(self.rect.x)

    def blitme(self):
        """draw an alien at a given position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move Alien to the left or right"""
        self.x += (self.ai_settings.alien_speed_factor * 
                        self.ai_settings.fleet_direction)

        self.rect.x = self.x

    def check_edges(self):
        """check whether a alien reaches the edge of the window"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

        return False

    