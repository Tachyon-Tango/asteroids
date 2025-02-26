# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while(True): # Primary game loop
        # Handle quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update entities
        updatable.update(dt)

        for ast in asteroids:
            if(player.check_collision_with(ast)):
                print( "Game over!")
                return

        # Draw background
        screen.fill("black")

        # Draw entities
        for obj in drawable:
            obj.draw(screen)

        # Refreshes the screen
        pygame.display.flip()

        # Increments game time
        dt_ms = clock.tick(60)
        dt = dt_ms/1000


if __name__ == "__main__":
    main()