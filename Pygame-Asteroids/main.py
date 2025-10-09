import pygame
from constants import * 
from player import Player

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
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        x = SCREEN_WIDTH/2
        y = SCREEN_HEIGHT/2
        player = Player(x, y)
        player.draw(screen)
        pygame.display.flip()         
         
        # Limits the fps till 60
        dt = (start_clock.tick(60))/1000
        

if __name__ == "__main__":
    main()
