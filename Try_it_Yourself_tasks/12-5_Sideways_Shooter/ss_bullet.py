import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ss_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ss_settings.bullet_width,
            ss_settings.bullet_height)
        self.rect.midright = ship.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

        self.colour = ss_settings.bullet_colour
        self.speed_factor = ss_settings.bullet_speed_factor

    def update(self):
        """Move the bullet across the screen."""
        # Update the decimal position of the bullet.
        self.x += self.speed_factor
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)