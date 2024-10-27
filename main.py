import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!") 
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    dt = 0

    #set up groups
    updatable = pygame.sprite.Group()
    renderable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()



    Player.containers = updatable, renderable
    Asteroid.containers = updatable, renderable, asteroids
    AsteroidField.containers = updatable
    Shot.containers = updatable, renderable, shots


    field = AsteroidField() 
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                exit()
                return
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    break
        
        for sprite in renderable:
            sprite.draw(screen)
        pygame.display.flip()
        # time in seconds since last tick
        dt = clock.tick(60)/1000 
    

if __name__ == "__main__":
    main()