import pygame

class Ship:

    def __init__(self, ss_settings, screen):
        """Initialise the ship and set its starting position."""
        self.screen = screen
        self.ss_settings = ss_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('brown_ship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the side centre of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centery)

        # Movement flags
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on movement flags."""
        #Update the ship's center value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ss_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ss_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centery = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)