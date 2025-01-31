# src/game/player.py
import pygame
import random
from ..configs import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, game_state):
        super().__init__()
        self.animations = {
            'idle': self.load_images_from_sheet(PLAYER_SPRITE_SHEET, 1, 6),
            'kick': self.load_images_from_sheet(KICK_SPRITE_SHEET, 1, 6),
            'punch': self.load_images_from_sheet(PUNCH_SPRITE_SHEET, 1, 6),
        }
        self.state = 'idle'
        self.index = 0
        self.image = self.animations[self.state][self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

        # Player status
        self.coins = 0
        self.experience = 0  # Starts at 0, level calculation will be based on this
        self.level = 1
        self.base_damage = 1  # Set a base damage value for the player

        # Movement and physics
        self.velocity_y = 1       # Alters the hump height
        self.jump_strength = -25
        self.gravity = 1
        self.speed = 10

        # Attack mechanics
        self.attacking = False
        self.attack_cooldown = 0

        # Store game state reference
        self.game_state = game_state
        self.health = 100

        # For flipping the sprite
        self.facing_right = True  # Assume player starts facing right

    # New methods to manage coins and experience
    def add_coins(self, amount):
        self.coins += amount

    def add_experience(self, amount):
        self.experience += amount
        self._update_level()

    def _update_level(self):
        # Simple level calculation. Adjust this formula as needed
        new_level = int(self.experience ** 0.5) + 1  # Example: sqrt(exp) + 1 for level
        if new_level > self.level:
            self.level = new_level
            print(f"Player leveled up to level {self.level}!")  # For debugging, replace with actual level up logic

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
        self.check_collisions()
        self.apply_physics()
        self.apply_animation()
        self.handle_bounds()

    def apply_animation(self):
        SPEED = 2
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
        
        # Flip the sprite based on direction
        self.image = self.animations[self.state][self.index]
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)  # Flip horizontally
        self.rect = self.image.get_rect(center=self.rect.center)  # Update rect to match new image

    def apply_physics(self):
        # Apply gravity and vertical movement regardless of attack state
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Ground check only if not attacking mid-air
        if not self.attacking or self.rect.bottom > SCREEN_HEIGHT - GROUND_HEIGHT:
            if self.rect.bottom > SCREEN_HEIGHT - GROUND_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
                self.velocity_y = 0

        if self.attacking:
            self.attack_cooldown = max(0, self.attack_cooldown - 1)

    def handle_bounds(self):
        # Ensure equal padding on left and right
        left_bound = PLAYER_WIDTH // 3
        right_bound = SCREEN_WIDTH - PLAYER_WIDTH // 3
        self.rect.clamp_ip(pygame.Rect(left_bound, 0, right_bound - left_bound, SCREEN_HEIGHT - GROUND_HEIGHT))
        
    def jump(self):
        if self.is_on_ground_or_platform():
            self.velocity_y = self.jump_strength
            # Emit smoke particles at the player's feet when jumping
            self.game_state.player_jumped(self)

    def is_on_ground_or_platform(self):
        # Check if on ground
        if self.rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
            return True
        
        # Check if on platform
        for platform in self.game_state.platforms:
            if (self.rect.bottom >= platform.rect.top and 
                self.rect.bottom <= platform.rect.centery and
                self.rect.right > platform.rect.left and 
                self.rect.left < platform.rect.right):
                return True
        return False

    def on_platform(self):
        return pygame.sprite.spritecollideany(self, self.game_state.platforms)
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            # Handle game over scenario
            print("Game Over!")

    def attack(self):
        if not self.attacking and self.attack_cooldown == 0:
            self.state = random.choice(['kick', 'punch'])
            self.index = 0
            self.attacking = True
            if self.state != 'punch':  # Keep some cooldown for kick if needed
                self.attack_cooldown = 5

    def move_left(self):
        self.rect.x -= self.speed
        self.facing_right = False  # Update facing direction

    def move_right(self):
        self.rect.x += self.speed
        self.facing_right = True  # Update facing direction

    def check_collisions(self):
        if DEBUG:
            print(f"Player pos before collision: {self.rect.x, self.rect.y}")

        # Always check collisions, even when not falling
        hits = pygame.sprite.spritecollide(self, self.game_state.platforms, False)
        platform_under = None
        if hits:
            # Find the highest platform the player is colliding with
            for platform in hits:
                # Simplified collision check - if player is above the platform
                if self.rect.bottom <= platform.rect.centery and self.velocity_y > 0:
                    if not platform_under or platform.rect.top < platform_under.rect.top:
                        platform_under = platform
            
            if platform_under:
                self.rect.bottom = platform_under.rect.top
                self.velocity_y = 0
                self.rect.x += platform_under.speed  # Move with the platform if landing on it
            
        # Ground collision check
        if self.rect.bottom > SCREEN_HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
            self.velocity_y = 0

        # Check for enemy collisions
        for enemy in self.game_state.enemies:
            # Expand the player's attack range
            attack_rect = self.rect.copy()
            if self.facing_right:
                attack_rect.right += ATTACK_RANGE_EXTENSION  # Example: Extend to the right
            else:
                attack_rect.left -= ATTACK_RANGE_EXTENSION  # Example: Extend to the left
            
            if attack_rect.colliderect(enemy.rect):
                if self.attacking:
                    enemy.take_damage(self.base_damage)
        
        if DEBUG:
            print(f"Player pos after collision: {self.rect.x, self.rect.y}")
            print(f"Platform pos: {[p.rect.x for p in self.game_state.platforms]}")