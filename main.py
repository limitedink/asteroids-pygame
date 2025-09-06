import sys
import pygame
from constants import *
from player import *
from asteroidfield import *
from circleshape import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    playing = True
    
    drawables = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (updatable, drawables)
    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawables)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill("black")
        
        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        for asteroid in asteroids:
            if player.colliding(asteroid):
                print("Game over!")
                sys.exit()


if __name__ == "__main__":
    main()
