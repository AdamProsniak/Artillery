import pygame
import numpy as np
import random


window_width = 1280
window_height = 720
FPS = 60
pic = pygame.image.load("background.png")
bak = pygame.image.load("T-34.png")
block = pygame.image.load("Enemy.png")
bullet = pygame.image.load("bullet.png")
win_screen = pygame.image.load("win_screen.png")
font_name = pygame.font.match_font('arial')

display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Artillery")
clock = pygame.time.Clock()


class Bak(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.w
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = bak
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 540


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, width, height):
        self.groups = game.all_sprites, game.a
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = bullet
        self.rect = self.image.get_rect()

        self.rect.x = width
        self.rect.y = height
        self.t = 0
        self.v_0 = 0
        self.angle = 0
        self.angle_in_radians = self.angle * (np.pi / 180)
        self.gravity = 9.81
        self.aim = False

    def angler(self):

        letters = pygame.font.Font(None, 40)
        black_colour = (0, 0, 0)

        users_angle = ""

        ready = False
        while not ready:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ready = True
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        users_angle += "1"
                    if event.key == pygame.K_2:
                        users_angle += "2"
                    if event.key == pygame.K_3:
                        users_angle += "3"
                    if event.key == pygame.K_4:
                        users_angle += "4"
                    if event.key == pygame.K_5:
                        users_angle += "5"
                    if event.key == pygame.K_6:
                        users_angle += "6"
                    if event.key == pygame.K_7:
                        users_angle += "7"
                    if event.key == pygame.K_8:
                        users_angle += "8"
                    if event.key == pygame.K_9:
                        users_angle += "9"
                    if event.key == pygame.K_0:
                        users_angle += "0"
                    if event.key == pygame.K_RETURN:
                        ready = True
                        self.angle = float("".join(users_angle))
            angle_data = letters.render("Start angle: " + users_angle, True, black_colour)
            play.display.blit(angle_data, (20, 20))
            pygame.display.update()

    def velocity(self):
        letters = pygame.font.Font(None, 40)
        black_colour = (0, 0, 0)

        users_angle = ""

        ready = False
        while not ready:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ready = True
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        users_angle += "1"
                    if event.key == pygame.K_2:
                        users_angle += "2"
                    if event.key == pygame.K_3:
                        users_angle += "3"
                    if event.key == pygame.K_4:
                        users_angle += "4"
                    if event.key == pygame.K_5:
                        users_angle += "5"
                    if event.key == pygame.K_6:
                        users_angle += "6"
                    if event.key == pygame.K_7:
                        users_angle += "7"
                    if event.key == pygame.K_8:
                        users_angle += "8"
                    if event.key == pygame.K_9:
                        users_angle += "9"
                    if event.key == pygame.K_0:
                        users_angle += "0"
                    if event.key == pygame.K_RETURN:
                        ready = True
                        self.v_0 = float("".join(users_angle))

            velocity_data = letters.render("Initial velocity: " + users_angle, True, black_colour)
            play.display.blit(velocity_data, (20, 50))
            pygame.display.flip()
            clock.tick(30)

    def update(self):
        if self.aim:
            self.fly()
        if self.rect.bottom > 600:
            self.aim = False

    def data(self):
        self.angler()
        self.velocity()

    def fire(self):
        if self.rect.bottom <= 600:
            self.aim = True
        else:
            self.rect.x += 0
            self.rect.y += 0

    def fly(self):
        angle = self.angle
        v = self.v_0
        angle_in_radians = angle * (np.pi / 180)
        v_y = (v * np.sin(angle_in_radians))
        v_x = (v * np.cos(angle_in_radians))

        self.t += 0.125
        self.rect.x += v_x/8
        self.rect.y -= (v_y - (self.gravity * self.t))/8


class Block(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.tr
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = block
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(200, 1200)
        self.rect.y = 520


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()

    def start(self):
        self.all_sprites = pygame.sprite.Group()
        self.a = pygame.sprite.Group()
        self.w = pygame.sprite.Group()
        self.tr = pygame.sprite.Group()
        self.Bak = Bak(self)
        self.Block = Block(self)
        self.Bullet = Bullet(self, self.Bak.rect.right - 5, self.Bak.rect.top - 10)

    def background(self):
        self.display.blit(pic, (0, 0))

    def running_game(self):
        self.run = True
        while self.run:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.refresh()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.start()
                if event.key == pygame.K_a:
                    self.Bullet.data()
                if event.key == pygame.K_SPACE:
                    self.Bullet.fire()
                if event.key == pygame.K_n:
                    if  self.Bullet.aim == False:
                        self.Bullet.rect.left = self.Bak.rect.right - 5
                        self.Bullet.rect.top = self.Bak.rect.top - 10
                        self.Bullet.t = 0

    def refresh(self):
        self.all_sprites.update()
        self.win()

    def draw(self):
        self.background()
        self.all_sprites.draw(self.display)
        self.win()
        pygame.display.update()

    def win(self):
        if self.Block.rect.left < self.Bullet.rect.right < self.Block.rect.right and self.Block.rect.top <= self.Bullet.rect.bottom:
            self.display.blit(win_screen, (20, 150))
            self.Bullet.v_0 = 0
            self.Bullet.gravity = 0


play = Game()

while True:
    play.start()
    play.running_game()

