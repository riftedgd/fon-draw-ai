import pygame, sys, random

pygame.init()

screen_height, screen_width = 800, 800
screen = pygame.display.set_mode((screen_height, screen_width))
rand_type = random.randint(1, 2)
rand_type_col_similar = random.randint(1, 3) # types of random and col_similar


red = (255, 0, 0) # standard colors
green = (0, 255, 0) 
blue = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()
             
    col = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) # creates random color

    rand_type = random.randint(1, 2)
    rand_type_col_similar = random.randint(1, 3) # types of random and col_similar

    if rand_type_col_similar == 1:
        col_similar = red
    elif rand_type_col_similar == 2: # creates similar colors at random
        col = green
    elif rand_type_col_similar == 3:
        col_similar = blue

    x, y = (random.randint(0, screen_width - 1), random.randint(0, screen_height - 1)) # creates x, y for the pixels
    sim_x, sim_y = (random.randint(100, screen_width - 300), random.randint(100, screen_height - 300)) 


    if rand_type == 1:
        screen.set_at((x, y), col) # creates random col, col_similar
    elif rand_type == 2:
        screen.set_at((x, y), col_similar)
    pygame.display.flip()
