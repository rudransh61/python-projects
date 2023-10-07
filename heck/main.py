import pygame
import random as rd
import os as os
pygame.init()


def textscreen(text,incol,outcol,x,y):
    screentext = font.render(text,True,incol,outcol)
    gameWindow.blit(screentext,[x,y])


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue=(0,0,255)

# Creating window
screen_width = 500
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Heck-By Rudransh")
pygame.display.update()

heck1 = pygame.image.load('.\heckchar.png').convert_alpha()
heck1 = pygame.transform.scale(heck1,(50,50))
security = pygame.image.load('.\htool.png').convert_alpha()
security = pygame.transform.scale(security,(50,50))
firewall= pygame.image.load('.\hfirewall.png')
firewall= pygame.transform.scale(firewall,(50,50))

score=0
lives=5
hiscore=0

fps=256

clock = pygame.time.Clock()
font = pygame.font.Font(None,35)

def gameover():


    exit_game2=False
    while not exit_game2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
            
        gameWindow.fill(black)
        textscreen("Score:"+str(score),blue,black,200,100)
       # textscreen("High Score:"+str(hiscore),blue,black,200,200)
        textscreen("Press enter key to continue",blue,black,100,300)
        pygame.display.update()

# Game specific variables

def gameloop():
    global lives
    global score
    global hiscore
    global xchar,ychar,xfire,yfire,xsecurity,ysecurity,g
    
    exit_game = False
    # Game Loop
    xchar = 370
    ychar = 400



    xfire = rd.randint(0,450)
    yfire = 0

    xsecurity = rd.randint(0,450)
    ysecurity = 0
    
    lives=5
    score=0
    
    g=0.4

    while not exit_game:
        
        ysecurity+=g
        yfire+=g
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xchar+=25
                if event.key == pygame.K_LEFT:
                    xchar-=25
        
        if ysecurity>=420:
            ysecurity=0
            xsecurity = rd.randint(0,450)
        if yfire>=420:
            yfire=0
            xfire = rd.randint(0,450)
        if xchar<0:
            xchar=450
        if xchar>450:
            xchar=0
            
            
        if abs(xsecurity-xfire)<=100:
            ysecurity=0
            xsecurity=rd.randint(0,450)

        
        if abs(xchar-xsecurity)<=40 and abs(ychar-ysecurity)<=40 :
            score+=1
            xsecurity=rd.randint(0,450)
            ysecurity=0
            
            
        if abs(xchar-xfire)<=50 and abs(ychar-yfire)<=50 :
            if score>=1:
                score-=1
            lives-=1
            xfire=rd.randint(0,450)
            yfire=0
        
        if lives<=0:
            gameover()
        
        # if score>hiscore:
        #     hiscore=score
        
        hiscore
        
        gameWindow.fill(black)
        gameWindow.blit(heck1,[xchar,ychar])
        gameWindow.blit(security,[xsecurity,ysecurity])
        gameWindow.blit(firewall,[xfire,yfire])
        textscreen("Score:"+str(score),blue,black,150,100)
        textscreen("Lives:"+str(lives),blue,black,300,100)
        #pygame.draw.rect(gameWindow, black, [pl1_x, pl1_y, pl1_size, pl1_size+100])
        pygame.display.update()
        clock.tick(fps)
        g+=0.0001

gameloop()

pygame.quit()
quit()

