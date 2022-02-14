
import pygame
import sys
from Alien import Alien
from Ship import Ship
from Bullets import Bullet
from pygame import mixer

pygame.init()

window_length = 1200
window_width = 686
screen = pygame.display.set_mode((window_length, window_width))
ship = Ship(x=574, y=579, image="Player_ship.png")
white = (255, 255, 255)
black = (0, 0, 0)
red = (182, 0, 22)
light_red = (255, 0, 0)
green = (0, 155, 0)
light_green = (0, 255, 0)
yellow = (165, 165, 5)
light_yellow = (255, 211, 25)
blue = (114, 170, 170)
light_blue = (110, 225, 225)


background = pygame.image.load("background.png")
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)
font = pygame.font.Font("Transformers Movie.ttf", 28)
intro_font = pygame.font.Font("Transformers Movie.ttf", 45)
score_font = pygame.font.Font("Transformers Movie.ttf", 24)
game_over_font = pygame.font.Font("Transformers Movie.ttf", 43)
button_font = pygame.font.Font("Transformers Movie.ttf", 31)
text_x = 10
text_y = 10
intro_menu = pygame.image.load("menu.png")
pause_menu = pygame.image.load("pause.png")
clock = pygame.time.Clock()


class Button:

    def __init__(self, text, x, y, width, height, inactive_colour, active_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive = inactive_colour
        self.active = active_color
        self.hover = False
        self.click = False

    def draw_button(self):
        '''
        :return:
        '''
        self.check_hover()

        if self.hover:
            text = button_font.render(self.text, True, self.active)
        else:
            text = button_font.render(self.text, True, self.inactive)
        screen.blit(text, (self.x, self.y))

    def check_hover(self):
        '''
        :return:
        '''
        cursor = pygame.mouse.get_pos()
        self.hover = False

        if self.x + self.width > cursor[0] > self.x and self.y + self.height > cursor[1] > self.y:
            self.hover = True


def show_button(buttons):
    '''
    :param buttons:
    :return:
    '''
    for button in buttons:
        button.draw_button()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                for button in buttons:
                    button.check_hover()
                    if button.hover:
                        button.click = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def pause(score_value):
    '''
    :param score_value:
    :return:
    '''
    paused = True
    continue_button = Button("Continue", 171, 184, 257, 28, green, light_green)
    main_menu_button = Button("Main Menu", 171, 321, 326, 28, blue, light_blue)
    quit_button = Button("Quit", 171, 437, 210, 28, red, light_red)
    buttons = [continue_button, main_menu_button, quit_button]
    while paused:
        screen.blit(pause_menu, (0, 0))
        pause_message = font.render("Paused", True, white)
        current_score = font.render(f"Current Score: {str(score_value)}", True, red)
        screen.blit(pause_message, (1029, 43))
        screen.blit(current_score, (171, 43))
        show_button(buttons)
        pygame.display.update()

        if continue_button.click:
            continue_button.click = False
            break
        if main_menu_button.click:
            main_menu_button.click = False
            main_menu()
        if quit_button.click:
            pygame.quit()
            sys.exit()


def main_menu():
    '''
    :return:
    '''
    mixer.music.stop()
    mixer.music.load("background music.mp3")
    mixer.music.set_volume(0.6)
    mixer.music.play(-1)
    play_button = Button("Play Game", 514, 261, 163, 28, blue, light_blue)
    tutorial_button = Button("Tutorial", 535, 356, 124, 28, yellow, light_yellow)
    quit_button = Button("Quit", 568, 450, 54, 28, red, light_red)
    buttons = [play_button, quit_button, tutorial_button]

    while True:

        screen.blit(intro_menu, (0, 0))

        message1 = intro_font.render("Game Created By", True, white)
        message2 = intro_font.render("Erfan Nazarian", True, light_green)
        screen.blit(message1, (28, 566))
        screen.blit(message2, (28, 617))

        show_button(buttons)
        if quit_button.click:
            pygame.quit()
            sys.exit()
        if play_button.click:
            play_button.click = False
            gaming_loop()
        if tutorial_button.click:
            tutorial_button.click = False
            tutorial()

        pygame.display.update()


def tutorial():
    '''
    :return:
    '''
    while True:

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        message1 = font.render("GAME CONTROLS", True, white)
        message2 = score_font.render("The goal of Space invaders is to shoot the enemies", True, white)
        message3 = score_font.render("Press the SPACE button to shoot enemies", True, white)
        message4 = score_font.render("Press the LEFT and RIGHT arrows to move around", True, white)
        message5 = score_font.render("Press the ESCAPE to pause", True, white)
        message6 = score_font.render("Take aim before shooting:", True, light_red)
        message7 = score_font.render("- You can only shoot again if a bullet is gone or if you hit an alien.", True,
                                     light_red)
        screen.blit(message1, (214, 69))
        screen.blit(message2, (214, 171))
        screen.blit(message3, (214, 206))
        screen.blit(message4, (214, 240))
        screen.blit(message5, (214, 274))
        screen.blit(message6, (214, 309))
        screen.blit(message7, (223, 351))
        return_button = Button("Return", 214, 489, 98, 28, green, light_green)
        buttons = [return_button]
        show_button(buttons)
        pygame.display.update()
        if return_button.click:
            break


def show_score(x, y, score_value):
    '''
    :param x:
    :param y:
    :param score_value:
    :return:
    '''
    score = score_font.render(f"Score {str(score_value)}", True, white)
    pause_message = score_font.render("Press \"ESC\" to Pause ", True, white)
    screen.blit(score, (x, y))
    screen.blit(pause_message, (x, y + 43))
    pygame.display.update()


def collision_check(enemy, b):
    enemy_rect = pygame.Rect((enemy.x-1), (enemy.y-1), (enemy.image.get_width()+1), (enemy.image.get_height()+1))
    b_rect = pygame.Rect((b.x-2), (b.y-2), (b.image.get_width()+2), (b.image.get_height()+2))
    if enemy_rect.colliderect(b_rect):
        return True
    return False


def game_over_text(score_value):
    game_over_sound = mixer.Sound("Game over.mp3")
    mixer.Sound.play(game_over_sound)
    while True:
        screen.fill((0, 0, 0))
        screen.blit(intro_menu, (0, 0))
        text = game_over_font.render("Game Over", True, light_red)
        text2 = game_over_font.render("You fought valiantly to protect earth", True, light_blue)
        text3 = game_over_font.render(f"You Scored: {str(score_value)}", True, white)
        screen.blit(text, (223, 43))
        screen.blit(text2, (223, 103))
        screen.blit(text3, (223, 163))
        quit_button = Button("Quit", 840, 407, 54, 28, red, light_red)
        main_menu_button = Button("Main", 253, 407, 71, 28, blue, light_blue)
        retry_button = Button("Retry", 536, 407, 81, 28, green, light_green)
        buttons = [quit_button, main_menu_button, retry_button]
        ship.move = 0
        show_button(buttons)
        if retry_button.click:
            retry_button.click = False
            gaming_loop()
        if main_menu_button.click:
            main_menu_button.click = False
            main_menu()
        if quit_button.click:
            pygame.quit()
            sys.exit()
        pygame.display.update()


def gaming_loop():
    mixer.music.stop()
    mixer.music.load("gameplay music.mp3")
    mixer.music.set_volume(0.6)
    mixer.music.play(-1)
    aliens = []
    count = 0
    score_value = 0
    ship.x_move = 0
    bullet = Bullet(ship.x, ship.y, "ship", "bullet.png")
    while True:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        pygame.draw.line(screen, light_red, (0, 527), (1200, 531), 4)
        ship.x += ship.x_move
        ship.draw_ship(screen)

        if len(aliens) == 0:
            x = 86
            y = 77

            for i in range(24):
                alien = Alien(x, y, "Enemy.png")
                x += 146
                if i == 7:
                    x = 86
                    y += 115
                if i == 15:
                    x = 86
                    y += 115
                alien.x_move += count
                aliens.append(alien)
            count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship.x_move = -8.5
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship.x_move = 8.5
                elif event.key == pygame.K_SPACE:
                    if bullet.state == "ready":
                        shoot_sound = mixer.Sound("Shoot.mp3")
                        mixer.Sound.play(shoot_sound)
                        bullet.ship_shoot()
                if event.key == pygame.K_ESCAPE:
                    pause(score_value)
                    ship.x_move = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship.x_move = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship.x_move = 0

        if bullet.state == "fire":
            bullet.bullet_move(ship)
            bullet.draw_bullet(screen)
        if ship.x <= 0:
            ship.x = 0
        if ship.x >= 1200 - 75:
            ship.x = 1200 - 75

        for alien in aliens:
            alien.draw_alien(alien.x, alien.y, screen)
            if alien.y > 514:
                mixer.music.stop()
                game_over_text(score_value)
            else:
                alien.move()

            collision_alien = collision_check(alien, bullet)
            if collision_alien:
                bullet.state = "ready"
                bullet.y = 583
                explosion_sound = mixer.Sound("Explosion-n.mp3")
                mixer.Sound.play(explosion_sound)
                aliens.remove(alien)
                score_value += 100
                for alien in aliens:
                    if alien.x_move < 0:
                        alien.x_move -= 0.3
                    else:
                        alien.x_move += 0.3
        if bullet.state == "ready":
            bullet.x = ship.x + 21

        show_score(text_x, text_y, score_value)
        pygame.display.update()
        clock.tick(61)


main_menu()




'''

import pygame
import sys
from Alien import Alien
from Ship import Ship
from Bullets import Bullet
from pygame import mixer

pygame.init()

Classes:
    Button
    {
    
        Functions:
        
        __init__(self, text, x, y, width, height, inactive_colour, active_color)
        draw_button(self)
        check_hover(self)
        
        function __init__(self, text, x, y, width, height, inactive_colour, active_color)
        {
            self.text = text
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.inactive = inactive_colour
            self.active = active_color
            self.hover = False
            self.click = False
        }
            
        end __init__(self, text, x, y, width, height, inactive_colour, active_color)
        
        function draw_button(self)
        {
            self.check_hover()
            
            if self.hover
                text = button_font.render(self.text, True, self.active)
            else
                text = button_font.render(self.text, True, self.inactive)
            screen.blit(text, (self.x, self.y))
        }
        
        end draw_button(self)
        
        function check_hover(self)
        {
            cursor = pygame.mouse.get_pos()
        self.hover = False

        if self.x + self.width > cursor[0] > self.x and self.y + self.height > cursor[1] > self.y:
            self.hover = True
        }
        
        end check_hover(self)
    }
    
Functions
    
    show_button(buttons)
    pause(score_value)
    main_menu()
    tutorial()
    show_scofe(x, y, score_value)
    collision_check(enemy, b)
    game_over_text(score_value)
    gaming_loop()
    
    function show_button(buttons)
    {
    
    read buttons
    
        for button in buttons
        {
            button.draw_button()
        }
        for event in pygame.event.get()
        {
            if event.type == pygame.MOUSEBUTTONDOWN
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    for button in buttons
                    {
                        button.check_hover()
                        if button.hover
                            button.click = True
                    }
            if event.type == pygame.QUIT
                pygame.quit()
                sys.exit()
        }
    }
    
    end show_button(buttons)
    
    function pause(score_value)
    {
    read score_value
        paused = True
        continue_button = Button("Continue", 171, 184, 257, 28, green, light_green)
        main_menu_button = Button("Main Menu", 171, 321, 326, 28, blue, light_blue)
        quit_button = Button("Quit", 171, 437, 210, 28, red, light_red)
        buttons = [continue_button, main_menu_button, quit_button]
        while paused
            {
            if continue_button.click 
                continue_button.click = False
                break
            if main_menu_button.click
                main_menu_button.click = False
                main_menu()
            if quit_button.click
                pygame.quit()
                sys.exit()
            }
    }
    
    end pause(score_value)
    
    function music_menu()
    {
        mixer.music.stop()
        mixer.music.load("background music.mp3")
        mixer.music.set_volume(0.6)
        mixer.music.play(-1)
        play_button = Button("Play Game", 514, 261, 163, 28, blue, light_blue)
        tutorial_button = Button("Tutorial", 535, 356, 124, 28, yellow, light_yellow)
        quit_button = Button("Quit", 568, 450, 54, 28, red, light_red)
        buttons = [play_button, quit_button, tutorial_button]
        
        while True
        {
            screen.blit(intro_menu, (0, 0))
    
            message1 = intro_font.render("Game Created By", True, white)
            message2 = intro_font.render("Erfan Nazarian", True, light_green)
            screen.blit(message1, (28, 566))
            screen.blit(message2, (28, 617))
    
            show_button(buttons)
            if quit_button.click
                pygame.quit()
                sys.exit()
            if play_button.click
                play_button.click = False
                gaming_loop()
            if tutorial_button.click
                tutorial_button.click = False
                tutorial()
    
            pygame.display.update()
        }
    }
    
    end main_menu()
    
    function tutorial()
    {
        while True
        {
            for events in pygame.event.get()
            {
                if events.type == pygame.QUIT
                    pygame.quit()
                    sys.exit()
            }
            screen.blit(background, (0, 0))
            message1 = font.render("GAME CONTROLS", True, white)
            message2 = score_font.render("The goal of Space invaders is to shoot the enemies", True, white)
            message3 = score_font.render("Press the SPACE button to shoot enemies", True, white)
            message4 = score_font.render("Press the LEFT and RIGHT arrows to move around", True, white)
            message5 = score_font.render("Press the ESCAPE to pause", True, white)
            message6 = score_font.render("Take aim before shooting:", True, light_red)
            message7 = score_font.render("- You can only shoot again if a bullet is gone or if you hit an alien.", True,
                                         light_red)
            screen.blit(message1, (214, 69))
            screen.blit(message2, (214, 171))
            screen.blit(message3, (214, 206))
            screen.blit(message4, (214, 240))
            screen.blit(message5, (214, 274))
            screen.blit(message6, (214, 309))
            screen.blit(message7, (223, 351))
            return_button = Button("Return", 214, 489, 98, 28, green, light_green)
            buttons = [return_button]
            show_button(buttons)
            pygame.display.update()
            if return_button.click
                break
        }
    }
    
    end tutorial()
    
    function show_score(x, y, score_value)
    {
    read x
    read y
    read score_value
        score = score_font.render(f"Score {str(score_value)}", True, white)
        pause_message = score_font.render("Press \"ESC\" to Pause ", True, white)
        screen.blit(score, (x, y))
        screen.blit(pause_message, (x, y + 43))
        pygame.display.update()
    }
    
    end show_score()
    
    function collision_check(enemy, b)
    {
    read enemy
    read b
        enemy_rect = pygame.Rect((enemy.x-1), (enemy.y-1), (enemy.image.get_width()+1), (enemy.image.get_height()+1))
        b_rect = pygame.Rect((b.x-2), (b.y-2), (b.image.get_width()+2), (b.image.get_height()+2))
            if enemy_rect.colliderect(b_rect):
                return True
        return False
    }
    
    end collision_check(enemy, b)
    
    function game_over_text(score_value)
    {
    read score_value
        game_over_sound = mixer.Sound("Game over.mp3")
        mixer.Sound.play(game_over_sound)
        while True
        {
            screen.fill((0, 0, 0))
            screen.blit(intro_menu, (0, 0))
            text = game_over_font.render("Game Over", True, light_red)
            text2 = game_over_font.render("You fought valiantly to protect earth", True, light_blue)
            text3 = game_over_font.render(f"You Scored: {str(score_value)}", True, white)
            screen.blit(text, (223, 43))
            screen.blit(text2, (223, 103))
            screen.blit(text3, (223, 163))
            quit_button = Button("Quit", 840, 407, 54, 28, red, light_red)
            main_menu_button = Button("Main", 253, 407, 71, 28, blue, light_blue)
            retry_button = Button("Retry", 536, 407, 81, 28, green, light_green)
            buttons = [quit_button, main_menu_button, retry_button]
            ship.move = 0
            show_button(buttons)
            if retry_button.click:
                retry_button.click = False
                gaming_loop()
            if main_menu_button.click:
                main_menu_button.click = False
                main_menu()
            if quit_button.click:
                pygame.quit()
                sys.exit()
            pygame.display.update()
        }
    }
    
    end game_over_text(score_value)
    
    function gaming_loop()
    {
        mixer.music.stop()
        mixer.music.load("gameplay music.mp3")
        mixer.music.set_volume(0.6)
        mixer.music.play(-1)
        aliens = []
        count = 0
        score_value = 0
        ship.x_move = 0
        bullet = Bullet(ship.x, ship.y, "ship", "bullet.png")
        while True
            {    
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            pygame.draw.line(screen, light_red, (0, 527), (1200, 531), 4)
            ship.x += ship.x_move
            ship.draw_ship(screen)
    
            if len(aliens) == 0
                x = 86
                y = 77
    
                for i in range(24)
                {
                    alien = Alien(x, y, "Enemy.png")
                    x += 146
                    if i == 7
                        x = 86
                        y += 115
                    if i == 15
                        x = 86
                        y += 115
                    alien.x_move += count
                    aliens.append(alien)
                }
                count += 1
    
            for event in pygame.event.get()
            {
                if event.type == pygame.QUIT
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a
                        ship.x_move = -8.5
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d
                        ship.x_move = 8.5
                    elif event.key == pygame.K_SPACE
                        if bullet.state == "ready":
                            shoot_sound = mixer.Sound("Shoot.mp3")
                            mixer.Sound.play(shoot_sound)
                            bullet.ship_shoot()
                    if event.key == pygame.K_ESCAPE
                        pause(score_value)
                        ship.x_move = 0
                if event.type == pygame.KEYUP
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a
                        ship.x_move = 0
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d
                        ship.x_move = 0
            }
    
            if bullet.state == "fire"
                bullet.bullet_move(ship)
                bullet.draw_bullet(screen)
            if ship.x <= 0
                ship.x = 0
            if ship.x >= 1200 - 75
                ship.x = 1200 - 75
    
            for alien in aliens
            {
                alien.draw_alien(alien.x, alien.y, screen)
                if alien.y > 514
                    mixer.music.stop()
                    game_over_text(score_value)
                else
                    alien.move()
    
                collision_alien = collision_check(alien, bullet)
                if collision_alien
                    bullet.state = "ready"
                    bullet.y = 583
                    explosion_sound = mixer.Sound("Explosion-n.mp3")
                    mixer.Sound.play(explosion_sound)
                    aliens.remove(alien)
                    score_value += 100
                    for alien in aliens
                    {
                        if alien.x_move < 0
                            alien.x_move -= 0.3
                        else
                            alien.x_move += 0.3
                    }
            }
            if bullet.state == "ready"
                bullet.x = ship.x + 21
    
            show_score(text_x, text_y, score_value)
            pygame.display.update()
            clock.tick(61)
        }
    }
    
    end gaming_loop()
    
    window_length = 1200
    window_width = 686
    screen = pygame.display.set_mode((window_length, window_width))
    ship = Ship(x=574, y=579, image="Player_ship.png")
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (182, 0, 22)
    light_red = (255, 0, 0)
    green = (0, 155, 0)
    light_green = (0, 255, 0)
    yellow = (165, 165, 5)
    light_yellow = (255, 211, 25)
    blue = (114, 170, 170)
    light_blue = (110, 225, 225)
    
    
    background = pygame.image.load("background.png")
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load("space.png")
    pygame.display.set_icon(icon)
    font = pygame.font.Font("Transformers Movie.ttf", 28)
    intro_font = pygame.font.Font("Transformers Movie.ttf", 45)
    score_font = pygame.font.Font("Transformers Movie.ttf", 24)
    game_over_font = pygame.font.Font("Transformers Movie.ttf", 43)
    button_font = pygame.font.Font("Transformers Movie.ttf", 31)
    text_x = 10
    text_y = 10
    intro_menu = pygame.image.load("menu.png")
    pause_menu = pygame.image.load("pause.png")
    clock = pygame.time.Clock()
'''