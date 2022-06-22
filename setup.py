import pygame
from pygame import *
from pygame.image import load

pygame.init()
clock = time.Clock()

# setting up window size
WIN_X = int(1000)

# how tall the screen is going to be
WIN_Y = int(750)

# set the screen
window = pygame.display.set_mode((WIN_X, WIN_Y))

# lists of animations for level selection
map1_animation = []
map2_animation = []
map3_animation = []

for i in range(1, 5):
    map1_animation.append(transform.scale(load("level/leaf" + str(i) + ".png"), (80, 110)))
    map2_animation.append(transform.scale(load("level/cactus" + str(i) + ".png"), (100, 120)))
for i in range(1, 9):
    map3_animation.append(transform.scale(load("level/cube" + str(i) + ".png"), (100, 103)))

animations = [map1_animation, map2_animation, map3_animation]

red = 255, 0, 0
blue = 0, 0, 255
black = 0, 0, 0
colours = [red, blue, black]

index=0
image=map1_animation[0]
numbers=[]
for i in range(1,7):
    numbers.append(transform.scale(load("level/Level " + str(i) + ".png"), (25, 50)))

signs = []
for i in range(1, 4):
    signs.append(load("choose maps/" + str(i) + ".png"))

sign_pos = [[280, 300], [700, 300], [500, 550]]
sign_size = [[230, 160], [232, 129], [204, 235]]

back_button = load("level/back.png")
back_button = transform.scale(back_button, (75, 70))

local_sign = [signs[0], signs[1], signs[2]]
load_button = []
for i in range(4):
    load_button.append(transform.scale(load("aftergame/" + str(i) + ".png"), (80, 80)))

grey = [transform.scale(load("level/grey0.png"), (80, 110)), transform.scale(load("level/grey1.png"), (100, 120)),
        transform.scale(load("level/grey2.png"), (100, 103))]

level_lock = [[True, False, False, False, False, False] for _ in range(3)]
map, level = 0, 0
