import pygame
from .player import Player
from ..configs import *

class GameState:
    def __init__(self):
        self.current_screen = None
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(0, SCREEN_HEIGHT - PLAYER_HEIGHT - GROUND_HEIGHT)  # Position at bottom left
        self.all_sprites.add(self.player)
    
    def set_screen(self, screen):
        self.current_screen = screen

    def handle_events(self, events):
        if self.current_screen:
            result = self.current_screen.handle_events(events)
            if result == False:
                return False  # Game should quit
            elif isinstance(result, str):  # Screen switch
                return result
        return True

    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, GROUND_COLOR, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
        self.all_sprites.draw(screen)