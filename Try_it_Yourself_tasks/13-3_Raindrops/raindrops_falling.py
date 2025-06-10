import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from raindrop import Raindrop
import game_functions as gf

def run_game():
    #Initialize pygame, settings and screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Raindrops")

    #Make a group of raindrops.
    raindrops = Group()

    #Create a shower of raindrops.
    gf.create_shower(settings, screen, raindrops)

    #Start the main loop for the game.
    while True:
        gf.check_events()
        gf.update_screen(settings, screen, raindrops)
        gf.update_raindrops(settings, raindrops)

run_game()