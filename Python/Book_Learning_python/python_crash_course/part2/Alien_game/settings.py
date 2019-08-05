# Store settings
class Settings():
    """Store all the config for our little game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) #Gray

        # Each time, the ship will move by 2 pixels.
        self.ship_speed_factor = 3.5

        # Config for bullet
        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
