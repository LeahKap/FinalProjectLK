import pygame, sys
from pygame.locals import *

wood= (200,250,50)
boardwidth= 3
boardheight= 3
spacesize=50
windowwidth = 700 
windowheight = 500 
xmargin = int((windowwidth - boardwidth * spacesize) / 2)
ymargin = int((windowheight - boardheight * spacesize) / 2)
colorboardrings= (0,0,240)
blue=(0,240,0)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((windowwidth, windowheight))
DISPLAYSURF.fill(wood)

#circles on board
#first row
pygame.draw.circle(DISPLAYSURF, colorboardrings, (215, 90), 50, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (215, 90), 30, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (215, 90), 6, 0)

pygame.draw.circle(DISPLAYSURF, colorboardrings, (345, 90), 50, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (345, 90), 30, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (345, 90), 6, 0)

pygame.draw.circle(DISPLAYSURF, colorboardrings, (475, 90), 50, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (475, 90), 30, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (475, 90), 6, 0)

#second row
pygame.draw.circle(DISPLAYSURF, colorboardrings, (215, 220), 50, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (215, 220), 30, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (215, 220), 6, 0)

pygame.draw.circle(DISPLAYSURF, colorboardrings, (345, 220), 50, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (345, 220), 30, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (345, 220), 6, 0)

pygame.draw.circle(DISPLAYSURF, colorboardrings, (475, 220), 50, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (475, 220), 30, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (475, 220), 6, 0)

#third row
pygame.draw.circle(DISPLAYSURF, colorboardrings, (215, 350), 50, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (215, 350), 30, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (215, 350), 6, 0)

pygame.draw.circle(DISPLAYSURF, colorboardrings, (345, 350), 50, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (345, 350), 30, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (345, 350), 6, 0)

pygame.draw.circle(DISPLAYSURF, colorboardrings, (475, 350), 50, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (475, 350), 30, 8)
pygame.draw.circle(DISPLAYSURF, colorboardrings, (475, 350), 6, 0)

pygame.font.init()  
my_font = pygame.font.SysFont('Arial Bold', 30)

text_surface1 = my_font.render('Player 1', False, (0, 0, 0))
DISPLAYSURF.blit(text_surface1, (50,15))
text_surface2 = my_font.render('Player 2', False, (0, 0, 0))
DISPLAYSURF.blit(text_surface2, (565,15))

 

pygame.display.set_caption('Otrio')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


def rings():
    player1big
    player1med
    player1small
    player2big
    player2med
    player2small
