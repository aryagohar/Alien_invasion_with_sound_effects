import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 10

        # Sound settings
        self.fire_sound = pygame.mixer.Sound('sounds/fire.wav')
        self.collision_sound = pygame.mixer.Sound('sounds/collision.wav')
        self.ship_hit_sound = pygame.mixer.Sound('sounds/ship_hit.wav')
        self.level_up_sound = pygame.mixer.Sound('sounds/level_up.wav')

        # Control volume per sound (0.0 to 1.0)
        self.fire_sound.set_volume(0.1)
        self.collision_sound.set_volume(0.2)
        self.ship_hit_sound.set_volume(0.3)
        self.level_up_sound.set_volume(0.3)

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 3.5
        # Scoring settings
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)



