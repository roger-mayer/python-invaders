import sys

import pygame

# Overall class to manage game assets and behavior
class AlienInvasion:

    def __init__(self):
        # Initialize game, create game resources
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # Start main loop for game
        while True:
            # Watch for key board and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


