import pygame

from ship import Ship
from settings import Settings
from pygame.sprite import Group

import game_functions as gf

def run_game():
	pygame.init()

	ai_settings = Settings()

	# Define Window
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Init Ship
	ship = Ship(ai_settings, screen)

	# Define a container used to store bullets
	bullets = Group()

	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()

		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		gf.update_screen(ai_settings, screen, ship, bullets)

if __name__ == "__main__":
	run_game()
