import pygame
import time
import threading
import random
pygame.init()
screen = pygame.display.set_mode((600, 600))
x= 30
y = 30
oldx = 30
oldy = 30
x2 = 30
y2 = 75
oldx2 = 30
oldy2 = 75
done = False
clock = pygame.time.Clock()
duration1 = 0
duration2 = 0
startTime1 = time.time()
startTime2 = time.time()
partWidth = 280
partHeight = 200
partW = 370
partH = 100

p1 = "player1-removebg-preview (1).png"
p2 = "player2-removebg-preview.png"
surf1 = pygame.image.load(p1).convert_alpha()
surf1small = pygame.transform.smoothscale(surf1, (65,50))
surf2 = pygame.image.load(p2).convert_alpha()
surf2small = pygame.transform.smoothscale(surf2, (55,50))
def resize():
    global partWidth , partHeight
    while True :
        for i in range(50):
            partWidth += 1
            time.sleep(0.01)
        time.sleep(1)
        for i in range(50):
            partWidth -=1
            time.sleep(0.01)
        time.sleep(1)
def move():
    global partW , partH
    while True :
        for i in range(50):
            partH += 1
            time.sleep(0.01)
        time.sleep(1)
        for i in range(50):
            partH -=1
            time.sleep(0.01)
        time.sleep(1)


resize_thread = threading.Thread(target = resize)
resize_thread.start()
resize_thread.deamon = True
moveThread = threading.Thread(target = move)
moveThread.deamon = True
moveThread.start()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 0.5
    if keys[pygame.K_d]:
        x += 0.5
    if keys[pygame.K_w]:
        y -= 0.5
    if keys[pygame.K_s]:
        y += 0.5

    keys2 = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x2 -= 0.5
    if keys[pygame.K_RIGHT]:
        x2 += 0.5
    if keys[pygame.K_UP]:
        y2 -= 0.5
    if keys[pygame.K_DOWN]:
        y2 += 0.5
    screen.fill('lightblue')

    player1 = surf1small.get_rect(topleft=(x, y))
    screen.blit(surf1small, player1)
    player2 = surf2small.get_rect(topleft=(x2, y2))
    screen.blit(surf2small, player2)

    wall1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 600, 20))  # Top wall
    wall2 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 580, 600, 20 )) #Bottom wall
    wall3 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0,20, 600))
    wall4 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(580, 0,20, 600))

    obstacle1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 0, 20, 300)) #k
    obstacle2 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(150, 280, 50, 20)) #o
    obstacle3 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 380, 100, 20)) #o
    obstacle4 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(80, 380, 20, 100)) #k
    obstacle5 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 380, 100, 20))#o
    obstacle6 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(400, 350, 20, 300))#k
    obstacle7 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(400, 350, 100, 20))#o
    obstacle8 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(partW,partH, 20, 230))#k
    obstacle9 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(partWidth,partHeight,200,20))#o
    obstacle10 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(480, 100, 100, 20))#o
    obstacle11 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(240, 330, 20, 180))#k

    font = pygame.font.SysFont("consolas", 50, True, False)
    gametitle = font.render("GOO!", True, (0, 0, 0))
    screen.blit(gametitle, (440, 250))

    font = pygame.font.SysFont("consolas", 15, True, False)
    timer1 = font.render("Time for player1:"+ str(duration1), True, (150, 150, 150))
    screen.blit(timer1, (20, 520))

    font = pygame.font.SysFont("consolas", 15, True, False)
    timer2 = font.render("Time for player2:"+ str(duration2), True, (150, 150, 150))
    screen.blit(timer2, (20, 545))


    walls = [obstacle1,obstacle2,obstacle3,obstacle4,obstacle5,obstacle6,obstacle7,obstacle8,obstacle9,obstacle10,obstacle11]
    for i in walls:
        if player1.colliderect(i):
            x = oldx
            y = oldy


    if player1.colliderect(wall1): y += 5
    elif player1.colliderect(wall2): y -= 5
    elif player1.colliderect(wall3): x += 5
    elif player1.colliderect(wall4): x -= 5


    for i in walls:
        if player2.colliderect(i):
            x2 = oldx2
            y2 = oldy2


    if player2.colliderect(wall1): y2 += 5
    elif player2.colliderect(wall2): y2 -= 5
    elif player2.colliderect(wall3): x2 += 5
    elif player2.colliderect(wall4): x2 -= 5

    finish = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 500, 70, 70))
    pygame.display.flip()


    if player1.colliderect(finish):
        x = oldx
        y = oldy
        endTime1 = time.time()
        duration1 = round(endTime1 - startTime1,2)
    if player2.colliderect(finish):
        x2 = oldx2
        y2 = oldy2
        endTime2 = time.time()
        duration2 = round(endTime2 - startTime2,2)

pygame.quit()