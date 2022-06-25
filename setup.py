import pygame
from pygame import *
from pygame.image import load

pygame.init()  # initialize pygame
mixer.init()  # initialize mixer
clock = time.Clock()  # track time using clock

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

# add the animation frames of the level buttons to the lists
for i in range(1, 5):
    map1_animation.append(transform.scale(load("level/leaf" + str(i) + ".png"), (80, 110)))
    map2_animation.append(transform.scale(load("level/cactus" + str(i) + ".png"), (100, 120)))
for i in range(1, 9):
    map3_animation.append(transform.scale(load("level/cube" + str(i) + ".png"), (100, 103)))

# store all the level animations under the list animations
animations = [map1_animation, map2_animation, map3_animation]

# initialize colours and store colours in an array
red = 255, 0, 0
blue = 0, 0, 255
black = 0, 0, 0
colours = [red, blue, black]

# set index to 0
index = 0
# set image to the first animation on the first map
image = map1_animation[0]

numbers = []  # initialize a list for level numbers
for i in range(1, 7):  # store the level number images in the list
    numbers.append(transform.scale(load("level/Level " + str(i) + ".png"), (25, 50)))  # add the number to the list

signs = []  # initialize a list for the map select signs
for i in range(1, 4):  # loop through the maps
    signs.append(load("choose maps/" + str(i) + ".png"))  # add the sign to the list

# set all the sign positions, sizes, and set the local_sign list to all the default sized signs
sign_pos = [[280, 300], [700, 300], [500, 550]]
sign_size = [[230, 160], [232, 129], [204, 235]]
local_sign = [signs[0], signs[1], signs[2]]

# set the back button image
back_button = load("level/back.png")
back_button = transform.scale(back_button, (75, 70))

# store all the "loading" buttons (replay button, pause button, etc.) inside a list
load_button = []
for i in range(6):
    load_button.append(transform.scale(load("button/" + str(i) + ".png"), (80, 80)))

# store unlocked level button images in a list
grey = [transform.scale(load("level/grey0.png"), (80, 110)), transform.scale(load("level/grey1.png"), (100, 120)),
        transform.scale(load("level/grey2.png"), (100, 103))]

# reset the level lock (true means the level is unlocked, false means it's locked)
level_lock = [[True, False, False, False, False, False] for _ in range(3)]
map, level = 0, 0  # reset the map and level
