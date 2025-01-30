# src/game/platform.py
import pygame
import random
from ..configs import SCREEN_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed=1):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill((200, 200, 200, 128))  # ARGB: A=128 for 50% opacity
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.height = height
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()  # Remove platform when it moves off screen