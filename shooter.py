import math
from math import *
from balls import *


def rotateCentreShooter(x, y, mouse_pos, image):
    run, rise = (mouse_pos[0]-x, mouse_pos[1]-y)
    angle = math.degrees(math.atan2(rise, run))

    rotimage = pygame.transform.rotate(image, -angle - 90)
    rect = rotimage.get_rect(center=(x, y))
    return rotimage, rect, angle


def follow_shooter(center, distance, pos):
    run, rise = (pos[0] - center[0], center[1] - pos[1])
    diff = sqrt(pow(run, 2) + pow(rise, 2))
    x = center[0] + run / diff * distance - 15
    y = center[1] - rise / diff * distance - 15
    return x, y


def ball_angle():
    if pygame.mouse.get_pos()[1] == 450:
        angle = 0
    else:
        angle = atan((pygame.mouse.get_pos()[0] - 500)/(450 - pygame.mouse.get_pos()[1])) * 180 / math.pi
    return angle


def draw_shooter(map, window, front, back):
    if map == 0:
        center = [500, 450]
        shooter = pygame.image.load("shooter 1.png")
        shooter = pygame.transform.scale(shooter, (112, 190))
        img, rect, angle = rotateCentreShooter(center[0], center[1], pygame.mouse.get_pos(), shooter)
        window.blit(front.ball_image, follow_shooter(center, 85, pygame.mouse.get_pos()))
        window.blit(back.ball_image, follow_shooter(center, -35, pygame.mouse.get_pos()))
        window.blit(img, rect)
