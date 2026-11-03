import pygame
import random
from constants import  *
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface, color: str = "white") -> None:
        pygame.draw.circle(surface = surface, color = color, center = self.position, radius = self.radius, width = LINE_WIDTH)
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vec_a1 = self.velocity.rotate(angle)
            vec_a2 = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)

            a1.velocity = 1.2 * vec_a1
            a2.velocity = 1.2 * vec_a2
    
    def bounce_off(self, other):
        # Vector pointing from the other asteroid to this asteroid
        collision_normal = self.position - other.position
        
        # Guard against zero-division if centers overlap perfectly
        if collision_normal.length_squared() == 0:
            return

        normal = collision_normal.normalize()

        ratio = self.radius/other.radius

        # Reflect self's velocity along the collision normal
        self.velocity = (1/ratio) * self.velocity.reflect(normal)

        # Reflect other's velocity along the opposite normal
        other.velocity = ratio * other.velocity.reflect(-normal)

        # Separate them slightly so they don't stay overlapping
        overlap = (self.radius + other.radius) - collision_normal.length()
        if overlap > 0:
            self.position += normal * (overlap / 2)
            other.position -= normal * (overlap / 2)

    def update(self, dt) -> None:
        self.position += self.velocity * dt
