# Total project has 551 lines


from Atari_Breakout.Atari_Breakout import atari_breakout
from Mario_Space_Invader.Mario import mario
from Flappy_Bird.flappy import flappy
from Tic_Tac_Toe.Tic_Tac_Toe import tic_tac_toe
import Snow_Falling as snow
import pygame
carryOn = True
pygame.init()
font = pygame.font.Font('freesansbold.ttf',70)
j = pygame.font.Font('freesansbold.ttf',17)

screen = pygame.display.set_mode((900,900))
def line():
    pygame.draw.line(screen, (255, 0, 0), (450, 0), (450, 900),10)
    pygame.draw.line(screen, (255, 0, 0), (0,450), (900, 450),10)
def label():
    atari = font.render('Atari', True, (125, 255, 246))
    breakout = font.render('Breakout', True, (125, 255, 246))
    mar_spac = font.render('Mario Space', True, (125, 255, 246))
    invade = font.render('Invader', True, (125, 255, 246))
    flap = font.render('Flappy_Bird', True, (125, 255, 246))
    tic = font.render('Tic_Tac_Toe', True, (125, 255, 246))
    joke = j.render('Click for surprise rip',True,(255,0,0))
    screen.blit(atari,(135,150))
    screen.blit(breakout, (75, 250))
    screen.blit(mar_spac, (460, 150))
    screen.blit(invade, (550, 250))
    screen.blit(flap, (25, 625))
    screen.blit(tic, (490, 625))
    screen.blit(joke,(135,100))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y) = pygame.mouse.get_pos()
            print(x,y)
            if 0 <= x <= 450 and 0 <= y <= 450 and not (130 <= x <= 300 and 100<= y<= 105) :
                atari_breakout()
                screen = pygame.display.set_mode((900, 900))
                screen.fill((0,0,0))
            elif 450 <= x <= 900 and 0 <= y <= 450:
                mario()
                screen = pygame.display.set_mode((900, 900))
                screen.fill((0,0,0))
            elif 0 <= x <= 450 and 450 <= y <= 900:
                flappy()
                screen = pygame.display.set_mode((900, 900))
                screen.fill((0,0,0))
            elif 450 <= x <= 900 and 450 <= y <= 900:
                tic_tac_toe()
                screen = pygame.display.set_mode((900, 900))
                screen.fill((0,0,0))
            elif 130 <= x <= 300 and 100<= y<= 104:
                snow.snow_falling(900,900)
                screen = pygame.display.set_mode((900, 900))
                screen.fill((0,0,0))

    line()
    label()
    pygame.display.update()
