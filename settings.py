class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Intiallize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 100, 255)
        self.ship_speed = 1.5