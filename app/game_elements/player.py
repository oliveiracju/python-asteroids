import pygame

from shared.constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from .circleshape import CircleShape
from .shot import Shot

class Player(CircleShape):
    shot_cooldown = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle())
    
    def rotate(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * delta_time
            
        if keys[pygame.K_a]:
           self.rotation -= PLAYER_TURN_SPEED * delta_time
    
    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        
        if self.shot_cooldown > 0:
            self.shot_cooldown -= delta_time

        if keys[pygame.K_w]:
            self.move(delta_time)
            
        if keys[pygame.K_s]:
           self.move(delta_time)

        if keys[pygame.K_SPACE] and self.shot_cooldown <= 0:
            self.shoot()
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN