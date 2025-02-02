import random
import pygame

from .circleshape import CircleShape
from shared.constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)
    
    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        angle_vector_one = self.position.rotate(split_angle)
        angle_vector_two = self.position.rotate(-split_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = angle_vector_one * 1.2

        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = angle_vector_two * 1.2
        
