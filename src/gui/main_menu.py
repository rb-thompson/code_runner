import pygame
from src.gui.screen import Screen
from ..configs import *

class MainMenu(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 36)
        self.start_text = self.font.render("Press SPACE to Start", True, (255, 255, 255))
        self.quit_text = self.font.render("Press Q to Quit", True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "play"  # Signal to switch to game screen
                if event.key == pygame.K_q:
                    return False  # Signal to quit the game
        return True

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill background with black
        self.screen.blit(self.start_text, (SCREEN_WIDTH // 2 - self.start_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(self.quit_text, (SCREEN_WIDTH // 2 - self.quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))