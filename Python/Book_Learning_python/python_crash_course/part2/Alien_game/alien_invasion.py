import pygame

from ship import Ship
from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()

    ai_settings = Settings()

    # Define Window
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

if __name__ == "__main__":
    run_game()
