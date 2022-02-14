import pygame


class Alien:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.x_move = 4
        self.y_move = 55
        self.image = pygame.image.load(image)

    def draw_alien(self, x_pos, y_pos, screen):
        screen.blit(self.image, (x_pos, y_pos))

    def move(self):
        self.x += self.x_move
        if self.x >= 1200 - 64:
            self.x_move = -abs(self.x_move)
            if self.y < 1136:
                self.y += self.y_move
            else:
                self.y = 1136
        elif self.x <= 0:
            self.x_move = abs(self.x_move)
            if self.y < 1136:
                self.y += self.y_move
            else:
                self.y = 1136

'''

import pygame


Class
 
    Alien
    {
        Functions
        
        __init__(self, x, y, image)
        draw_alien(self, x_pos, y_pos, screen)
        move(self)
        
    function __init__(self, x, y, image)
    {
    read x
    read y
    read image
    
        self.x = x
        self.y = y
        self.x_move = 4
        self.y_move = 55
        self.image = pygame.image.load(image)
    }
    
    end __init__(self, x, y, image)

    function draw_alien(self, x_pos, y_pos, screen):
    {
    read x_pos
    read y_pos
    read screen
        screen.blit(self.image, (x_pos, y_pos))
    }
    
    end draw_alien
        
    function move(self)
    {
        self.x += self.x_move
        if self.x >= 1200 - 64
            self.x_move = -abs(self.x_move)
            if self.y < 1136
                self.y += self.y_move
            else
                self.y = 1136
        elif self.x <= 0
            self.x_move = abs(self.x_move)
            if self.y < 1136
                self.y += self.y_move
            else
                self.y = 1136
    }
    
    end move(self)
'''