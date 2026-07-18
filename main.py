import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from shot import Shot


def main() -> None:
    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    _ = asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    _ = player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (updatable, drawable, shots)

    dt = 0.0
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.kill()
                    log_event("asteroid_shot")

        _ = screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        print(dt)
        print(player.position)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
