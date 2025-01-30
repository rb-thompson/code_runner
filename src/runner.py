# src/runner.py
import pygame
from src.configs import *
from src.game.game_state import GameState
from src.gui.main_menu import MainMenu
from src.log_handler import get_logger

logger = get_logger(__name__)

class GameRun:
    def __init__(self):
        logger.info("Starting the Game!")
        
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.game_state = GameState()
        self.main_menu = MainMenu(self.screen)
        self.current_state = "menu"
        self.fps_clock = pygame.time.Clock()
        self.fps_font = pygame.font.Font(None, 24)  # Moved font initialization here

    def main(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False

            if self.current_state == "menu":
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.current_state = "game"
            elif self.current_state == "game":
                keys = pygame.key.get_pressed()  
                if keys[pygame.K_LEFT]:
                    self.game_state.player.move_left()
                if keys[pygame.K_RIGHT]:
                    self.game_state.player.move_right()
                if keys[pygame.K_UP]:
                    self.game_state.player.jump()
                if keys[pygame.K_z]:
                    self.game_state.player.attack()

                self.game_state.handle_events(events)  # Handle other events like quitting

            if self.current_state == "menu":
                self.main_menu.draw()
            elif self.current_state == "game":
                self.game_state.update()
                self.game_state.draw(self.screen)

            # Calculate FPS
            fps = int(self.fps_clock.get_fps())
            fps_text = self.fps_font.render(f"FPS: {fps}", True, (255, 0, 0))  # Red text
            self.screen.blit(fps_text, (SCREEN_WIDTH - fps_text.get_width() - 10, 10))  # Position in top right corner
            
            pygame.display.flip()
            self.fps_clock.tick(FPS)
            self.clock.tick(FPS)

        pygame.quit()

    def __del__(self):
        pygame.quit()