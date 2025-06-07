import pygame

class Figure():

    def __init__(self, screen):
        """Initialize the figure and set its starting position."""
        self.screen = screen

        #Load the figure image and get its rect.
        self.image = pygame.image.load('megaman-sprite-8bit.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Place the figure in the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        #Store a decimal value for the figure's center.
        self.center = float(self.rect.centerx)

        #Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flags."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        """Draw the figure at its current location."""
        self.screen.blit(self.image, self.rect)