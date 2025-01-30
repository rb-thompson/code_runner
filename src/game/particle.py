# src/game/particle.py
import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, particle_type, colors=None, size_range=(5, 10), speed_range=(0.5, 1), lifetime_range=(30, 60)):
        super().__init__()
        self.type = particle_type
        
        # Size
        size = random.randint(*size_range)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Specific colors for smoke
        if colors and particle_type == 'smoke':
            self.color = random.choice(colors)
        elif particle_type == 'smoke':
            self.color = self._generate_smoke_color()  # Fallback to random smoky color if no specific colors provided
        else:
            self.color = (255, 255, 0)  # Default spark color
        
        # Fill the surface with the color, including alpha for transparency
        self.image.fill((*self.color, random.randint(100, 200)))  # Random alpha for varying transparency
        
        self.rect = self.image.get_rect(center=pos)
        self.lifetime = random.randint(*lifetime_range)
        self.velocity = [random.uniform(-speed_range[1], speed_range[1]), random.uniform(-speed_range[1], speed_range[1])]
        self.gravity = 0  # Optional: add gravity for a more natural fall

    def _generate_smoke_color(self):
        # Generate a color for smoke that looks smoky (dark grays with a hint of other colors)
        base = random.randint(50, 150)  # Base gray value
        r = base + random.randint(-20, 20)
        g = base + random.randint(-20, 20)
        b = base + random.randint(-20, 20)
        return (min(r, 255), min(g, 255), min(b, 255))

    def update(self):
        # Apply gravity (if you want particles to fall)
        self.velocity[1] += self.gravity
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()  # Remove the particle when its lifetime ends

        # Simulate fading for all types of particles
        current_alpha = self.image.get_alpha()
        if current_alpha is not None and current_alpha > 0:
            new_alpha = max(0, current_alpha - 5)
            self.image.set_alpha(new_alpha)