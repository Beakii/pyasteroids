from circle import *
from constants import *
import sys

from shot import Shot

class Player(Circle):    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cool_down = 0

    def shoot(self):
        if self.shoot_cool_down <= 0:
            self.shoot_cool_down = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS) # type: ignore
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # type: ignore

    def rotate(self, deltaTime, direction):
        self.rotation += direction * (PLAYER_TURN_SPEED * deltaTime)
    
    def move(self, deltaTime, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * forward * PLAYER_SPEED * deltaTime

    def update(self, deltaTime):
        self.shoot_cool_down -= deltaTime
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(deltaTime, -1)
        if keys[pygame.K_d]:
            self.rotate(deltaTime, 1)
        if keys[pygame.K_w]:
            self.move(deltaTime, 1)
        if keys[pygame.K_s]:
            self.move(deltaTime, -1)

        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if keys[pygame.K_ESCAPE]:
            sys.exit()