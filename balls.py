import pygame
from random import *

# load all ball images
ball_images = [[] for i in range(7)]
for i in range(7):
    for j in range(8):
        image = pygame.image.load("balls/" + str(i) + str(j) + ".png")
        ball_images[i].append(pygame.transform.scale(image, (30, 30)))

balls_exist = set()


# randomly generate the two balls on the shooter and the balls exist in main list
# previous for shooter checking if still exist, repeat for wanting ball in or not in ball_exist
def pick_ball(previous=-1, repeat=True):
    # for shooter, if the ball type still in balls_exist, don't change
    if previous != -1 and (previous in balls_exist or len(balls_exist) == 0):
        return previous
    # pick a ball until match the condition
    while len(balls_exist) != 0:
        rand = randint(0, 6)
        if (rand in balls_exist) == repeat or len(balls_exist) == 7:
            return rand
    return previous

# spawn the balls according to the level and map
def generate_ball(level, map=0):
    ball = []
    position = 0
    type = randint(0, 6)  # first ball type
    # more balls in higher levels
    while position <= 40 + 3 * level:
        balls_exist.add(type)
        # more scattered colour in higher levels
        for j in range(randint(1, 8 - level)):
            # different spawning position for map 3
            if map == 2:
                ball.append(pokeballs(type, 120 - position * 30, 110, 0, 3))
            else:
                ball.append(pokeballs(type, 120 - position * 30, 100, 0, 3))
            position += 1
        type = pick_ball(-1, False)  # pick another ball colour
    return ball


# pokeball class with the ball_image, position, rotate of angle and rect for collision
class pokeballs:
    def __init__(self, ball_type, x_pos=-30, y_pos=-30, rotate=randint(0, 2), x_move=3, y_move=0):
        self.type = ball_type
        self.rotate = rotate  # the rotation of the ball
        self.ball_image = ball_images[self.type][int(self.rotate)]  # the image to display
        self.rect = self.ball_image.get_rect()  # rect for collision
        self.angle = 0  # the angle of the image
        self.pos = [x_pos, y_pos]  # the position
        self.rect.topleft = self.pos
        self.road_h, self.road_v = 0, 0  # the road it is on
        self.speed = abs(x_move)  # the set speed
        self.x_move = x_move  # how much to move horizontally
        self.y_move = y_move  # how much to move vertically
        self.move = True  # whether the ball is moving

    # loop through the images
    def roll(self, speed):
        self.rotate += speed
        if int(self.rotate) >= 8:
            self.rotate = 0
        self.ball_image = ball_images[self.type][int(self.rotate)]

    # change the position according to x_move and y_move and rotate them to roll forward on the path
    def shooter_move(self, angle=False):
        x, y = self.pos
        self.pos = [x + self.x_move, y + self.y_move]
        if angle:
            if self.x_move > 0:
                self.angle = 90
            elif self.x_move < 0:
                self.angle = 270
            elif self.y_move > 0:
                self.angle = 0
            elif self.y_move < 0:
                self.angle = 180
            self.roll(self.speed / 7)

    # draw the ball
    def draw(self, window):
        self.ball_image = pygame.transform.rotate(ball_images[self.type][int(self.rotate)], self.angle)
        self.rect = self.ball_image.get_rect()
        window.blit(self.ball_image, self.pos)
