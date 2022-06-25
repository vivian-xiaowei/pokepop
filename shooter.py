import math
from math import *
from balls import *
from pygame import transform


def rotate_shooter(window, x, y, mouse_pos, image):  # function to rotate the shooter
    run, rise = (mouse_pos[0] - x, mouse_pos[1] - y)  # get the run and rise to calculate slope
    angle = math.degrees(math.atan2(rise, run))  # the angle is inverse tan of rise over run

    rotimage = transform.rotate(image, -angle - 90)  # rotate the image by the angle calculated
    rect = rotimage.get_rect(center=(x, y))  # find the centre of the image
    window.blit(rotimage, rect)  # blit the newly rotated image to the screen


def follow_shooter(window, ball, center, distance):  # function so the next ball follows the shooter
    mx, my = pygame.mouse.get_pos()  # get the mouse position
    run, rise = mx - center[0], center[1] - my  # find the run and rise using the centre of the shooter and the mouse
    diff = sqrt(pow(run, 2) + pow(rise, 2))  # calculate the difference between the points
    x, y = center  # set the centre to x and y
    if diff != 0:  # if the difference isn't 0
        x = center[0] + run * distance / diff - ball.rect.width / 2  # calculate x and y (position of the ball)
        y = center[1] - rise * distance / diff - ball.rect.height / 2
    ball.pos = x, y  # set the ball position to x and y
    if rise > 0:  # if the rise is above 0
        # set the ball angle to the negative arc tan of the run over the rise multiplied by 180 divided by pi
        ball.angle = -atan(
            (pygame.mouse.get_pos()[0] - center[0]) / (center[1] - pygame.mouse.get_pos()[1])) * 180 / math.pi
    elif rise < 0:  # if the rise is below 0
        # set the ball angle to the negative arc tan of the run over the rise multiplied by 180 divided by pi plus 180
        ball.angle = -atan(
            (pygame.mouse.get_pos()[0] - center[0]) / (center[1] - pygame.mouse.get_pos()[1])) * 180 / math.pi + 180
    elif run < 0:  # if the rise is 0 and the run is negative
        ball.angle = 90  # set the ball's angle to 90
    else:  # if the rise is 0 and the run is positive or 0
        ball.angle = 270  # set the ball's angle to 270
    ball.draw(window)  # draw the ball


def draw_shooter(map, window, front, back, pos, speed):  # function to draw the shooter
    if map == 0:  # if the map is 0
        size = 112, 190  # set the shooter size and distance (for the middle ball) accordingly
        distance = 85, -34.8
    elif map == 1:  # if the map is 1
        size = 140, 190  # set the shooter size and distance (for the middle ball) accordingly
        distance = 100, -30
    else:  # if the map is 2
        size = 160, 150  # set the shooter size and distance (for the middle ball) accordingly
        distance = 80, -25
    shooter = pygame.image.load("shooter " + str(map + 1) + ".png")  # set the shooter image accordingly
    shooter = transform.scale(shooter, size)
    if int(speed) == 1:  # if the speed is 1
        follow_shooter(window, front, pos, distance[0])  # blit the next ball image accordingly
    rotate_shooter(window, pos[0], pos[1], pygame.mouse.get_pos(), shooter)  # rotate the shooter accordingly
    if int(speed) == 1:  # if the speed is 1
        follow_shooter(window, back, pos, distance[1])  # blit the next ball image accordingly
