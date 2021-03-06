import pygame

from ship import Ship
from alien import Alien
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

	# Define a container used to store aliens
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)

	while True:
		# For track keyboard input
		gf.check_events(ai_settings, screen, ship, bullets)

		# For redraw player's ship
		ship.update()

		# For redraw bullet from player's ship
		gf.update_bullets(bullets)

		# For redraw aliens
		gf.update_aliens(ai_settings, aliens)

		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

if __name__ == "__main__":
	run_game()
