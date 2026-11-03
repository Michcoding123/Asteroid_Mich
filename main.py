import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()    
    Player.containers = (updatable, drawable)
    play3r = Player(x = SCREEN_WIDTH/2, y =  SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60)/1000

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        updatable.update(dt)
        
        asteroids_list = list(asteroids)
        for i in range(len(asteroids_list)):
            for j in range(i + 1, len(asteroids_list)):
                if asteroids_list[i].collides_with(asteroids_list[j]):
                    asteroids_list[i].bounce_off(asteroids_list[j])
            if asteroids_list[i].collides_with(play3r):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroids_list[i].collides_with(shot):
                    log_event("asteroid_shot")
                    asteroids_list[i].split()
                    shot.kill()

if __name__ == "__main__":
    main()
