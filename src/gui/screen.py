import pygame

class Screen:
    def __init__(self, screen):
        self.screen = screen

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self):
        pass

    def draw(self):
        pass