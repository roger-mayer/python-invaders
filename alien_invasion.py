import sys

import pygame
from settings import Settings
from ship import Ship


# Overall class to manage game assets and behavior
class AlienInvasion:

    def __init__(self):
        # Initialize game, create game resources
        pygame.init()
        self.settings = Settings()

        # instance of Settings class to set display
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        # Start main loop for game
        while True:
            # Watch for key board and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw game each time through loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # show most recent screen
            pygame.display.flip()


if __name__ == '__main__':
    # make a game instance
    ai = AlienInvasion()
    ai.run_game()
