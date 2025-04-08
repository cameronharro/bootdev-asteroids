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
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  # describe game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    player.update(dt)
    screen.fill("black")
    player.draw(screen)
    display.flip()

    # limit loop to 60 fps
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()