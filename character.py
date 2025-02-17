import pygame

class Character:
    """A class a to manage the character"""
    
    def __init__(self, ai_character):
        """Initialize the game characterand set its starting position"""

        self.screen = ai_character.screen
        self.screen_rect = ai_character.screen.get_rect()

        self.image = pygame.image.load("images/red_alien.png")
        
        self.image.set_colorkey((255, 255, 255))

        self.image_rect = self.image.get_rect()
        # put that image in centre of the screen
        self.image_rect.center = self.screen_rect.center
        

    def blit_char(self):
        """Draw the character at its current location"""
        self.screen.blit(self.image, self.image_rect)



