import pygame
from constants import  LINE_WIDTH
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface, color: str = "white") -> None:
        pygame.draw.circle(surface = surface, color = color, center = self.position, radius = self.radius, width = LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += self.velocity * dt
