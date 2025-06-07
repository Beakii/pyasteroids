import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    deltaTime = 0

    group_updateable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()

    Shot.containers = (group_shots, group_drawable, group_updateable) # type: ignore
    Asteroid.containers = (group_asteroids, group_updateable, group_drawable) # type: ignore
    AsteroidField.containers = (group_updateable) # type: ignore
    Player.containers = (group_updateable, group_drawable) # type: ignore

    AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)



# Main Game Loop
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                return
            
        screen.fill(color="black")
        time_since_last_call = game_clock.tick(60)
        deltaTime = time_since_last_call/1000

        for drawable in group_drawable:
            drawable.draw(screen)
        group_updateable.update(deltaTime)

        for asteroid in group_asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        for asteroid in group_asteroids:
            for shot in group_shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.kill()

        pygame.display.flip()



# Ensures program can only be executed by running this file directly, not as an import.
if __name__ == "__main__":
    main()