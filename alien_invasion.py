import sys

import pygame

from settings  import Settings
from ship import Ship
from character import Character


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0 ), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.character = Character(self)
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            #Redraw the screen during each pass through the loop. 
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()
            
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Rsspond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   sys.exit()
            elif event.type == pygame.KEYDOWN:
                 self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)

    def _check_keydown_events(self, event3):
        """Respond to keypresses."""
        if event3.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event3.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event3.key == pygame.K_q:
             sys.exit()
    
    def _check_keyup_events(self, event3):
         """Respond to key releases."""
         if event3.key == pygame.K_RIGHT:
              self.ship.moving_right = False
         elif event3.key == pygame.K_LEFT:
              self.ship.moving_left = False
              

    def _update_screen(self):
         """Update images on thre screen, and flip to the new screen."""
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()
         self.character.blit_char()
         #Make the most recently drawn screen visible.
         pygame.display.flip()


if __name__ == "__main__":
        ai = AlienInvasion()
        ai.run_game()


