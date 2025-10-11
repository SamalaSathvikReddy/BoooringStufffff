import pygame
import sys
from constants import * 
from player import Player
from asteroids import Asteroid
from asteroidfield import *
from circleshape import * 
from shot import *

def main():
    pygame.init()
    print("Starting-Asteroids!")
    """ 
    print(SCREEN_HEIGHT)
    print(SCREEN_WIDTH)
    """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    start_clock = pygame.time.Clock()
    dt = 0
   
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2


    
    # Creating Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()   

    
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    player = Player(x, y)
    asteroid_field = AsteroidField() 
    # Game Loop 
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if player.collides(obj):
                print("Game Over !")
                sys.exit()
            for shot in shots:
                if obj.collides(shot):
                    shot.kill()
                    obj.split()

        
        pygame.display.flip()         
         
        # Limits the fps till 60
        dt = (start_clock.tick(60))/1000
        

if __name__ == "__main__":
    main()
