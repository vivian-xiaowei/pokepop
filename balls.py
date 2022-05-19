from typing import Any

import pygame
from pygame import *
import pygame.sprite

ball_images = [[] for i in range(7)]
for i in range(7):
    for j in range(8):
        ball_images[i].append(pygame.image.load("balls/" + str(i) + str(j) + ".png"))


# pokeball class with the ball_image, position, angle of rotation and rect for collision
class pokeballs:
    def __init__(self, ball_type, x_pos, y_pos):
        self.colour = ball_type
        self.ball_image = ball_images[ball_type][0]
        self.rect = self.ball_image.get_rect()
        self.angle = 0
        self.rotation = 0
        self.pos = [x_pos, y_pos]
        self.rect.center = self.pos
        self.road_h = 0
        self.road_v = 0
        self.x_move = 0.8
        self.y_move = 0.8

    # loop through the images
    def roll(self, speed):
        self.angle += speed
        if int(self.angle) >= 8:
            self.angle = 0
        self.ball_image = ball_images[0][int(self.angle)]

    def move(self, direction, speed):
        self.pos[direction] += speed
        print(self.x_move > 0 and direction == 0)
        if self.x_move > 0 and direction == 0:
            self.rotation = 90
        elif self.x_move < 0 and direction == 0:
            self.rotation = 270
        elif self.y_move > 0 and direction == 1:
            self.rotation = 0

    def draw(self, window):
        self.ball_image = pygame.transform.rotate(self.ball_image, self.rotation)
        window.blit(self.ball_image, self.pos)
