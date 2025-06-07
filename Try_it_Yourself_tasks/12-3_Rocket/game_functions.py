import sys

import pygame

def check_events(rocket_sprite):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket_sprite.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket_sprite.moving_left = True
            elif event.key == pygame.K_UP:
                rocket_sprite.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket_sprite.moving_down = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket_sprite.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket_sprite.moving_left = False
            elif event.key == pygame.K_UP:
                rocket_sprite.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket_sprite.moving_down = False