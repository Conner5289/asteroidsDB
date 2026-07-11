import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    _ = pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        _ = screen.fill("Black")

        _ = pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)
        if event.type == pygame.QUIT:
            return


if __name__ == "__main__":
    main()
