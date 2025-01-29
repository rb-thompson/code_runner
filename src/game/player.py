# src/game/player.py
import pygame
import random
from ..configs import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load animations
        self.animations = {
            'idle': self.load_images_from_sheet(PLAYER_SPRITE_SHEET, 1, 6), # 6 frames for walk
            'kick': self.load_images_from_sheet(KICK_SPRITE_SHEET, 1, 6),  # 6 frames for kick
            'punch': self.load_images_from_sheet(PUNCH_SPRITE_SHEET, 1, 6),  # 6 frames for punch
        }
        self.state = 'idle'
        self.index = 0
        self.image = self.animations[self.state][self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

        # Movement mechanics
        self.velocity_y = 0
        self.jump_strength = -15
        self.gravity = 0.8

        # Attack mechanics
        self.attacking = False
        self.attack_cooldown = 0

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
        # Animation update
        SPEED = 5  # You might want to adjust this for longer animations like punch and kick
        self.counter += 1
        if self.counter >= SPEED:
            self.counter = 0
            if self.attacking:
                self.index += 1
                if self.index >= len(self.animations[self.state]):
                    self.index = 0
                    self.attacking = False
                    self.state = 'idle'
            else:
                self.index = (self.index + 1) % len(self.animations[self.state])
        self.image = self.animations[self.state][self.index]

        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Ground check
        if self.rect.bottom > SCREEN_HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
            self.velocity_y = 0

        # Attack cooldown
        if self.attacking:
            self.attack_cooldown = max(0, self.attack_cooldown - 1)

    def jump(self):
        if self.rect.bottom == SCREEN_HEIGHT - GROUND_HEIGHT:
            self.velocity_y = self.jump_strength

    def attack(self):
        if not self.attacking and self.attack_cooldown == 0:
            self.state = random.choice(['kick', 'punch'])
            self.index = 0
            self.attacking = True
            self.attack_cooldown = 10  # Adjust this value based on how long the animation takes