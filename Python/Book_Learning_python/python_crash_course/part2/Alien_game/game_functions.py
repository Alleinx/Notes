import sys
import pygame

def check_events():
    """Response to keyboard and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # Change the color of the screen for every iteration.
    screen.fill(ai_settings.bg_color)
    
    # Draw the ship
    ship.blitme()

    # Refresh the screeen to display changes 
    pygame.display.flip()