import pygame


class Ship:
    def __init__(self, x, y, image):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.x_move = 0
        self.state = "normal"

    def draw_ship(self, screen):
        screen.blit(self.image, (self.x, self.y))

'''

Class 
    Ship
    {
        Functions
        
        __init__(self, x, y, image)
        draw_ship(self, screen)
        
        function __init__(self, x, y, image)
        {
            self.image = pygame.image.load(image)
            self.x = x
            self.y = y
            self.x_move = 0
            self.state = "normal"
        }
        
        end __init__(self, x, y, image)
        
        function draw_ship(self, screen):
        {
        read screen
            screen.blit(self.image, (self.x, self.y))
        }            
'''
