import pygame
#from database import connect_database, database_version
from constants import *
from circleshape import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    dt = 0
    
    updatable = pygame.sprite.Group()
    
    drawable = pygame.sprite.Group()

    shots = pygame.sprite.Group() 
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000 
        
        updatable.update(dt)

        shots.update(dt)
        
        for asteroid in asteroids:
            asteroid.collision(player)

        screen.fill((0,0,0))
        
        for sprite in drawable:
            sprite.draw(screen)

        for shot in shots:
            shot.draw(screen)    
        
        pygame.display.flip()

                   

    print("Starting Asteroids!" )
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
