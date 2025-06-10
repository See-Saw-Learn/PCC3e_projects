import sys

import pygame
from raindrop import Raindrop

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, raindrops):
    """Update images on the screen and flip to teh new screen."""
    # Redraw the screen and the raindrop during each pass through the loop.
    screen.fill(settings.bg_color)
    raindrops.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_raindrops_x(settings, raindrop_width):
    """Determine the number of raindrops that fit in a row."""
    available_space_x = settings.screen_width - 2 * raindrop_width
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x

def get_number_rows(settings, raindrop_height):
    """Determine the number of rows of raindrops that fit on the screen."""
    available_space_y = (settings.screen_height - 3 * raindrop_height)
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows

def create_raindrop(settings, screen, raindrops, raindrop_number, row_number):
    """Create a raindrop and place it in the row."""
    raindrop = Raindrop(settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = (raindrop.rect.height + 2 * raindrop.rect.height *
                       row_number)
    raindrops.add(raindrop)

def create_shower(settings, screen, raindrops):
    """Create a shower of raindrops."""
    #Create a raindrop and find the number of raindrops in a row.
    raindrop = Raindrop(settings, screen)
    number_raindrops_x = get_number_raindrops_x(settings, raindrop.rect.width)
    number_rows = get_number_rows(settings, raindrop.rect.height)

    #Create the first row of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(settings, screen, raindrops, raindrop_number,
                            row_number)

def drop_shower(settings, raindrops):
    """Drop the shower."""
    for raindrop in raindrops.sprites():
        raindrop.rect.y += settings.raindrop_speed_factor
    settings.shower_direction *= -1

def update_raindrops(settings, raindrops):
    """Update the positions of all raindrops in the shower."""
    raindrops.update()

