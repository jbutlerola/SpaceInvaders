import pygame
import random
# initializes pygame
pygame.init()

# creates screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.png")

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 40

# Bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0.2
bulletY_change = 1
bullet_state = 'ready'   #Ready- cant see bullet on screen, Fire - Bullet is moving

def player(x, y):
  screen.blit(playerImg, (x, y))

def enemy(x, y):
  screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
  global bullet_state
  bullet_state = 'fire'
  screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop
running = True
while running:
  # screen background color
  screen.fill((40, 40, 40))
  # background image
  screen.blit(background, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
    # if keystroke press, check whether right or left
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        playerX_change -= 0.3
      if event.key == pygame.K_d:
        playerX_change += 0.3
      if event.key == pygame.K_SPACE:
        if bullet_state is 'ready':
          # gets current x coordinate of player 
          bulletX = playerX
          fire_bullet(bulletX, bulletY)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_a or event.key == pygame.K_d:
        playerX_change = 0
    
  # checking for boundries of spaceship
  playerX += playerX_change

  if playerX <= 0:
    playerX = 0
  elif playerX >= 736:
    playerX = 736

  # enemy movement
  enemyX += enemyX_change

  if enemyX <= 0:
    enemyX_change = 0.2
    enemyY += enemyY_change
  elif enemyX >= 736:
    enemyX_change = -0.2
    enemyY += enemyY_change

  # Bullet movement
  if bulletY <= 0:
    bulletY = 480
    bullet_state = 'ready'

  if bullet_state == 'fire':
    fire_bullet(bulletX, bulletY)
    bulletY -= bulletY_change
  
  player(playerX, playerY)
  enemy(enemyX, enemyY)
  pygame.display.update()

