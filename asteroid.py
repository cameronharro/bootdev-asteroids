import pygame
import random
from circleshape import CircleShape
from constants import (
  ASTEROID_MIN_RADIUS
)

class Asteroid(CircleShape):
  def __init__(self, x, y, radius, velocity):
    super().__init__(x, y, radius)
    self.velocity = velocity
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      x = self.position.x
      y = self.position.y
      split_angle = random.uniform(20, 50)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      Asteroid(x, y, new_radius, self.velocity.rotate(split_angle) * 1.2)
      Asteroid(x, y, new_radius, self.velocity.rotate(-1 * split_angle) * 1.2)