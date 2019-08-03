import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        # Set the initial position of the ship on screen.
        
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Moving Flags:
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # Redraw the ship on the screen.
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.center < self.ai_settings.screen_width:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.center > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.bottom > 0:
            self.rect.bottom -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.ai_settings.screen_height:
            self.rect.bottom += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center