import pygame
from constants import *
from player import Player

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  display = pygame.display
  screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updateable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  # describe game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    updateable.update(dt)
    screen.fill("black")
    for item in drawable:
      item.draw(screen)
    display.flip()

    # limit loop to 60 fps
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()