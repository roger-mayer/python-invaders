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

        # For fullscreen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.ket == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
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
