from circle import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
import sys

class Player(Circle):    
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
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, deltaTime, direction):
        self.rotation += direction * (PLAYER_TURN_SPEED * deltaTime)
    
    def move(self, deltaTime, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * forward * PLAYER_SPEED * deltaTime

    def update(self, deltaTime):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(deltaTime, -1)
        if keys[pygame.K_d]:
            self.rotate(deltaTime, 1)
        if keys[pygame.K_w]:
            self.move(deltaTime, 1)
        if keys[pygame.K_s]:
            self.move(deltaTime, -1)
        
        if keys[pygame.K_ESCAPE]:
            sys.exit()