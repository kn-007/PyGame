import pygame
import random
from pygame.locals import*
change = [2,4,8]
xchange =  random.choice(change)
ychange =  random.choice(change)
random_coordinate = []
x = 100
y = 300
z = 'Right'
blue = (0, 0, 255)
red = (255, 0, 0)
y_r=y_l=300
left_pad =right_pad=0
bottom_right = 0
bottom_left = 0
pygame.init()
screen = pygame.display.set_mode((600, 600))
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key==K_UP:
                right_pad= -1
            elif event.key ==K_DOWN:
                right_pad=1
            if event.key==K_w:
                left_pad= -1
            elif event.key ==K_s:
                left_pad=1

        elif event.type == KEYUP:
            if event.key==K_UP:
                right_pad=0
            if event.key==K_DOWN:
                right_pad=0
            if event.key==K_w:
                left_pad=0
            if event.key==K_s:
                left_pad=0
            

    
    pygame.display.update()
    screen.fill((0, 0, 0))
    if x == 100:
        xchange = random.choice(change)
    if x == 500:
        xchange = -random.choice(change)
    if y == 500:
        ychange = -random.choice(change)
    if y == 100:
        ychange = random.choice(change)  
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 100)
    x += xchange
    y += ychange
    
    pygame.draw.rect(screen, red,  (0, y_l , 100, 200))
    pygame.draw.rect(screen, red,  (500, y_r, 100, 200))

    y_r+=right_pad
    y_l+=left_pad
    bottom_right = y_r +200
    bottom_left = y_l + 200
    if y_r <=0:
        y_r=0
    if y_r >= 400:
        y_r = 400

    if y_l <=0:
        y_l=0
    if y_l >= 400:
        y_l = 400

    if x == 500 and y_r <= y <= bottom_right :
        print("Collision with right paddel")
        xchange =- xchange
    if x == 100 and y_l <= y <= bottom_left:
        print("Collision with the left paddle")
        xchange =- xchange

--------------------------------------------------------------------------------------------------------------------------------------------------------------
(New Score, Paddle, Etc)

import pygame
import random
import time
from pygame.locals import*
change = [1,3]
xchange =  random.choice(change)
ychange =  random.choice(change)
random_coordinate = []
x = 300
y = 300
z = 'Right'
blue = (0, 0, 255)
red = (255, 0, 0)
y_r=y_l=300
left_pad =right_pad=0
bottom_right = 0
bottom_left = 0
pygame.init()
xchange = random.choice(change)
ychange = random.choice(change)
screen = pygame.display.set_mode((600, 600))
left_score = 0
right_score = 0
def show_text(msg, a, b, color, size):
    fontobj = pygame.font.SysFont("Comic Sans MS", size)
    msobj = fontobj.render(msg, False, color)
    screen.blit(msobj, (a,b))
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key==K_UP:
                right_pad= -1
            elif event.key ==K_DOWN:
                right_pad=1
            if event.key==K_w:
                left_pad= -1
            elif event.key ==K_s:
                left_pad=1

        elif event.type == KEYUP:
            if event.key==K_UP:
                right_pad=0
            if event.key==K_DOWN:
                right_pad=0
            if event.key==K_w:
                left_pad=0
            if event.key==K_s:
                left_pad=0
    left_score = str(left_score)
    right_score = str(right_score)
    show_text("Score:" + left_score, 100, 100, blue, 32)
    show_text("Score:" + right_score, 400, 100, blue, 32)
    pygame.display.update()
    screen.fill((0, 0, 0))
    if x == 102:
        right_score = int(right_score)
        right_score += 1
        time.sleep(1)
        x=300
        y=300
        xchange = random.choice(change)
    if x ==501:
        left_score = int(left_score)
        left_score += 1
        time.sleep(1)
        x=300
        y=300        
        xchange = -random.choice(change)
    if y > 500:
        ychange = -random.choice(change)
    if y < 100:
        ychange = random.choice(change)  
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 100)
    x += xchange
    y += ychange
    
    pygame.draw.rect(screen, red,  (0, y_l , 100, 200))
    pygame.draw.rect(screen, red,  (500, y_r, 100, 200))

    y_r+=right_pad
    y_l+=left_pad
    bottom_right = y_r +200
    bottom_left = y_l + 200
    if y_r <=0:
        y_r=0
    if y_r >= 400:
        y_r = 400

    if y_l <=0:
        y_l=0
    if y_l >= 400:
        y_l = 400

    if x == 402 and y_r <= y <= bottom_right :
        print("Collision with right paddel")
        xchange =- xchange
    if x == 201 and y_l <= y <= bottom_left:
        print("Collision with the left paddle")
        xchange =- xchange
    if left_score == 11:
        screen.fill((0,0,0))
        show_text("Left Wins!", 100,100, blue, 120)
        pygame.display.update()
        break
    if right_score == 11:
        screen.fill((0,0,0))
        show_text("Right Wins!", 100,100, blue, 120)
        pygame.display.update()
        break

----------------------------------------------------
Flappy
import pygame, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000, 600))
yellow = (255, 255, 0)
red = (255, 0, 0 )
ychange = 0
birdx = 500
birdy = 300
pipex =  800
height = 0
bottom_height = 0
pipey= 0
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                ychange = -2
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                ychange = 1      
    pygame.display.update()
    screen.fill((0,0,0))    
    pygame.draw.circle(screen, yellow, (birdx, birdy), 40)
    birdy += ychange
    pygame.draw.rect(screen, red, (pipex, pipey, 80, height))
    pygame.draw.rect(screen, red, (pipex, 0, 80, height))
    pipex -= 1
    if pipex <= 0:
        pipex = 1000
        height = random.randint(50, 500)
----------------------------------------------------------------------------------------------------------------------------
Snow Falling Simulation
import pygame
import random
from pygame.locals import*
random_coordinate = []
pygame.init()
screen = pygame.display.set_mode((600, 600))
for i in range(50):
    a=[random.randint(0,600), random.randint(0,600)]
    random_coordinate.append(a)

while True:
    pygame.display.update()
    screen.fill((0,0,0))
    for r in random_coordinate:
        pygame.draw.circle(screen, (255,255,255), r, 2)
        r[1] += 1
        if r[1] == 600:
            r[1] = 1
            r[0] = random.randint(0,600)

