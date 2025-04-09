import pygame
from constants import *
from player import (
  Player
)
from asteroid import (
  Asteroid
)
from asteroidfield import (
  AsteroidField
)
from shot import (
  Shot
)

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  # init game and display
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  display = pygame.display
  screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  # define entities and groups
  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updateable, drawable)
  Asteroid.containers = (asteroids, updateable, drawable)
  AsteroidField.containers = (updateable)
  Shot.containers = (shots, drawable, updateable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  AsteroidField()

  # describe game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    updateable.update(dt)
    for asteroid in asteroids:
      if asteroid.overlaps(player):
        print("Game over!")
        return
    screen.fill("black")
    for item in drawable:
      item.draw(screen)
    display.flip()

    # limit loop to 60 fps
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()