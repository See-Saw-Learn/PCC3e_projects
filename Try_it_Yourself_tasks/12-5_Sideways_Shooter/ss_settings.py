class Settings():
    """A class to store all settings for Side Shooter."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (49, 21, 79)
        self.bullets_allowed = 3

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = 41, 247, 17
