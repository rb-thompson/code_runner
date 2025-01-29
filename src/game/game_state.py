import pygame
from .player import Player
from .background import Background
from ..configs import *

class GameState:
    def __init__(self):
        self.current_screen = None
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(0, SCREEN_HEIGHT - PLAYER_HEIGHT - GROUND_HEIGHT)
        self.all_sprites.add(self.player)
        self.background = Background()  # Initialize the background

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                if event.key == pygame.K_f:  # 'F' for attack, you can change this
                    self.player.attack()
        return True

    def update(self):
        self.all_sprites.update()
        self.background.update()  # Update the background

    def draw(self, screen):
        self.background.draw(screen)  # Draw background first
        pygame.draw.rect(screen, GROUND_COLOR, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
        self.all_sprites.draw(screen)