import math

import pygame
from random import *
from math import *

ball_images = [[] for i in range(7)]
for i in range(7):
    for j in range(8):
        ball_images[i].append(pygame.image.load("balls/" + str(i) + str(j) + ".png"))


# pokeball class with the ball_image, position, rotate of angle and rect for collision
class pokeballs:
    def __init__(self, ball_type, x_pos, y_pos):
        self.type = ball_type
        self.rotate = 0
        self.ball_image = ball_images[self.type][self.rotate]
        self.rect = self.ball_image.get_rect()
        self.angle = 0
        self.pos = [x_pos, y_pos]
        self.rect.center = self.pos
        self.road_h, self.road_v = 0, 0
        self.x_move = 0.3
        self.y_move = 0.3
        # else:
        #     self.distance = 300
        #     self.circle_angle = 0

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

    def two_direction_move(self):
        self.pos[0] -= self.x_move
        self.pos[1] -= self.y_move
        self.angle = asin(self.x_move)

    def changePos(self, x, y):
        self.pos = [x, y]

    def positionY(self):
        return self.pos[1]

    def draw(self, window):
        self.ball_image = pygame.transform.rotate(self.ball_image, self.angle)
        window.blit(self.ball_image, self.pos)
