import sys

import pygame

def check_events(figure):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                figure.moving_right = True
            elif event.key == pygame.K_LEFT:
                figure.moving_left = True
            elif event.key == pygame.K_UP:
                figure.moving_up = True
            elif event.key == pygame.K_DOWN:
                figure.moving_down = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                figure.moving_right = False
            elif event.key == pygame.K_LEFT:
                figure.moving_left = False
            elif event.key == pygame.K_UP:
                figure.moving_up = False
            elif event.key == pygame.K_DOWN:
                figure.moving_down = False