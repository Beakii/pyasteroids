from circle import *

class Asteroid(Circle):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, deltaTime):
        self.position = self.position + (self.velocity * deltaTime)