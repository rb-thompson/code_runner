# src/game/coffee.py
import pygame
import random
from ..configs import *

class Coffee(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = self.load_images_from_sheet(COFFEE_SPRITE_SHEET, 1, 6)
        self.index = 0
        self.image = self.animations[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.float_speed = 1  # Speed at which coffee floats up and down
        self.float_direction = 1  # 1 for up, -1 for down

    def load_images_from_sheet(self, sheet_path, rows, cols):
        sprite_sheet = pygame.image.load(sheet_path).convert_alpha()
        sheet_width, sheet_height = sprite_sheet.get_size()
        frame_width = sheet_width // cols
        frame_height = sheet_height // rows
        animation_list = []
        
        for row in range(rows):
            for col in range(cols):
                frame_location = (col * frame_width, row * frame_height)
                image = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA, 32)
                image.blit(sprite_sheet, (0, 0), (frame_location, (frame_width, frame_height)))
                animation_list.append(image)
        return animation_list

    def update(self):
        self.apply_animation()
        self.float()

    def apply_animation(self):
        SPEED = 10
        self.counter += 1
        if self.counter >= SPEED:
            self.counter = 0
            self.index = (self.index + 1) % len(self.animations)
        self.image = self.animations[self.index]

    def float(self):
        # Simple floating effect
        self.rect.y += self.float_speed * self.float_direction
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
            self.float_direction *= -1