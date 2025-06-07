import pygame

class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers) # type: ignore
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, deltaTime):
        pass

    def collision(self, target):
        if self.position.distance_to(target.position) <= (self.radius + target.radius):
            return True
        return False