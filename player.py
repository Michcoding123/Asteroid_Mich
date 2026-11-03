import circleshape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame

class Player(circleshape.CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface, color: str = "white") -> None:
        pygame.draw.polygon(surface = screen, color = color, points = self.triangle(), width = LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        vector = pygame.Vector2(0, 1)
        rot_vector = vector.rotate(self.rotation)
        vel_vec = rot_vector * PLAYER_SPEED
        self.position += vel_vec * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt = -dt)

        if keys[pygame.K_d]:
            self.rotate(dt = dt)

        if keys[pygame.K_w]:
            self.move(dt = dt)

        if keys[pygame.K_s]:
            self.move(dt = -dt)


