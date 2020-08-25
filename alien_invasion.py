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
            self._check_events()
            self.ship.update()
            self._update_screen()

    # Respond to key and mouse events
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        # update images on screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # show most recent screen
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance
    ai = AlienInvasion()
    ai.run_game()
