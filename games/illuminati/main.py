import pygame as pygame
import random as rd
pygame.init()


def textscreen(text,incol,outcol,x,y):
    screentext = font.render(text,True,incol,outcol)
    gameWindow.blit(screentext,[x,y])
    
    
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 500
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Heck-By Rudransh")
pygame.display.update()

heck1 = pygame.image.load('.\py program\heck\heckchar.png').convert_alpha()
heck1 = pygame.transform.scale(heck1,(50,50))
tool1 = pygame.image.load('.\py program\heck\htool.png').convert_alpha()
tool1 = pygame.transform.scale(tool1,(50,50))

# Game specific variables
exit_game = False
game_over = False


fps=256
clock = pygame.time.Clock()
font = pygame.font.Font(None,55)
# Game Loop
xchar = 370
ychar = 400

xtool1 = rd.randint(0,450)
ytool1 = 0

while not exit_game:
    
    ytool1+=0.4
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xchar+=25
            if event.key == pygame.K_LEFT:
                xchar-=25
    
    if ytool1>=500:
        ytool1=0
        xtool1 = rd.randint(0,450)
    if xchar<0:
        xchar=450
    if xchar>450:
        xchar=0
    gameWindow.fill(black)
    gameWindow.blit(heck1,[xchar,ychar])
    gameWindow.blit(tool1,[xtool1,ytool1])
    #pygame.draw.rect(gameWindow, black, [pl1_x, pl1_y, pl1_size, pl1_size+100])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
