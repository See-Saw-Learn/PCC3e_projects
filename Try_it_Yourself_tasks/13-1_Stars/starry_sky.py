import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf


def run_game():
    # Initialise pygame, settings, game and screen object.
    pygame.init()
    ss_settings = Settings()
    screen = pygame.display.set_mode(
        (ss_settings.screen_width, ss_settings.screen_height))
    pygame.display.set_caption("Starry Sky")

    # Make a group of stars.
    stars = Group()

    # Create a sky full of stars.
    gf.create_sky(ss_settings, screen, stars)

    # Start the main loop for the game.
    while True:
        gf.check_events()
        gf.update_screen(ss_settings, screen, stars)

run_game()