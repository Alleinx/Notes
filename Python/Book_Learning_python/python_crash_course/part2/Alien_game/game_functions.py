import sys
import pygame

from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Response to keyboard and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            __check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            __check_keyup_events(event, ship)


def __check_keydown_events(event, ai_settings, screen, ship, bullets):
    """React when user press down a key"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_UP:
        ship.moving_up = True     

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    # Shoot a bullet when user press "SPACE" key.
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def __check_keyup_events(event, ship):
    """React when user release a key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
            
    elif event.key == pygame.K_UP:
        ship.moving_up = False 
            
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings, screen, ship, bullets):
    # Change the color of the screen for every iteration.
    screen.fill(ai_settings.bg_color)
    
    # Draw bullet

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw the ship
    ship.blitme()

    # Refresh the screeen to display changes 
    pygame.display.flip()

def update_bullets(bullets):
    """Update the position of bullets and remove bullets that out of the window"""

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)