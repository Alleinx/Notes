import sys
import pygame

def check_events(ship):
    """Response to keyboard and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            
            elif event.key == pygame.K_UP:
                ship.moving_up = True 
            
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True

        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            
            elif event.key == pygame.K_UP:
                ship.moving_up = False 
            
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

def update_screen(ai_settings, screen, ship):
    # Change the color of the screen for every iteration.
    screen.fill(ai_settings.bg_color)
    
    # Draw the ship
    ship.blitme()

    # Refresh the screeen to display changes 
    pygame.display.flip()