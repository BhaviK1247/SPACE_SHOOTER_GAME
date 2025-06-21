import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Super Mario")
icon = pygame.image.load('sup.png')
pygame.display.set_icon(icon)

back_image = pygame.image.load('space.jpg')
ufo = pygame.image.load('ufo.png')
ufo_x = 350
ufo_y = 450
ufo_change = 0

enemy_image = pygame.image.load('monster.png')
e_x = random.randint(0, 800)
e_y = random.randint(50, 150)
e_change = 0.2

bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 450
bullet_change_x = 0
bullet_change_y = 0.5
bullet_state = 'ready'

score = 0
font = pygame.font.Font(None, 36)

def player(x, y):
    screen.blit(ufo, (x, y))

def enemy(x, y):
    screen.blit(enemy_image, (x, y))

def bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(ex, ey, bx, by):
    distance = ((ex - bx) ** 2 + (ey - by) ** 2) ** 0.5
    if distance < 27:
        return True
    return False

run = True
while run:
    screen.blit(back_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ufo_change = -0.2
            elif event.key == pygame.K_RIGHT:
                ufo_change = 0.2
            elif event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_x = ufo_x
                    bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ufo_change = 0

    ufo_x = ufo_x + ufo_change

    if ufo_x <= 0:
        ufo_x = 0
    elif ufo_x >= 736:
        ufo_x = 736

    e_x += e_change
    if e_x <= 0 or e_x >= 736:
        e_change *= -1
        e_y += 20

    if bullet_state == 'fire':
        bullet(bullet_x, bullet_y)
        bullet_y -= bullet_change_y
        if bullet_y <= 0:
            bullet_y = 450
            bullet_state = 'ready'

    collision = is_collision(e_x, e_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 450
        bullet_state = 'ready'
        score += 1
        e_x = random.randint(0, 800)
        e_y = random.randint(50, 150)

    player(ufo_x, ufo_y)
    enemy(e_x, e_y)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
