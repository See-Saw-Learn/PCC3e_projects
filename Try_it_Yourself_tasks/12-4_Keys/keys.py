import sys

import pygame

def run_game():
    # Initialise game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Keys")

    # Start the main loop for the game.
    while True:

        # Watch for keyboard events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()