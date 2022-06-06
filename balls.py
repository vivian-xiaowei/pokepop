import pygame
from random import *

ball_images = [[] for i in range(7)]
for i in range(7):
    for j in range(8):
        image = pygame.image.load("balls/" + str(i) + str(j) + ".png")
        ball_images[i].append(pygame.transform.scale(image, (30, 30)))

balls_exist = set()


def pick_ball():  # randomly generate the two balls on the shooter and make sure the ball exist in the main list
    while True:
        rand = randint(0, 6)
        if rand in balls_exist:
            return rand


def generate_ball(level):
    ball = []
    position = 0
    while position <= 10:
        type = randint(0, 6)
        if position <= 20:
            balls_exist.add(type)
        for j in range(randint(1, 8 - level)):
            ball.append(pokeballs(type, 800 - position * 30, 100, 0, 3))
            position += 1
    return ball


# pokeball class with the ball_image, position, rotate of angle and rect for collision
class pokeballs:
    def __init__(self, ball_type, x_pos=0, y_pos=0, rotate=randint(0, 2), x_move=3, y_move=0):
        self.type = ball_type
        self.rotate = rotate  # the rotation of the ball
        self.ball_image = ball_images[self.type][int(self.rotate)]
        self.rect = self.ball_image.get_rect()
        self.angle = 0  # the angle of the image
        self.pos = [x_pos, y_pos]
        self.road_h, self.road_v = 0, 0
        self.speed = abs(x_move)
        self.x_move = x_move
        self.y_move = y_move

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
        self.roll(abs(self.x_move) / 7)

    def shooter_move(self, angle=False):
        x, y = self.pos
        if self.x_move == -1:
            self.pos = [x, y + self.y_move]
        else:
            self.pos = [x + self.x_move, y + self.y_move]
        if angle:
            if self.x_move == 3:
                self.angle = 90
            elif self.x_move == -3:
                self.angle = 270
            elif self.y_move == 3:
                self.angle = 0
            self.roll(self.speed / 7)

    def changePos(self, x, y):
        self.pos = [x, y]

    def positionY(self):
        return self.pos[1]

    def draw(self, window):
        self.ball_image = pygame.transform.rotate(ball_images[self.type][int(self.rotate)], self.angle)
        self.rect = self.ball_image.get_rect()
        window.blit(self.ball_image, self.pos)

    def shift(self, map):
        if map == 0:
            if self.road_h >= self.road_v:
                self.pos[0] += 15 * self.x_move / abs(self.x_move)
            else:
                self.pos[1] += 15
