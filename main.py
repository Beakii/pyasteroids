import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                return
            
        screen.fill(color="black")
        pygame.display.flip()
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


# Ensures program can only be executed by running this file directly, not as an import.
if __name__ == "__main__":
    main()