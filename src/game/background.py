# src/game/background.py
import pygame
from ..configs import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE

class Background:
    def __init__(self):
        self.image = pygame.image.load(BACKGROUND_IMAGE).convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH * 2, SCREEN_HEIGHT))  # Make image twice the screen width for seamless looping
        self.rect = self.image.get_rect()
        self.x_pos = 0
        self.speed = 1  # Adjust this to change scroll speed

    def update(self):
        self.x_pos -= self.speed
        if self.x_pos <= -SCREEN_WIDTH:  # When the leftmost part of the image is off-screen
            self.x_pos = 0  # Reset to start

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, 0))
        # Draw the second part of the image to the right to make the loop seamless
        screen.blit(self.image, (self.x_pos + SCREEN_WIDTH, 0))