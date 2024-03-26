import pygame, sys, random

pygame.init()

screen_height, screen_width = 800, 800
screen = pygame.display.set_mode((screen_height, screen_width))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()

    col = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    x, y = (random.randint(0, screen_width - 1), random.randint(0, screen_height - 1))

    screen.set_at((x, y), col)
    pygame.display.flip()
