import pygame
import numpy as np
import random


window_width = 1280
window_height = 720
FPS = 60
pic = pygame.image.load("background.png")
bak = pygame.image.load("T-34.png")
block = pygame.image.load("block.png")
bullet = pygame.image.load("bullet.png")
win_screen = pygame.image.load("win_screen.png")
font_name = pygame.font.match_font('arial')

display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Artillery")
clock = pygame.time.Clock()


class Bak(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.w
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = tank
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 540


class Bullet(pg.sprite.Sprite):
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

    def angle(self):

        letters = pg.font.Font(None, 40)
        black_colour = (0, 0, 0)

        users_angle = ""

        ready = False
        while not ready:
            for event in pygame.event.get():
                if event.type == pg.QUIT:
                    ready = True
                    pg.quit()
                    quit()
                else:

                    key = pygame.key.get_pressed()

                    if key[pygame.K_KP1]:
                        users_angle += "1"
                    if key[pygame.K_KP2]:
                        users_angle += "2"
                    if key[pygame.K_KP3]:
                        users_angle += "3"
                    if key[pygame.K_KP4]:
                        users_angle += "4"
                    if key[pygame.K_KP5]:
                        users_angle += "5"
                    if key[pygame.K_KP6]:
                        users_angle += "6"
                    if key[pygame.K_KP7]:
                        users_angle += "7"
                    if key[pygame.K_KP8]:
                        users_angle += "8"
                    if key[pygame.K_KP9]:
                        users_angle += "9"
                    if key[pygame.K_KP0]:
                        users_angle += "0"
                    if key[pygame.K_KP_ENTER]:
                        ready = True
                        self.angle = float("".join(users_angle))
            angle_data = letters.render("Start angle: " + user_input, True, black_colour)
            pygame.display.blit(data, (20, 20))
            pygame.display.update()

    def velocity(self):
        letters = pg.font.Font(None, 40)
        black_colour = (0, 0, 0)

        users_velocity = ""

        ready = False
        while not ready:
            for event in pygame.event.get():
                if event.type == pg.QUIT:
                    ready = True
                    pygame.quit()
                    quit()
                else:
                    if key[pygame.K_KP1]:
                        users_velocity += "1"
                    if key[pygame.K_KP2]:
                        users_velocity += "2"
                    if key[pygame.K_KP3]:
                        users_velocity += "3"
                    if key[pygame.K_KP4]:
                        users_velocity += "4"
                    if key[pygame.K_KP5]:
                        users_velocity += "5"
                    if key[pygame.K_KP6]:
                        users_velocity += "6"
                    if key[pygame.K_KP7]:
                        users_velocity += "7"
                    if key[pygame.K_KP8]:
                        users_velocity += "8"
                    if key[pygame.K_KP9]:
                        users_velocity += "9"
                    if key[pygame.K_KP0]:
                        users_velocity += "0"
                    if event.key == pg.K_RETURN:
                        ready = True
                        self.v_0 = float("".join(users_velocity))
            velocity_data = letters.render("Initial velocity: " + users_velocity, True, black_colour)
            pygame.display.blit(data, (20, 50))
            pygame.display.flip()
            clock.tick(30)

    def update(self):
        if self.aim:
            self.fly()
        if self.rect.bottom > 600:
            self.aim = False

    def data(self):
        self.angle()
        self.velocity()

    def fire(self):
        if self.rect.bottom <= 600:
            self.aim = True
        else:
            self.rect.x += 0
            self.rect.y += 0

    def fly(self):
        angle = self.angle()
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
        self.all_sprites = pg.sprite.Group()
        self.a = pg.sprite.Group()
        self.w = pg.sprite.Group()
        self.tr = pg.sprite.Group()
        self.Bak = Bak(self)
        self.Block = Block(self)
        self.Bullet= Bullet(self, self.Bak.rect.right - 5, self.Bak.rect.top - 10)

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
                if event.key == pygame.K_a:
                    if not self.Bullet.aim():
                        self.Bullet.rect.left = self.Bak.rect.right - 5
                        self.Bak.rect.top = self.Bak.rect.top - 10
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
            self.display.blit(WS, (20, 150))
            self.Bullet.v_0 = 0
            self.Bullet.gravity = 0


play = Game()

while True:
    play.start()
    play.run()

