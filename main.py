import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
        player_1.update(dt)
        screen.fill("black")
        player_1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
