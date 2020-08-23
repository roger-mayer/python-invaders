import sys

import pygame


# Overall class to manage game assets and behavior
class AlienInvasion:

    def __init__(self):
        # Initialize game, create game resources
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230)

    def run_game(self):
        # Start main loop for game
        while True:
            # Watch for key board and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw game each time through loop
            self.screen.fill(self.bg_color)

            # show most recent screen
            pygame.display.flip()


if __name__ == '__main__':
    # make a game instance
    ai = AlienInvasion()
    ai.run_game()
