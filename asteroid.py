import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius < ASTEROID_MIN_RADIUS):
            return
        rand_ang = random.uniform(20, 50)
        new_velocity_a = self.velocity.rotate(rand_ang)
        new_velocity_b = self.velocity.rotate(-1 * rand_ang)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_a.velocity = new_velocity_a * 1.2
        new_asteroid_b.velocity = new_velocity_b * 1.2
        