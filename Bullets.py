import pygame


class Bullet:
    def __init__(self, x, y, type, image):
        self.x = x
        self.y = y
        self.type = type
        self.image = pygame.image.load(image)
        if self.type == "ship":
            self.state = "ready"

    def ship_shoot(self):
        self.change = -17
        self.image = pygame.image.load("bullet.png")
        if self.state == "ready":
            self.state = "fire"
        self.y = 557

    def bullet_move(self, ship):
        if self.state == "fire":
            self.y += self.change
            if self.y <= 0:
                self.state = "ready"
                self.x = ship.x
                self.y = 771

    def draw_bullet(self, screen):
        screen.blit(self.image, (self.x, self.y))

'''

Classes
    {
        Bullet
        {
            __init__(self, x, y, type, image)
            def ship_shoot(self)
            ship_shoot(self)
            def bullet_move(self, ship)
            draw_bullet(self, screen)
            
            function __init__(self, x, y, type, image)
            {
                read x
                read y
                read type
                read image
                
                self.x = x
                self.y = y
                self.type = type
                self.image = pygame.image.load(image)
                if self.type == "ship"
                    self.state = "ready"
            }
            
            end __init__(self, x, y, type, image)
            
            function ship_shoot(self)
            {
                self.change = -17
                self.image = pygame.image.load("bullet.png")
                if self.state == "ready"
                    self.state = "fire"
                self.y = 557
            }
            
            end ship_shoot
        
            function bullet_move(self, ship)
            {
                read ship
                
                if self.state == "fire"
                    self.y += self.change
                    if self.y <= 0
                        self.state = "ready"
                        self.x = ship.x
                        self.y = 771
            }
            
            end bullet_move(self, ship)
            
            function draw_bullet(self, screen)
            {
                read screen
                
                screen.blit(self.image, (self.x, self.y))
            }
            
            end draw_bullet(self, screen)
            
'''