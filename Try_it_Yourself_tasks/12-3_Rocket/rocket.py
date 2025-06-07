import sys

import pygame

from settings import Settings
from rocket_sprite import Rocket
import game_functions as gf

def run_game():
    #Initialize pygame, settings, and screen object.
    pygame.init()
    gc_settings = Settings()
    screen = pygame.display.set_mode((gc_settings.screen_width,
                                      gc_settings.screen_height))
    pygame.display.set_caption("Rocket")

    #Make a rocket.
    rocket = Rocket(screen)

    #Start the main loop for the game.
    while True:
        gf.check_events(rocket)
        rocket.update()

        #Redraw the screen during each pass through the loop.
        screen.fill(gc_settings.bg_color)
        rocket.blitme()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()