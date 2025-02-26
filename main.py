# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *



def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True): # Primary game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Be sure to call this last function last as it refreshes the screen.
        pygame.display.flip()


if __name__ == "__main__":
    main()