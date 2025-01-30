# src/configs.py 
import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

TITLE = "CODE RUNNER"

# Colors for dark mode
BACKGROUND_COLOR = (20, 20, 20)  # Very dark gray
GROUND_COLOR = (50, 50, 50)      # Dark gray for the ground
PLAYER_COLOR = (255, 255, 255)   # White for the player (placeholder)

PLAYER_WIDTH = 150
PLAYER_HEIGHT = 200
GROUND_HEIGHT = 50

HEALTH_BAR_WIDTH = 200
HEALTH_BAR_HEIGHT = 20
STATUS_BAR_COLOR = (100, 100, 100)  # Dark gray
HEALTH_COLOR = (255, 0, 0)  # Red for health bar
TEXT_COLOR = (255, 255, 255)  # White for text
STATUS_BAR_ICON_SIZE = 20  # Size for small icons

# Debug settings
DEBUG = False  # Set to True to enable debug prints

import os  # Import os at the end to avoid circular import issues

# Path to assets directory
ASSETS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
PLAYER_SPRITE_SHEET = os.path.join(ASSETS_PATH, 'sprites', 'player_sprite_sheet.png')
KICK_SPRITE_SHEET = os.path.join(ASSETS_PATH, 'sprites', 'player_kick_sheet.png')
PUNCH_SPRITE_SHEET = os.path.join(ASSETS_PATH, 'sprites', 'player_punch_sheet.png')
BACKGROUND_IMAGE = os.path.join(ASSETS_PATH, 'background', 'background.png')