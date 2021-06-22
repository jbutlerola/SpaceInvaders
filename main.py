import pygame

# initializes pygame
pygame.init()

# creates screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
  screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
  # screen background color
  screen.fill((40, 40, 40))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
    # if keystroke press, check whether right or left
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        playerX_change -= 0.3
      if event.key == pygame.K_d:
        playerX_change += 0.3
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_a or event.key == pygame.K_d:
        playerX_change = 0
      

  playerX += playerX_change

  if playerX <= 0:
    playerX = 0
  elif playerX >= 736:
    playerX = 736

  player(playerX, playerY)
  pygame.display.update()

