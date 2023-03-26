import pygame
from pygame.locals import *
import random
import time
pygame.init()
pygame.font.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
score = 0

h = []
for i in range(0,351):
    h.append(i)

# Creating window
screen_width = 320
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
font = pygame.font.Font(None,22)

def textscreen(text,incol,outcol,x,y):
    screentext = font.render(text,True,incol,outcol)
    gameWindow.blit(screentext,[x,y])

def gameover():
    global score
    score
    a = False
    gameWindow.fill((0,0,0))
    textscreen("Game Over Score:"+str(score),white,black,75,50)
    textscreen("Press Enter To Continue",white,black,75,100)
    textscreen("Use Space Bar to play",white,black,75,150)
    pygame.display.update()
    while not a:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score = 0
                    gameloop()

def gameloop():
    
    
    # Game Title
    pygame.display.set_caption("Hopper")
    pygame.display.update()

    # Game specific variables
    hopper_x = 75
    hopper_y = 200
    g = 12
    hopper_size = 20
    fps = 256

    pillar_x = 420
    pillar_y = 0
    pillar_size = 50
    pillar_size_h = random.choice(h)
    pillar_speed = 10


    pillar2_x = 420
    pillar2_y = pillar_size_h + 150
    pillar2_size = 50
    pillar2_size_h = 500
    pillar2_speed = 10

    
    exit_game = False
    while not exit_game:
            
        
        pillar_x -= pillar_speed
        pillar2_x -= pillar2_speed
        hopper_y += g
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hopper_y-=60
                    
        if hopper_y<0 or hopper_y>480:
            gameover()
        
        
        if pillar_x<=0:
            global score
            score+=1
            pillar_size_h = random.choice(h)
            pillar_x = 360
        
        if pillar2_x<=0:
            pillar2_y = pillar_size_h + 150
            pillar2_x = 360

        
        hopper = pygame.Rect(hopper_x,hopper_y,hopper_size,hopper_size)
        pillar = pygame.Rect(pillar_x,pillar_y,pillar_size,pillar_size_h)
        pillar2 = pygame.Rect(pillar2_x,pillar2_y,pillar2_size,pillar2_size_h)
        
        
        
        if hopper.colliderect(pillar) or hopper.colliderect(pillar2) :
            gameover()
        
        gameWindow.fill((0,0,255))

        pygame.draw.rect(gameWindow, (0,255,0), [hopper_x, hopper_y, hopper_size, hopper_size])
        pygame.draw.rect(gameWindow, (255,0,0), [pillar_x, pillar_y, pillar_size, pillar_size_h])
        textscreen("Score:" + str(score),white,black,100,50)
        pygame.draw.rect(gameWindow, (255,0,0), [pillar2_x, pillar2_y, pillar2_size, pillar2_size_h])
        pygame.display.update()
        clock.tick(fps)
        time.sleep(0.07)
        g+=0.01


gameloop()

pygame.quit()
quit()

