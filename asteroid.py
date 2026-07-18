from typing import override

import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface):
        _ = pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            r_angle = random.uniform(20, 51)
            vec1 = self.velocity.rotate(r_angle)
            vec2 = self.velocity.rotate(-r_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid_pos = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid_neg = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid_pos.velocity = vec1
            asteroid_neg.velocity = vec2
