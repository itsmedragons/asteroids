import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0


    running = True
    while running: # setting an infinite loop to keep the game running
        for event in pygame.event.get(): # checking for events and window closure
            if event.type == pygame.QUIT: 
                running = False

        updateable.update(dt) 

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print ("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
 
        screen.fill("black")  # Fill the screen with black

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Update the display


        dt = clock.tick(60) / 1000.0 # 60 FPS
            

if __name__ == "__main__":
    main()