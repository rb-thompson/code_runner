# src/gui/pause_menu.py
import pygame
import math
from ..configs import *

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.pulse_time = 0
        
        # Pre-render two sizes of text for a simple pulse effect
        self.small_title = pygame.font.Font(None, 50).render("Game Paused", True, (105, 252, 83))
        self.large_title = pygame.font.Font(None, 52).render("Game Paused", True, (105, 252, 83))
        self.pulsing_title = self.small_title

        self.resume_text = self.font.render("Press ESC to Resume", True, (255, 255, 255))
        self.quit_text = self.font.render("Press Q to Quit", True, (255, 255, 255))

    def draw(self):
        # Darken the screen for a pause effect
        darken_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        darken_surface.fill((0, 0, 0, 64))  # Semi-transparent black overlay
        self.screen.blit(darken_surface, (0, 0))

        # Simple pulse effect for the title text
        self.pulse_time += 1
        if self.pulse_time % 60 < 30:  # Every 30 frames out of 60, switch size
            self.pulsing_title = self.large_title
        else:
            self.pulsing_title = self.small_title

        # Draw pause menu text
        self.screen.blit(self.pulsing_title, (SCREEN_WIDTH // 2 - self.pulsing_title.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(self.resume_text, (SCREEN_WIDTH // 2 - self.resume_text.get_width() // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(self.quit_text, (SCREEN_WIDTH // 2 - self.quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))