from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

class Player(CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shoot_timer = 0

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

    def shoot(self) -> None:
        if self.shoot_timer > 0:
            return
        else:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        position = self.position
        shot = Shot(position.x, position.y)
        ini_vec = pygame.Vector2(0, 1)
        rot_vec = ini_vec.rotate(self.rotation)
        shot.velocity = rot_vec * PLAYER_SHOOT_SPEED

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
        
        self.shoot_timer -= dt

        if keys[pygame.K_SPACE]:
            self.shoot()


