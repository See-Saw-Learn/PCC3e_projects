import pygame

class Figure():
    """A class to manage the figure."""

    def __init__(self, gc_game):
        """Initialize the figure and set its starting position."""
        self.screen = gc_game.screen

        #Load the figure image and get its rect.
        self.image = pygame.image.load('megaman-sprite-8bit.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = gc_game.screen.get_rect()

        #Place the figure in the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the figure at its current location."""
        self.screen.blit(self.image, self.rect)