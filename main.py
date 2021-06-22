import pygame
import random
import math

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
  enemyImg.append(pygame.image.load('enemy.png'))
  enemyX.append(random.randint(0, 736))
  enemyY.append(random.randint(50, 150))
  enemyX_change.append(0.4)
  enemyY_change.append(40)

# Bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0.2
bulletY_change = 1
bullet_state = 'ready'   #Ready- cant see bullet on screen, Fire - Bullet is moving

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score(x, y):
  score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
  screen.blit(score, (x, y))
def player(x, y):
  screen.blit(playerImg, (x, y))


def enemy(x, y, i):
  screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
  global bullet_state
  bullet_state = 'fire'
  screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
  distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
  if distance < 27:
    return True
  return False


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
  for i in range(num_of_enemies):

    enemyX[i] += enemyX_change[i]

    if enemyX[i] <= 0:
      enemyX_change[i] = 0.4
      enemyY[i] += enemyY_change[i]
    elif enemyX[i] >= 736:
      enemyX_change[i] = -0.4
      enemyY[i] += enemyY_change[i]

    # Collision
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
      bulletY = 480
      bullet_state = 'ready'
      score_value += 1
      enemyX[i] = random.randint(0, 736)
      enemyY[i] = random.randint(50, 150)

    enemy(enemyX[i], enemyY[i], i)

  # Bullet movement
  if bulletY <= 0:
    bulletY = 480
    bullet_state = 'ready'

  if bullet_state == 'fire':
    fire_bullet(bulletX, bulletY)
    bulletY -= bulletY_change
  

  player(playerX, playerY)
  show_score(textX, textY)
  pygame.display.update()

