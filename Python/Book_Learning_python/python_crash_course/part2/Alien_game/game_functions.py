import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """Response to keyboard and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            __check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            __check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # Change the color of the screen for every iteration.
    screen.fill(ai_settings.bg_color)
    
    # Draw bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the ship
    ship.blitme()

    # Draw Aliens
    aliens.draw(screen)

    # Refresh the screeen to display changes 
    pygame.display.flip()


def update_bullets(bullets):
    """Update the position of bullets and remove bullets that out of the window"""

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a group of aliens"""

    alien = Alien(ai_settings, screen) 

    number_of_aliens_x = __get_number_of_aliens_x(ai_settings, alien.rect.width)
    number_rows = __get_number_of_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_of_aliens_x):
            __create_alien(ai_settings, screen, aliens, alien_number, row_number)


def __get_number_of_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows


def __get_number_of_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_of_aliens_x = int(available_space_x / (2 * alien_width))

    return number_of_aliens_x


def __create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen) 
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def __fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


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
        __fire_bullet(ai_settings, screen, ship, bullets)
    
    # Quit the game when pressing 'q'
    elif event.key == pygame.K_q:
        sys.exit()


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
