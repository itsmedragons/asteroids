import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width:{SCREEN_WIDTH}")
    print(f"Screen height:{SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    running = True
    while running: # setting an infinite loop to keep the game running
        for event in pygame.event.get(): # checking for events and window closure
            if event.type == pygame.QUIT: 
                running = False
           
        screen.fill("black")  # Fill the screen with black
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000.0 # 60 FPS
            

if __name__ == "__main__":
    main()