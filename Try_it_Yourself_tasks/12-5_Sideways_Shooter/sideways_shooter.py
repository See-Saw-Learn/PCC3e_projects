import sys

import pygame
from pygame.sprite import Group

from ss_settings import Settings
from ss_ship import Ship
import ss_game_functions as sgf

def run_game():
    # Initialise game and create a screen object.
    pygame.init()
    ss_settings = Settings()

    screen = pygame.display.set_mode(
        (ss_settings.screen_width, ss_settings.screen_height))
    pygame.display.set_caption("Side Shooter")

    # Make a ship
    ship = Ship(ss_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        sgf.check_events(ss_settings, screen, ship, bullets)
        ship.update()
        sgf.update_bullets(screen, bullets)
        sgf.update_screen(ss_settings, screen, ship, bullets)

run_game()