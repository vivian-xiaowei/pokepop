from typing import Any

import pygame
from pygame import *
import pygame.sprite

ball_images = [[] for i in range(7)]
for i in range(7):
    for j in range(8):
        ball_images[i].append(pygame.image.load("balls/" + str(i) + str(j) + ".png"))


# pokeball class with the image, position, angle of rotation and rect for collision
class pokeballs:
    def __init__(self, ball_image, x_pos, y_pos):
        self.ball_image = ball_image
        self.rect = self.ball_image.get_rect()
        self.angle = 0
        self.pos = [x_pos, y_pos]
        self.rect.center = self.pos
        self.road_h = 0
        self.road_v = 0
        self.move = 0.8

    # loop through the images
    def roll(self, speed):
        self.angle += speed
        if int(self.angle) >= 8:
            self.angle = 0
        self.ball_image = ball_images[0][int(self.angle)]

    def move(self, direction, speed):
        self.pos[direction] += speed

    def draw(self, window):
        window.blit(self.ball_image, self.pos)
