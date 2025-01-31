# src/game/coin.py
import pygame
import random
from ..configs import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = self.load_images_from_sheet(COIN_SPRITE_SHEET, 1, 6)  # Assuming 6 frames for animation
        self.index = 0
        self.image = self.animations[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.lifetime = 300  # 5 seconds at 60 FPS
        self.fade_timer = 0
        self.jump_speed = -10  # Initial jump speed
        self.gravity = 0.5  # Gravity to make coins fall back down

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
        self.jump_and_fall()
        self.fade()

    def apply_animation(self):
        SPEED = 10
        self.counter += 1
        if self.counter >= SPEED:
            self.counter = 0
            self.index = (self.index + 1) % len(self.animations)
        self.image = self.animations[self.index]

    def jump_and_fall(self):
        # Apply gravity and initial jump
        self.rect.y += self.jump_speed
        self.jump_speed += self.gravity

        # Ensure coin doesn't go below the ground
        if self.rect.bottom > SCREEN_HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
            self.jump_speed = 0  # Stop the coin from moving once it lands

    def fade(self):
        self.fade_timer += 1
        if self.fade_timer >= self.lifetime:
            self.kill()
        else:
            # Simple fade effect by reducing alpha
            alpha = 255 - (255 * self.fade_timer // self.lifetime)
            self.image.set_alpha(alpha)