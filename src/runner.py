# src/runner.py
import pygame
from src.configs import *
from src.game.game_state import GameState
from src.gui.main_menu import MainMenu
from src.log_handler import get_logger

logger = get_logger(__name__)

class GameRun:
    def __init__(self):
        logger.info("Initializing GameRun")

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.game_state = GameState()
        self.main_menu = MainMenu(self.screen)
        self.current_state = "menu"  # Use this to switch between menu and game

    def main(self):
        logger.info("Starting main game loop")

        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False

            if self.current_state == "menu":
                screen_action = self.main_menu.handle_events(events)
                if screen_action == "play":
                    self.current_state = "game"
            elif self.current_state == "game":
                self.game_state.handle_events(events)

            if self.current_state == "menu":
                self.main_menu.draw()
            elif self.current_state == "game":
                self.game_state.update()
                self.game_state.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def __del__(self):
        logger.info("Cleaning up GameRun")
        pygame.quit()