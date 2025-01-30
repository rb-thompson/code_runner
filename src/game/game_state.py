import pygame
import random
from .player import Player
from .background import Background
from .platform import Platform
from ..configs import *

class GameState:
    def __init__(self):
        self.current_screen = None
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(0, SCREEN_HEIGHT - PLAYER_HEIGHT - GROUND_HEIGHT, self)
        self.all_sprites.add(self.player)
        self.background = Background()
        self.player.health = 100
        self.last_platform = None

    def update(self):
        self.all_sprites.update()
        self.background.update()
        self.generate_platforms()

    def generate_platforms(self):
        if not self.platforms or self.platforms.sprites()[-1].rect.right < SCREEN_WIDTH - 600:
            x = SCREEN_WIDTH
            
            # Calculate a reasonable height range from the ground
            min_height = 200  # Minimum height from ground
            max_height = 200  # Maximum height from ground
            
            # Calculate y position relative to ground
            ground_level = SCREEN_HEIGHT - GROUND_HEIGHT
            y = ground_level - random.randint(min_height, max_height)
            
            # Use consistent platform dimensions
            width = 200  # Fixed width for all platforms
            height = 20  # Fixed height for all platforms
            
            platform = Platform(x, y, width, height)
            self.platforms.add(platform)
            self.all_sprites.add(platform)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
        return True

    def draw(self, screen):
        self.background.draw(screen)
        pygame.draw.rect(screen, GROUND_COLOR, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
        self.all_sprites.draw(screen)
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform.rect, 1)  # Green for platforms
            pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 1)  # Red for player