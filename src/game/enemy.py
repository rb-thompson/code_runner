# src/game/enemy.py
import pygame
import random
from ..configs import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type):
        super().__init__()
        self.type = enemy_type
        self.animations = self.load_animations()
        self.state = 'idle'
        self.index = 0
        self.image = self.animations[self.state][self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

        self.speed = 2
        self.health = 1
        self.move_direction = -1
        
        if self.type == 'code_bug':
            self.speed = 2
            self.health = 1

    def load_animations(self):
        animations = {}
        if self.type == 'code_bug':
            animations['idle'] = self.load_images_from_sheet(CODE_BUG_IDLE_SHEET, 1, 6)
            # animations['move'] = self.load_images_from_sheet(CODE_BUG_MOVE_SHEET, 1, 4)  # Example for movement animation
            # animations['attack'] = self.load_images_from_sheet(CODE_BUG_ATTACK_SHEET, 1, 5)  # Example for attack animation
        # Add more enemy types here
        return animations
    
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
        self.move()

    def apply_animation(self):
        SPEED = 10  # Adjust this to change animation speed
        self.counter += 1
        if self.counter >= SPEED:
            self.counter = 0
            self.index = (self.index + 1) % len(self.animations[self.state])
        self.image = self.animations[self.state][self.index]

    def move(self):
        # Keep enemy on ground
        ground_y = SCREEN_HEIGHT - GROUND_HEIGHT - self.rect.height
        self.rect.y = ground_y
        
        # Move horizontally
        self.rect.x += self.speed * self.move_direction
        
        # Check if it has moved off-screen
        if self.rect.right < 0:
            self.kill()  # Remove from sprite group if off-screen

        # Randomly change direction for unpredictability
        if random.randint(1, 100) == 1:  # 1% chance to change direction
            self.move_direction *= -1

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()