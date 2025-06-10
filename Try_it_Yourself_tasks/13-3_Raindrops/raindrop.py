import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in the sky."""

    def __init__(self, settings, screen):
        """Initialize the raindrop and set its starting position."""
        super(Raindrop, self).__init__()
        self.screen = screen
        self.settings = settings

        #Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the raindrop's exact position.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the raindrop at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the raindrops down."""
        self.y += (self.settings.raindrop_speed_factor *
                   self.settings.shower_direction)
        self.rect.y = self.y