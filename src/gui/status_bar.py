# src/gui/status_bar.py
import pygame
from ..configs import *

class StatusBar:
    def __init__(self, player):
        self.player = player
        self.font = self.font = pygame.font.Font(None, 28)

        # Load icons (replace paths with actual paths to your image files)
        self.health_icon = pygame.image.load('assets/icons/health_icon.png').convert_alpha()
        self.health_icon = pygame.transform.scale(self.health_icon, (STATUS_BAR_ICON_SIZE, STATUS_BAR_ICON_SIZE))
        self.coin_icon = pygame.image.load('assets/icons/coin_icon.png').convert_alpha()
        self.coin_icon = pygame.transform.scale(self.coin_icon, (STATUS_BAR_ICON_SIZE, STATUS_BAR_ICON_SIZE))
        self.level_icon = pygame.image.load('assets/icons/level_icon.png').convert_alpha()
        self.level_icon = pygame.transform.scale(self.level_icon, (STATUS_BAR_ICON_SIZE, STATUS_BAR_ICON_SIZE))

    def draw(self, screen):
        # Health Bar
        pygame.draw.rect(screen, STATUS_BAR_COLOR, (10, 10, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        current_health_width = (self.player.health / 100) * HEALTH_BAR_WIDTH
        pygame.draw.rect(screen, HEALTH_COLOR, (10, 10, current_health_width, HEALTH_BAR_HEIGHT))

        # Text for health, coins, and experience with icons
        health_text = self.font.render(f" {self.player.health}", True, TEXT_COLOR)
        coins_text = self.font.render(f" {self.player.coins}", True, TEXT_COLOR)
        level_text = self.font.render(f" Level {self.player.level}", True, TEXT_COLOR)

        screen.blit(self.health_icon, (10, 35))
        screen.blit(health_text, (10 + STATUS_BAR_ICON_SIZE + 5, 35))  # +5 for some space between icon and text
        screen.blit(self.coin_icon, (10, 65))
        screen.blit(coins_text, (10 + STATUS_BAR_ICON_SIZE + 5, 65))
        screen.blit(self.level_icon, (10, 95))
        screen.blit(level_text, (10 + STATUS_BAR_ICON_SIZE + 5, 95))

        # Draw border around health bar
        pygame.draw.rect(screen, (31, 33, 32), (10, 10, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT), 2)

    def _get_gradient_color(self, health_percentage):
        # Simple gradient from green to red
        if health_percentage > 0.5:
            # Green to Yellow
            r = int(255 * (1 - (health_percentage - 0.5) * 2))
            g = 255
        else:
            # Yellow to Red
            r = 255
            g = int(255 * health_percentage * 2)
        return (r, g, 0)  # No blue component