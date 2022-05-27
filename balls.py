import pygame
from random import *

ball_images = [[] for i in range(7)]
for i in range(7):
    for j in range(8):
        image = pygame.image.load("balls/" + str(i) + str(j) + ".png")
        ball_images[i].append(pygame.transform.scale(image, (30, 30)))


balls_exist = set()


def generate_ball(level):
    ball = []
    position = 0
    while position <= 25:
        type = randint(0, 6)
        balls_exist.add(type)
        for j in range(randint(1, 6 - level)):
            ball.append(pokeballs(type, 700 - position * 30, 100))
            position += 1
    return ball


# pokeball class with the ball_image, position, rotate of angle and rect for collision
class pokeballs:
    def __init__(self, ball_type, x_pos, y_pos):
        self.type = ball_type
        self.rotate = randint(0, 2)  # the rotation of the ball
        self.ball_image = ball_images[self.type][self.rotate]
        self.rect = self.ball_image.get_rect()
        self.angle = 0  # the angle of the image
        self.pos = [x_pos, y_pos]
        self.rect.center = self.pos
        self.road_h, self.road_v = 0, 0
        self.x_move = .3
        self.y_move = .3

    # loop through the images
    def roll(self, speed):
        self.rotate += speed
        if int(self.rotate) >= 8:
            self.rotate = 0
        self.ball_image = ball_images[self.type][int(self.rotate)]

    def move(self, direction, speed):
        self.pos[direction] += speed
        if self.x_move > 0 and direction == 0:
            self.angle = 90
        elif self.x_move < 0 and direction == 0:
            self.angle = 270
        elif self.y_move > 0 and direction == 1:
            self.angle = 0
        self.roll(abs(self.x_move) / 3.75)

    def changePos(self, x, y):
        self.pos = [x, y]

    def positionY(self):
        return self.pos[1]

    def draw(self, window):
        self.ball_image = pygame.transform.rotate(self.ball_image, self.angle)
        window.blit(self.ball_image, self.pos)

    def collide(self, window, x1, y1, x2, y2):
        return self.rect.colliderect(pygame.draw.line(window, (0, 0, 0), (x1, y1), (x2, y2)))
