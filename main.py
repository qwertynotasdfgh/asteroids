import sys

import pygame

from asteroidfield import AsteroidField
from asteroids import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups #
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # containers #
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    AsteroidField()

    # player #
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # clock #
    clock = pygame.time.Clock()
    dt = 0.0

    # loop #
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # game loop start #
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player_1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
