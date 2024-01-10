import pygame as pg
from pygame.locals import *
import random as rd
import time
import os as os
pg.init()
pg.font.init()
clock = pg.time.Clock()
    
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
yellow = (255,165,0)
red=(255,0,0)


car = pg.image.load('.\car.png')
car = pg.transform.scale(car,(40,40))
font = pg.font.Font('freesansbold.ttf', 32)

width = 1000
height = 480
window = pg.display.set_mode((width,height))
pg.display.set_caption ("CrossyRoad")

def gameloop():
    
    window.fill(black)
    
    
    gameover = False
    
    width = 1000
    height = 480
    xcor = 500
    ycor = 450

    xecor1 =  rd.randint(0,1000)
    xecor2 =  rd.randint(0,1000)
    xecor3 =  rd.randint(0,1000)
    xecor4 =  rd.randint(0,1000)
    xecor5 =  rd.randint(0,1000)
    xecor6 =  rd.randint(0,1000)
    xecor7 =  rd.randint(0,1000)
    xecor8 =  rd.randint(0,1000)
    xecor9 =  rd.randint(0,1000)
    xecor10 =  rd.randint(0,1000)
    yecor = 65
    yecor1 = 90
    yecor2 = 125
    yecor3 = 160
    yecor4 = 195
    yecor5 = 230
    yecor6 = 265
    yecor7 = 300
    yecor8 = 335
    yecor9 = 370
    yecor10 = 405


    
    while not gameover :
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = True
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_RIGHT :
                    xcor += 10
                if event.key == pg.K_LEFT :
                    xcor -= 10
                if event.key == pg.K_UP :
                    ycor -= 10
                if event.key == pg.K_DOWN :
                    ycor += 10
        window.fill(black)
        pg.draw.rect(window,red,[-xcor,80,10000,2]) #Finish
        pg.draw.rect(window,green,[-xcor,440,10000,2]) #Start
        pg.draw.rect(window,yellow,[xcor,ycor,20,20])
        
        #cars
        # pg.draw.rect(window,green,[xecor1,yecor1,20,20])
        # pg.draw.rect(window,green,[xecor2,yecor2,20,20])
        # pg.draw.rect(window,green,[xecor3,yecor3,20,20])
        # pg.draw.rect(window,green,[xecor4,yecor4,20,20])
        # pg.draw.rect(window,green,[xecor5,yecor5,20,20])
        # pg.draw.rect(window,green,[xecor6,yecor6,20,20])
        # pg.draw.rect(window,green,[xecor7,yecor7,20,20])
        # pg.draw.rect(window,green,[xecor8,yecor8,20,20])
        # pg.draw.rect(window,green,[xecor9,yecor9,20,20])
        # pg.draw.rect(window,green,[xecor10,yecor10,20,20])
        
        window.blit(car,[xecor1,yecor1])
        window.blit(car,[xecor2,yecor2])
        window.blit(car,[xecor3,yecor3])
        window.blit(car,[xecor4,yecor4])
        window.blit(car,[xecor5,yecor5])
        window.blit(car,[xecor6,yecor6])
        window.blit(car,[xecor7,yecor7])
        window.blit(car,[xecor8,yecor8])
        window.blit(car,[xecor9,yecor9])
        window.blit(car,[xecor10,yecor10])
        ##################################################

        pg.time.Clock()

        pg.display.update()
        
        xecor1 += 0.09
        xecor2 += 0.09
        xecor3 += 0.09
        xecor4 += 0.09
        xecor5 += 0.09
        xecor6 += 0.09
        xecor7 += 0.09
        xecor8 += 0.09
        xecor9 += 0.09
        xecor10 +=0.09
        
        if xcor>980 :
            xcor = 980
        if xcor<0 :
            xcor = 0
        
        if ycor<80 :
            window.fill(green)
            gameor = True
            while gameor:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        exit()
                text_screen("Yeah !! (game finished)",green,black,150,200)
                pg.display.update()
            
        if xecor1>900 :
            xecor1 = 20
        
        if xecor2>900 :
            xecor2 = 20
            
        if xecor3>900 :
            xecor3 = 20 
        if xecor4>900 :
            xecor4 = 20 
        if xecor5>900 :
            xecor5 = 20
            
        if xecor6>900 :
            xecor6 = 20
        if xecor7>900 :
            xecor7 = 20
            
        if xecor8>900 :
            xecor8 = 20 
        if xecor9>900 :
            xecor9 = 20 
        if xecor10>900 :
            xecor10 = 20
            
            
            
            
            
            #################################################
        if abs(xcor-xecor1)<40 and abs(ycor-yecor1)<40 :
            gameover = True
        if abs(xcor-xecor2)<40 and abs(ycor-yecor2)<40 :
            gameover = True
        if abs(xcor-xecor3)<40 and abs(ycor-yecor3)<40 :
            gameover = True
        if abs(xcor-xecor4)<40 and abs(ycor-yecor4)<40 :
            gameover = True
        if abs(xcor-xecor5)<40 and abs(ycor-yecor5)<40 :
            gameover = True
        if abs(xcor-xecor6)<40 and abs(ycor-yecor6)<40 :
            gameover = True
        if abs(xcor-xecor7)<40 and abs(ycor-yecor7)<40 :
            gameover = True
        if abs(xcor-xecor8)<40 and abs(ycor-yecor8)<40 :
            gameover = True
        if abs(xcor-xecor9)<40 and abs(ycor-yecor9)<40 :
            gameover = True
        if abs(xcor-xecor10)<40 and abs(ycor-yecor10)<40 :
            gameover = True
            
            
            
    if gameover :
        gameoverf()

    clock.tick(60)
    
    

def text_screen(text,incolor,outcol,x,y):
    screen_text = font.render(text,True,incolor,outcol)
    window.blit(screen_text,[x,y])

def welcome():
    exit_game = False
    window.fill(red)
    while not exit_game:
        text_screen("Welcome to The CrossyRoad",green,black,150,200)
        text_screen("-By Rudransh Bhardwaj",green,black,150,250)
        text_screen("(press Any key to play)",green,black,150,300)
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True
                if event.type == pg.KEYDOWN :
                    gameloop()
        pg.display.update()
    clock.tick(60)

def gameoverf():
    gameover = False
    while not gameover:
        window.fill(red)
        text_screen("Game over ?!?!?!?!",green,black,100,200)
        text_screen("press Any key to play again",green,black,100,250)
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameover = True
                if event.type == pg.KEYDOWN :
                    welcome()
        pg.display.update()
    clock.tick(60)
    



welcome()


pg.quit()
quit()
