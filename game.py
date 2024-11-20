import pygame
from random import uniform as func
from time import sleep

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)

x, y = WIDTH // 2, HEIGHT // 2
radius = 10

height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10
num = 1.5


def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text = ''.join([chr(int(str(el), 8)) for el in [107, 141, 155, 145, 40, 157, 166, 145, 162]])
    a = Font.render(text, 1, (255, 255, 255))
    win.blit(a, (WIDTH // 2 - 70, HEIGHT // 3))
    pygame.display.update()

def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  # up
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  # left
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  # right
    #pygame.draw.rect(win, white, (0, HEIGHT - bound, WIDTH, bound))  # down

    pygame.draw.rect(win, white, (xp, yp, width, height))
    pygame.draw.circle(win, (0, 255, 0), (x, y), radius)

    pygame.display.update()

run = True

while run:
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    velocity = 8
    vx = velocity * func(-1, 1)
    vy = velocity * func(-1, 1)

    if x + vx < bound + radius or x + vx > WIDTH - bound - radius:
        vx = -vx
    if y + vy < bound + radius:
        vy = -vy

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - width - bound:
        xp += vp

    if xp <= x + vx <= xp + width:
        vx *= num
        vy *= num
        if xp <= x + vx <= xp + width:
            vy = -vy
        else:
            drawScore()
            sleep(10)
            run = False

    x += vx
    y += vy

    drawWindow()

pygame.quit()