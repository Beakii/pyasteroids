import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    deltaTime = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Main Game Loop
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                return
            
        screen.fill(color="black")
        time_since_last_call = game_clock.tick(60)
        deltaTime = time_since_last_call/1000

        player.draw(screen)

        pygame.display.flip()



# Ensures program can only be executed by running this file directly, not as an import.
if __name__ == "__main__":
    main()