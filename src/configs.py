# src/configs.py 
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

TITLE = "CODE RUNNER"

# Colors for dark mode
BACKGROUND_COLOR = (20, 20, 20)  # Very dark gray
GROUND_COLOR = (50, 50, 50)      # Dark gray for the ground
PLAYER_COLOR = (255, 255, 255)   # White for the player (placeholder)

PLAYER_WIDTH = 150
PLAYER_HEIGHT = 300
GROUND_HEIGHT = 50


import os  # Import os at the end to avoid circular import issues

# Path to assets directory
ASSETS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
PLAYER_SPRITE_SHEET = os.path.join(ASSETS_PATH, 'sprites', 'player_sprite_sheet.png')
KICK_SPRITE_SHEET = os.path.join(ASSETS_PATH, 'sprites', 'player_kick_sheet.png')
PUNCH_SPRITE_SHEET = os.path.join(ASSETS_PATH, 'sprites', 'player_punch_sheet.png')
BACKGROUND_IMAGE = os.path.join(ASSETS_PATH, 'background', 'background.png')