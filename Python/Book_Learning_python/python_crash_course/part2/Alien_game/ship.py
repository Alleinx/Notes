import pygame

class Ship():

    def __init__(self, screen):
        # Set the initial position of the ship on screen.
        
        self.screen = screen
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.__horizontal_var_offset = 5
        self.__vertial_var_offset = 5
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # Redraw the ship on the screen.
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += self.__horizontal_var_offset

        if self.moving_left:
            self.rect.centerx -= self.__horizontal_var_offset

        if self.moving_up:
            self.rect.bottom -= self.__vertial_var_offset

        if self.moving_down:
            self.rect.bottom += self.__vertial_var_offset