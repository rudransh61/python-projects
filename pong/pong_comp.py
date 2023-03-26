import pygame
from pygame.locals import *
import random
import time
pygame.init()
pygame.font.init()

def textscreen(text,incol,outcol,x,y):
    screentext = font.render(text,True,incol,outcol)
    gameWindow.blit(screentext,[x,y])
    
    
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


mul = [-1,1]
# Creating window
screen_width = 800
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("PongByRudransh")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
pl1_x = 0
pl1_y = 55
pl1_size = 10

score1 = 0
score2 = 0

pl2_x = 790
pl2_y = 55
pl2_size = 10
fps = 30
ball_x,ball_y = 400,250
ball_size = 20

x_vel = 5*rd.choice(mul)
y_vel = 5*rd.choice(mul)

clock = pygame.time.Clock()
font = pygame.font.Font(None,55)
# Game Loop
while not exit_game:
    
    
    pl1 = pygame.Rect(pl1_x,pl1_y,pl1_size,pl1_size+100)
    pl2 = pygame.Rect(pl2_x,pl2_y,pl2_size,pl2_size+100)
    ball = pygame.Rect(ball_x,ball_y,ball_size,ball_size)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pl1_y = pl1_y - 30
            if event.key == pygame.K_DOWN:
                pl1_y = pl1_y + 30
            if event.key == pygame.K_c:
                score1+=1
            if event.key == pygame.K_h:
                score2+=1

    ball_x += x_vel
    ball_y += y_vel
    
    pl2_y=ball_y-55

    if pl1.colliderect(ball):
        x_vel*=-1.002
        score1 +=1
    if pl2.colliderect(ball):
        x_vel*=-1.002
        score2 +=1

    
    if pl1_y<0 :
        pl1_y=0
    if pl1_y>390 :
        pl1_y=390
    if pl2_y<0 :
        pl2_y=0
    if pl2_y>390 :
        pl2_y=390
        
    if ball_y>=490 or ball_y<=10:
        y_vel*=-1
    if ball_x>=790 or ball_x<=0:
        x_vel*=-1
        
    
    if pl1.colliderect(ball):
        global i
        i=1
        x_vel*=-1
        score1 +=i
        i=0
        
    if pl2.colliderect(ball):
        global j
        j=1
        x_vel*=-1
        score2 +=j
        j=0

    
    
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [pl1_x, pl1_y, pl1_size, pl1_size+100])
    pygame.draw.rect(gameWindow, black, [pl2_x, pl2_y, pl2_size, pl2_size+100])
    pygame.draw.rect(gameWindow, black, [ball_x, ball_y, ball_size, ball_size])
    pygame.draw.line(gameWindow,(0,0,0) ,(400, -100), (400, 600))
    textscreen("Score:"+str(score1) ,(0,0,0),(255,255,255),200,50)
    textscreen("Score:"+str(score2) ,(0,0,0),(255,255,255),600,50)
    pygame.display.update()
    clock.tick(fps)



