import pygame
import random
from .player import Player                  # player
from .enemy import Enemy                    # foes
from .coffee import Coffee                  # coffee bonus
from .coin import Coin                      # coin rewards
from .particle import Particle              # particle emitter
from ..gui.status_bar import StatusBar      # status bar
from .background import Background          # background scrolling
from .platform import Platform              # platform generation
from ..configs import *                     # configuration
import pygame.mixer                         # audio 

class GameState:
    def __init__(self):
        self.current_screen = None
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(0, SCREEN_HEIGHT - PLAYER_HEIGHT - GROUND_HEIGHT, self)
        self.all_sprites.add(self.player)
        self.background = Background()
        self.status_bar = StatusBar(self.player)
        self.player.health = 100
        self.last_platform = None
        self.particles = pygame.sprite.Group()
        
        self.enemies = pygame.sprite.Group()
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 180  # Spawn an enemy every 3 seconds at 60 FPS
        self.difficulty_level = 1  # Initial difficulty level

        self.coins = pygame.sprite.Group()
        self.coffees = pygame.sprite.Group()
        self.coffee_spawn_chance = 0.3  # 30% chance to spawn coffee when an enemy is defeated
        self.bonus_timer = 0  # Timer for speed bonus
        self.bonus_duration = 600  # 10 seconds at 60 FPS

        # Initialize music
        pygame.mixer.init()
        pygame.mixer.music.load('assets/audio/gameplay_track.mp3')
        pygame.mixer.music.set_volume(0.5)  # Set volume to 50%
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely

    def update(self):
        self.all_sprites.update()
        self.background.update()
        self.generate_platforms()
        self.particles.update()
        self.generate_enemies()
        self.update_difficulty()
        self.check_coffee_pickup()
        self.apply_bonus()
        self.coins.update()

    def check_coffee_pickup(self):
        for coffee in self.coffees:
            if pygame.sprite.collide_rect(self.player, coffee):
                # Player picks up coffee
                self.player_picked_coffee()
                coffee.kill()

    def player_picked_coffee(self):
        print("Player picked up coffee, speed bonus activated!")
        self.player.speed_bonus = True
        self.bonus_timer = self.bonus_duration

    def apply_bonus(self):
        if self.bonus_timer > 0:
            self.bonus_timer -= 1
            if self.bonus_timer == 0:
                self.player.speed_bonus = False
                print("Speed bonus ended!")

    def update_difficulty(self):
        # Example of how difficulty might increase over time
        # Adjust this logic to fit the game's progression
        if self.player.experience > 100 * self.difficulty_level:
            self.difficulty_level += 1
            # Decrease spawn interval to increase difficulty
            self.enemy_spawn_interval = max(60, self.enemy_spawn_interval - 20)
            print(f"Difficulty increased to level {self.difficulty_level}. Spawn interval now: {self.enemy_spawn_interval}")

    def generate_enemies(self):
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer >= self.enemy_spawn_interval:
            self.enemy_spawn_timer = 0  # Reset timer
            # Spawn enemy at ground level
            x = SCREEN_WIDTH
            y = SCREEN_HEIGHT - GROUND_HEIGHT - ENEMY_HEIGHT  # Adjust based on enemy sprite height
            enemy = Enemy(x, y, 'code_bug', self)  # Pass self (GameState instance)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)

    def generate_platforms(self):
        if not self.platforms or self.platforms.sprites()[-1].rect.right < SCREEN_WIDTH - 600:
            x = SCREEN_WIDTH
            
            # Calculate a reasonable height range from the ground
            min_height = 200  # Minimum height from ground
            max_height = 200  # Maximum height from ground
            
            # Calculate y position relative to ground
            ground_level = SCREEN_HEIGHT - GROUND_HEIGHT
            y = ground_level - random.randint(min_height, max_height)
            
            # Use consistent platform dimensions
            width = 200  # Fixed width for all platforms
            height = 20  # Fixed height for all platforms
            
            platform = Platform(x, y, width, height)
            self.platforms.add(platform)
            self.all_sprites.add(platform)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
        return True
    
    def draw(self, screen):
        self.background.draw(screen)
        pygame.draw.rect(screen, GROUND_COLOR, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
        self.all_sprites.draw(screen)
        self.particles.draw(screen)
        self.status_bar.draw(screen)
        self.enemies.draw(screen)
        self.coins.draw(screen)
        # DEBUG: Activate hitboxes for troubleshooting and testing
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform.rect, 1)  # Green for platforms
        pygame.draw.rect(screen, (255, 0, 0), self.player.rect, 1)  # Red for player
        
        for enemy in self.enemies:
            pygame.draw.rect(screen, (0, 0, 255), enemy.rect, 2)  # Blue outline for enemies

    # Particle emitter
    def emit_particles(self, pos, particle_type, colors=None, size_range=(5, 10), count=10):
        for _ in range(count):
            particle = Particle(pos, particle_type, colors=colors, size_range=size_range)
            self.particles.add(particle)
            self.all_sprites.add(particle)

    # Particle emitter methods for player/enemy actions
    def player_jumped(self, player):
        self.emit_particles(self.player.rect.center, 'smoke', 
                    colors=[(105, 252, 83), (255, 255, 255), (255, 255, 255)], 
                    size_range=(1, 5), 
                    count=20)
        
    def enemy_defeated(self, enemy):
        print("Enemy health is <= 0, should trigger particles")
        self.emit_particles(enemy.rect.center, 'smoke', 
                    colors=[(105, 252, 83), (255, 255, 255), (255, 255, 255)], 
                    size_range=(1, 5), 
                    count=20)
        # Award experience for defeating the enemy
        self.player.add_experience(10)
        # Chance to spawn coffee
        if random.random() < self.coffee_spawn_chance:
            self.spawn_coffee(enemy.rect.centerx, enemy.rect.centery)
        # Spawn coins
        self.spawn_coins(enemy.rect.centerx, enemy.rect.centery)
        enemy.kill()

    def spawn_coffee(self, x, y):
        coffee = Coffee(x, y)
        self.coffees.add(coffee)
        self.all_sprites.add(coffee)

    def spawn_coins(self, x, y):
        num_coins = random.randint(1, 5)  # Random number of coins between 1-5
        for _ in range(num_coins):
            # Offset each coin slightly to give the effect of them jumping out
            offset_x = random.randint(-20, 20)
            coin = Coin(x + offset_x, y)
            self.coins.add(coin)
            self.all_sprites.add(coin)

    def player_collected_coin(self):
        self.player.add_coins(1)
        print(f"Player collected a coin! Total coins: {self.player.coins}")

    def add_experience(self, amount):
        self.experience += amount
        self._update_level()

    def _update_level(self):
        # Simple level calculation. Adjust this formula as needed
        new_level = int(self.experience ** 0.5) + 1  # Example: sqrt(exp) + 1 for level
        if new_level > self.level:
            self.level = new_level
            print(f"Player leveled up to level {self.level}!")  # For debugging, replace with actual level up logic
