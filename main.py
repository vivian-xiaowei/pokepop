import pygame.sprite

from lines import *
from balls import *


def main():
    # spiral variable
    x_s, y_s, a = spiral()
    # straight line rotate variable
    ball_list = []
    pic = pygame.sprite.Sprite()
    pic.rect = Rect((600, 160), (22, 22))
    pic.image = pygame.image.load("balls/00.png")
    for i in range(10):
        ball_list.append(pokeballs(1, 700 - i * 22, 100, 1))
    for i in range(5):
        ball_list.append(pokeballs(4, 700 - 220 - i * 22, 100, 1))

    while True:  # main game loop
        clock.tick(60)
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        # draw the spiral lines
        spiral_lines, slope = draw_spiral(x_s, y_s)
        # window.blit(pic.image, pic.rect.center)
        # for i in range(len(spiral_lines)):
        #     if pic.rect.colliderect(spiral_lines[i]):
        #         x, y = pic.rect.center
        #         # print(slope[i][0], slope[i][1])
        #         x += slope[i][0]
        #         y += slope[i][1]
        #         print(x, y)
        #         pic.rect.center = x, y

        # change the ball position base on the collision with straight lines
        for count in range(len(ball_list)):
            ball = ball_list[count]
            ball.rect.center = ball.pos
            # follow_lines(ball)
            follow_spiral(ball, slope)
            ball.draw(window)

        pygame.display.update()

def map2():
    # straight line angle variable
    ball_list = []
    for i in range(5):
        ball_list.append(pokeballs(0, 600 + i * 22, 100))

    while True:  # main game loop
        clock.tick(60)
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        # change the ball position base on the collision with straight lines
        for ball in ball_list:
            ball.rect.center = ball.pos
            map2_follow_lines(ball)
            ball.draw(window)

        pygame.display.update()


if __name__ == "__main__":
    # map = input()
    # if map == "lines":
    #     main()
    # else:
    #     map2()
    map2()
    # main()
