import pygame
import sys
import random
from time import sleep
from time import *
import time


class main():
    def level_1():

        number_list = ["Apple","Orange","Grapes","WoodApple","PineApple","Papaw"]
        apple_list = []
        orange_list = []
        grape_list = []
        pine_list = []
        mango_list = []
        papaw_list = []

        apple_score = []
        orange_score = []
        grape_score = []
        pine_score = []
        mango_score = []
        papaw_score = []

        pygame.init()

        white = (255,255,255)
        black = (0,0,0)
        grey = (128,128,128)
        gray = (105,105,105)
        green = (0,255,0)
        light = (211,211,211)
        red = (255,0,0)
        blue = (0,0,255)
        
        time_left = 60

        total_score = 0


        screen = pygame.display.set_mode((640,520))
        pygame.display.set_caption("ABC-Pairs Memory Game ")

        screen.fill(white)
            
        screen.fill(grey,rect=[80,100,100,100])
        screen.fill(grey,rect=[200,100,100,100])
        screen.fill(grey,rect=[320,100,100,100])
        screen.fill(grey,rect=[440,100,100,100])
        screen.fill(grey,rect=[80,220,100,100])
        screen.fill(grey,rect=[200,220,100,100])
        screen.fill(grey,rect=[320,220,100,100])
        screen.fill(grey,rect=[440,220,100,100])
        screen.fill(grey,rect=[80,340,100,100])
        screen.fill(grey,rect=[200,340,100,100])
        screen.fill(grey,rect=[320,340,100,100])
        screen.fill(grey,rect=[440,340,100,100])

        pygame.display.update()

        game = False
        font = pygame.font.SysFont(None, 25)


        box_1_width = 100
        box_1_height = 140


        def message(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[box_1_width,box_1_height])
        def message2(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[220,140])
        def message3(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[340,380])
        def message4(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[460,260])
        def message5(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[340,140])
        def message6(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[340,260])
        def message7(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[450,140])
        def message8(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[90,380])
        def message9(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[100,260])
        def message10(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[220,380])
        def message11(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[220,260])
        def message12(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[460,380])
        def score_text(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[50,480])
        def level_text(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[250,480])
        def match(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[291,52])
        def level1(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[354,482])
        def score_val(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[151,484])
        def time(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[151,484])
        def start(msg,color):
            screen_text = font.render(msg, True, color)
            screen.blit(screen_text,[485,490])
        def complete(msg,color):
            screen_text = font.render(msg, True, color)
            screen_score.blit(screen_text,[150,100])
        def play(msg,color):
            screen_text = font.render(msg, True, color)
            screen_score.blit(screen_text,[282,177])
        def exit1(msg,color):
            screen_text = font.render(msg, True, color)
            screen_score.blit(screen_text,[482,177])
        def choose(msg,color):
            screen_text = font.render(msg, True, color)
            screen_score.blit(screen_text,[82,177])

            
            

        

        score_text("Score :",green)
        screen.fill(light,rect=[116,480,80,20])
        level_text("Level :",green)
        screen.fill(light,rect=[316,480,80,20])
        level1("1",black)
        screen.fill(grey,rect=[450,480,180,30])
        start("Start Game ",black)
        pygame.display.update()
        count = 1
        score = 0
        score_orange = 0
        score_grape = 0
        score_pine = 0
        score_mango = 0
        score_papaw = 0
        total_mins = time_left//60
        total_sec = 10

        final_score = 0
        final_score_apple = 5
        final_score_orange = 5
        final_score_grape = 5
        final_score_pine = 5
        final_score_mango = 5
        final_score_papaw = 5
        while True:
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if ((event.type==pygame.MOUSEBUTTONDOWN)):
                    x,y = pygame.mouse.get_pos()
                    if((x>=450 and x<=630) and (y>=480 and y<=510)):
                        screen.fill(grey,rect=[80,100,100,100])
                        message("Apple",black)
                        screen.fill(grey,rect=[320,340,100,100])
                        message3("Apple",black)
                        screen.fill(grey,rect=[200,100,100,100])
                        message2("Orange",black)
                        screen.fill(grey,rect=[440,220,100,100])
                        message4("Orange",black)
                        screen.fill(grey,rect=[320,100,100,100])
                        message5("Grapes",black)
                        screen.fill(grey,rect=[320,220,100,100])
                        message6("Grapes",black)
                        screen.fill(grey,rect=[440,100,100,100])
                        message7("Pineapple",black)
                        screen.fill(grey,rect=[80,340,100,100])
                        message8("Pineapple",black)
                        screen.fill(grey,rect=[80,220,100,100])
                        message9("Mango",black)
                        screen.fill(grey,rect=[200,340,100,100])
                        message10("Mango",black)
                        screen.fill(grey,rect=[200,220,100,100])
                        message11("Papaw",black)
                        screen.fill(grey,rect=[440,340,100,100])
                        message12("Papaw",black)
                        pygame.display.update()
                        while True:
                            if(total_sec >=0):
                                screen.fill(white,rect=[400,10,100,15])
                                pygame.display.update()
                                text = font.render(("0"+str(total_mins)+":"+str(total_sec)),True,black)
                                screen.blit(text,(400,10))
                                pygame.display.update()
                                total_mins = 0
                                total_sec -=1
                                sleep(1)
                            
                            for event in pygame.event.get():
                                if event.type==pygame.KEYDOWN:
                                    if(event.key== pygame.K_p):
                                        main.level_1()
                                    elif(event.key==pygame.K_e):
                                        pygame.quit()
                                        sys.exit()
                                    elif(event.key==pygame.K_2):
                                        import Pairs_2
                                        
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    screen.fill(white,rect=[291,52,100,15])
                                    pygame.display.update()
                                    mx, my = pygame.mouse.get_pos()     
                                    if(((mx>=80 and mx <=180)and(my>=100 and my<=200))):
                                        orange_score.append(1)
                                        grape_score.append(1)
                                        pine_score.append(1)
                                        mango_score.append(1)
                                        papaw_score.append(1)
                                        apple_score.append(1)
                                        screen.fill(white,rect=[291,52,100,15])
                                        match("",white)
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        apple_list.append(1)
                                        screen.fill(gray,rect=[80,100,100,100])
                                        message("Apple",black)
                                        pygame.display.update()
                                        screen.fill(white,rect=[291,52,100,15])
                                        pygame.display.update()
                                    if(((mx>=320 and mx<=420)and(my>=340 and my<=440))):
                                        apple_score.append(2)
                                        screen.fill(white,rect=[291,52,100,15])
                                        pygame.display.update()
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        apple_list.append(2)
                                        screen.fill(gray,rect=[320,340,100,100])
                                        message3("Apple",black)
                                        pygame.display.update()
                                        screen.fill(white,rect=[291,52,100,15])
                                        pygame.display.update()
                                        
                                        
                                    apple_list = list(dict.fromkeys(apple_list))
                                    if((len(apple_list))==2):
                                        final_score +=20
                                        score =20
                                        screen.fill(white,rect=[80,100,100,100])
                                        screen.fill(white,rect=[320,340,100,100])
                                        pygame.display.update()
                                    else:
                                        score = 0
                                        screen.fill(white,rect=[291,52,100,15])
                                        pygame.display.update()
                                        
                                    
                                        
                                       
                                        
                                       
                                    if((mx>=200 and mx<=300)and(my>=100 and my<=200)):
                                        orange_score.append(3)
                                        grape_score.append(3)
                                        pine_score.append(3)
                                        mango_score.append(3)
                                        papaw_score.append(3)
                                        apple_score.append(3)
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                            
                                        orange_list.append(1)
                                        screen.fill(gray,rect=[200,100,100,100])
                                        message2("Orange",black)
                                        pygame.display.update()
                                        message7("Pineapple",black)
                                        pygame.display.update()
                                    if((mx>=440 and mx<=540)and(my>=220 and my<=320)):
                                        orange_score.append(4)
                                        grape_score.append(4)
                                        pine_score.append(4)
                                        mango_score.append(4)
                                        papaw_score.append(4)
                                        apple_score.append(4)
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                        orange_list.append(2)
                                        screen.fill(gray,rect=[440,220,100,100])
                                        message4("Orange",black)
                                        pygame.display.update()

                                    orange_list = list(dict.fromkeys(orange_list))
                                    if((len(orange_list))==2):
                                        final_score +=20
                                        score_orange =20
                                        screen.fill(white,rect=[200,100,100,100])
                                        screen.fill(white,rect=[440,220,100,100])
                                        pygame.display.update()
                                    else:
                                        score_orange = 0
                                        screen.fill(white,rect=[291,52,100,15])
                                        pygame.display.update()
                                   

                                    
                                    if((mx>=320 and mx<=420)and(my>=100 and my<=200)):
                                        orange_score.append(5)
                                        grape_score.append(5)
                                        pine_score.append(5)
                                        mango_score.append(5)
                                        papaw_score.append(5)
                                        apple_score.append(5)
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                        grape_list.append(1)
                                        screen.fill(gray,rect=[320,100,100,100])
                                        message5("Grapes",black)
                                        pygame.display.update()
                                    if((mx>=320 and mx<=420)and(my>=220 and my<=320)):
                                        orange_score.append(6)
                                        grape_score.append(6)
                                        pine_score.append(6)
                                        mango_score.append(6)
                                        papaw_score.append(6)
                                        apple_score.append(6)
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                        grape_list.append(2)
                                        screen.fill(gray,rect=[320,220,100,100])
                                        message6("Grapes",black)
                                        pygame.display.update()
                                    grape_list = list(dict.fromkeys(grape_list))
                                    
                                    if((len(grape_list))==2):
                                        final_score +=20
                                        score_grape =20
                                        screen.fill(white,rect=[320,100,100,100])
                                        screen.fill(white,rect=[320,220,100,100])
                                        pygame.display.update()
                                    else:
                                        score_grape =0
                                        screen.fill(white,rect=[291,52,100,15])
                                        pygame.display.update()
                                    
                                        

                                    if((mx>=440 and mx<=540)and(my>=100 and my<=200)):
                                        orange_score.append(7)
                                        grape_score.append(7)
                                        pine_score.append(7)
                                        mango_score.append(7)
                                        papaw_score.append(7)
                                        apple_score.append(7)
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                        pine_list.append(1)
                                        screen.fill(gray,rect=[440,100,100,100])
                                        message7("Pineapple",black)
                                        pygame.display.update()
                                    if((mx>=80 and mx<=180)and(my>=340 and my<=440)):
                                        orange_score.append(8)
                                        grape_score.append(8)
                                        pine_score.append(8)
                                        mango_score.append(8)
                                        papaw_score.append(8)
                                        apple_score.append(8)
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                        pine_list.append(2)
                                        screen.fill(gray,rect=[80,340,100,100])
                                        message8("Pineapple",black)
                                        pygame.display.update()
                                        
                                    pine_list = list(dict.fromkeys(pine_list))
                                    if((len(pine_list))==2):
                                        final_score +=20
                                        score_pine =20
                                        screen.fill(white,rect=[80,340,100,100])
                                        screen.fill(white,rect=[440,100,100,100])
                                        pygame.display.update()
                                    else:
                                        score_pine = 0
                                        screen.fill(white,rect=[291,52,100,15])
                                        pygame.display.update()
                                    
                                        

                                    if((mx>=80 and mx<=180)and(my>=220 and my<=320)):
                                        orange_score.append(9)
                                        grape_score.append(9)
                                        pine_score.append(9)
                                        mango_score.append(9)
                                        papaw_score.append(9)
                                        apple_score.append(9)
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                        mango_list.append(1)
                                        screen.fill(gray,rect=[80,220,100,100])
                                        message9("Mango",black)
                                        pygame.display.update()
                                    if((mx>=200 and mx<=300)and(my>=340 and my<=440)):
                                        orange_score.append(10)
                                        grape_score.append(10)
                                        pine_score.append(10)
                                        mango_score.append(10)
                                        papaw_score.append(10)
                                        apple_score.append(10)
                                        if(score_papaw != 20):
                                            del papaw_list[0:2]
                                            screen.fill(grey,rect=[200,220,100,100])
                                            message11("Papaw",black)
                                            screen.fill(grey,rect=[440,340,100,100])
                                            message12("Papaw",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,220,100,100])
                                            screen.fill(white,rect=[440,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                        mango_list.append(2)
                                        screen.fill(gray,rect=[200,340,100,100])
                                        message10("Mango",black)
                                        pygame.display.update()
                                    

                                    mango_list = list(dict.fromkeys(mango_list))
                                    if((len(mango_list))==2):
                                        final_score +=20
                                        score_mango =20
                                        screen.fill(white,rect=[200,340,100,100])
                                        screen.fill(white,rect=[80,220,100,100])
                                        pygame.display.update()
                                    else:
                                        score_mango = 0
                                        screen.fill(white,rect=[291,52,100,15])
                                        pygame.display.update()
                                    
                                    

                                    if((mx>=200 and mx<=300)and(my>=220 and my<=320)):
                                        orange_score.append(11)
                                        grape_score.append(11)
                                        pine_score.append(11)
                                        mango_score.append(11)
                                        papaw_score.append(11)
                                        apple_score.append(11)
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                        papaw_list.append(1)
                                        screen.fill(gray,rect=[200,220,100,100])
                                        message11("Papaw",black)
                                        pygame.display.update()
                                    if((mx>=440 and mx<=540)and(my>=340 and my<=440)):
                                        orange_score.append(12)
                                        grape_score.append(12)
                                        pine_score.append(12)
                                        mango_score.append(12)
                                        papaw_score.append(12)
                                        apple_score.append(12)
                                        if(score_mango != 20):
                                            del mango_list[0:2]
                                            screen.fill(grey,rect=[80,220,100,100])
                                            message9("Mango",black)
                                            screen.fill(grey,rect=[200,340,100,100])
                                            message10("Mango",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,220,100,100])
                                            screen.fill(white,rect=[200,340,100,100])
                                            pygame.display.update()
                                        if(score_pine != 20):
                                            del pine_list[0:2]
                                            screen.fill(grey,rect=[80,340,100,100])
                                            message8("Pineapple",black)
                                            screen.fill(grey,rect=[440,100,100,100])
                                            message7("Pineapple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,340,100,100])
                                            screen.fill(white,rect=[440,100,100,100])
                                            pygame.display.update()
                                        if(score_grape != 20):
                                            del grape_list[0:2]
                                            screen.fill(grey,rect=[320,100,100,100])
                                            message5("Grapes",black)
                                            screen.fill(grey,rect=[320,220,100,100])
                                            message6("Grapes",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[320,100,100,100])
                                            screen.fill(white,rect=[320,220,100,100])
                                            pygame.display.update()
                                        if(score_orange != 20):
                                            del orange_list[0:2]
                                            screen.fill(grey,rect=[200,100,100,100])
                                            message2("Orange",black)
                                            screen.fill(grey,rect=[440,220,100,100])
                                            message4("Orange",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[200,100,100,100])
                                            screen.fill(white,rect=[440,220,100,100])
                                            pygame.display.update()
                                        if(score != 20):
                                            del apple_list[0:2]
                                            screen.fill(grey,rect=[80,100,100,100])
                                            
                                            message("Apple",black)
                                            screen.fill(grey,rect=[320,340,100,100])
                                            message3("Apple",black)
                                            pygame.display.update()
                                        else:
                                            screen.fill(white,rect=[80,100,100,100])
                                            screen.fill(white,rect=[320,340,100,100])
                                            pygame.display.update()
                                        papaw_list.append(2)
                                        screen.fill(gray,rect=[440,340,100,100])
                                        message12("Papaw",black)
                                        pygame.display.update()

                                    papaw_list = list(dict.fromkeys(papaw_list))
                                    if((len(papaw_list))==2):
                                        final_score +=20
                                        score_papaw =20
                                        screen.fill(white,rect=[440,340,100,100])
                                        screen.fill(white,rect=[200,220,100,100])
                                        pygame.display.update()
                                    else:
                                        score_papaw = 0
                                        screen.fill(white,rect=[291,52,100,15])
                                        pygame.display.update()


                                  
                                    score_all = score_orange+score_grape+score_pine+score_mango+score_papaw+score
                                   
                                    
                                   
                                    if(score_all==120):
                                        bonus = total_sec
                                        for apple in range(0,len(apple_score)):
                                            try:
                                                if((apple_score[apple]==1 and apple_score[apple+1]==2)or(apple_score[apple]==2 and apple_score[apple+1]==1)):
                                                    final_score_apple += 20
                                                elif(((apple_score[apple]==1 or apple_score[apple]==2)and(apple_score[apple+1] !=1 and apple_score[apple+1]!=2))==True):
                                                    final_score_apple = final_score_apple + (-5)
                                                    
                                                  
                                                elif((apple_score[apple]==3 and apple_score[apple+1]==4)or(apple_score[apple]==4 and apple_score[apple+1]==3)):
                                                    final_score_orange += 20
                                                elif((apple_score[apple]==3 or apple_score[apple]==4)and(apple_score[apple+1] !=3 and apple_score[apple+1]!=4)==True):
                                                    final_score_orange = final_score_orange + (-5)

                                                elif((apple_score[apple]==5 and apple_score[apple+1]==6)or(apple_score[apple]==6 and apple_score[apple+1]==5)):
                                                    final_score_grape += 20
                                                elif((apple_score[apple]==5 or apple_score[apple]==6)and(apple_score[apple+1] !=5 and apple_score[apple+1]!=6)==True):
                                                    final_score_grape = final_score_grape + (-5)

                                                elif((apple_score[apple]==7 and apple_score[apple+1]==8)or(apple_score[apple]==8 and apple_score[apple+1]==7)):
                                                    final_score_pine += 20
                                                elif((apple_score[apple]==7 or apple_score[apple]==8)and(apple_score[apple+1] !=7 and apple_score[apple+1]!=8)==True):
                                                    final_score_pine = final_score_pine + (-5)

                                                elif((apple_score[apple]==9 and apple_score[apple+1]==10)or(apple_score[apple]==10 and apple_score[apple+1]==9)):
                                                    final_score_mango += 20
                                                elif((apple_score[apple]==9 or apple_score[apple]==10)and(apple_score[apple+1] !=9 and apple_score[apple+1] != 10)==True):
                                                    final_score_mango = final_score_mango + (-5)

                                                elif((apple_score[apple]==11 and apple_score[apple+1]==12)or(apple_score[apple]==12 and apple_score[apple+1]==11)):
                                                    final_score_papaw += 20
                                                elif((apple_score[apple]==11 or apple_score[apple]==12)and(apple_score[apple+1] !=11 and apple_score[apple+1] != 12)==True):
                                                    final_score_papaw = final_score_papaw + (-5)
                                            except(IndexError):
                                                continue
                                            
                                            

                                        try:    
                                            if((apple_score[-2]==1 or apple_score[-2]==2)and(apple_score[-1]==1 or apple_score[-1]==2)):
                                                final_score_apple -= 5
                                            elif((apple_score[-2]==3 or apple_score[-2]==4)and(apple_score[-1]==3 or apple_score[-1]==4)):
                                                final_score_orange -= 5
                                            elif((apple_score[-2]==5 or apple_score[-2]==6)and(apple_score[-1]==5 or apple_score[-1]==6)):
                                                final_score_grape -= 5
                                            elif((apple_score[-2]==7 or apple_score[-2]==8)and(apple_score[-1]==7 or apple_score[-1]==8)):
                                                final_score_pine -= 5
                                            elif((apple_score[-2]==9 or apple_score[-2]==10)and(apple_score[-1]==9 or apple_score[-1]==10)):
                                                final_score_mango -= 5
                                            elif((apple_score[-2]==11 or apple_score[-2]==12)and(apple_score[-1]==11 or apple_score[-1]==12)):
                                                final_score_papaw -= 5
                                        except(IndexError):
                                            apple_score = []

                                        total_score = final_score_apple + final_score_orange + final_score_grape + final_score_pine + final_score_mango + final_score_papaw + bonus
                                        score_val(str(total_score),red)
                                        pygame.display.update()
                                        sleep(3)
                                        screen_score = pygame.display.set_mode((600,250))
                                        pygame.display.set_caption("ABC Scores")
                                        screen_score.fill(white)
                                        pygame.display.update()
                                        scoring =  "Level Complete !"
                                        scoring_1 = "\n"
                                        scoring_2 = "You Scored "+str(total_score)+"bonus( "+str(bonus)
                                        scoring_3 = " )"
                                        complete((scoring+scoring_1+scoring_2+scoring_3),black)
                                        screen_score.fill(green,rect=[280,175,120,60])
                                        play("Play Again(P)",black)
                                        screen_score.fill(red,rect=[480,175,70,60])
                                        exit1("Exit (E)",black)
                                        screen_score.fill(blue,rect=[80,175,120,60])
                                        choose("Level-2 (2)",black)
                                        pygame.display.update()

                                    elif(total_sec <0 and score_all>0):
                                        fruit_score = []
                                        final_score_apple = 0
                                        final_score_orange = 0
                                        final_score_grape = 0
                                        final_score_pine = 0
                                        final_score_mango = 0
                                        final_score_papaw = 0
                                        bonus = 0
                                        for apple in range(0,len(apple_score)):
                                            try:
                                                if((apple_score[apple]==1 and apple_score[apple+1]==2)or(apple_score[apple]==2 and apple_score[apple+1]==1)):
                                                    final_score_apple += 20
                                                elif(((apple_score[apple]==1 or apple_score[apple]==2)and(apple_score[apple+1] !=1 and apple_score[apple+1]!=2))==True):
                                                    final_score_apple = final_score_apple + (-5)
                                                    
                                                  
                                                elif((apple_score[apple]==3 and apple_score[apple+1]==4)or(apple_score[apple]==4 and apple_score[apple+1]==3)):
                                                    final_score_orange += 20
                                                elif((apple_score[apple]==3 or apple_score[apple]==4)and(apple_score[apple+1] !=3 and apple_score[apple+1]!=4)==True):
                                                    final_score_orange = final_score_orange + (-5)

                                                elif((apple_score[apple]==5 and apple_score[apple+1]==6)or(apple_score[apple]==6 and apple_score[apple+1]==5)):
                                                    final_score_grape += 20
                                                elif((apple_score[apple]==5 or apple_score[apple]==6)and(apple_score[apple+1] !=5 and apple_score[apple+1]!=6)==True):
                                                    final_score_grape = final_score_grape + (-5)

                                                elif((apple_score[apple]==7 and apple_score[apple+1]==8)or(apple_score[apple]==8 and apple_score[apple+1]==7)):
                                                    final_score_pine += 20
                                                elif((apple_score[apple]==7 or apple_score[apple]==8)and(apple_score[apple+1] !=7 and apple_score[apple+1]!=8)==True):
                                                    final_score_pine = final_score_pine + (-5)

                                                elif((apple_score[apple]==9 and apple_score[apple+1]==10)or(apple_score[apple]==10 and apple_score[apple+1]==9)):
                                                    final_score_mango += 20
                                                elif((apple_score[apple]==9 or apple_score[apple]==10)and(apple_score[apple+1] !=9 and apple_score[apple+1] != 10)==True):
                                                    final_score_mango = final_score_mango + (-5)

                                                elif((apple_score[apple]==11 and apple_score[apple+1]==12)or(apple_score[apple]==12 and apple_score[apple+1]==11)):
                                                    final_score_papaw += 20
                                                elif((apple_score[apple]==11 or apple_score[apple]==12)and(apple_score[apple+1] !=11 and apple_score[apple+1] != 12)==True):
                                                    final_score_papaw = final_score_papaw + (-5)
                                            except(IndexError):
                                                continue
                                            
                                            

                                        try:    
                                            if((apple_score[-2]==1 or apple_score[-2]==2)and(apple_score[-1]==1 or apple_score[-1]==2)):
                                                final_score_apple -= 5
                                            elif((apple_score[-2]==3 or apple_score[-2]==4)and(apple_score[-1]==3 or apple_score[-1]==4)):
                                                final_score_orange -= 5
                                            elif((apple_score[-2]==5 or apple_score[-2]==6)and(apple_score[-1]==5 or apple_score[-1]==6)):
                                                final_score_grape -= 5
                                            elif((apple_score[-2]==7 or apple_score[-2]==8)and(apple_score[-1]==7 or apple_score[-1]==8)):
                                                final_score_pine -= 5
                                            elif((apple_score[-2]==9 or apple_score[-2]==10)and(apple_score[-1]==9 or apple_score[-1]==10)):
                                                final_score_mango -= 5
                                            elif((apple_score[-2]==11 or apple_score[-2]==12)and(apple_score[-1]==11 or apple_score[-1]==12)):
                                                final_score_papaw -= 5
                                        except(IndexError):
                                            apple_score = []
                                        
                                            
                                        fruit_score.append(final_score_apple)
                                        fruit_score.append(final_score_orange)
                                        fruit_score.append(final_score_grape)
                                        fruit_score.append(final_score_pine)
                                        fruit_score.append(final_score_mango)
                                        fruit_score.append(final_score_papaw)
                                        for fruits in range(0,len(fruit_score)):
                                            if(fruit_score[fruits]==15):
                                                fruit_score[fruits] +=5
                                            elif(fruit_score[fruits]>0 and fruit_score[fruits] != 15):
                                                fruit_score[fruits] +=10
                                        for total in range(0,len(fruit_score)):
                                            total_score += fruit_score[total]
        
                                        score_val(str(total_score),red)
                                        pygame.display.update()
                                        sleep(2)
                                        screen_score = pygame.display.set_mode((600,250))
                                        pygame.display.set_caption("ABC Scores")
                                        pygame.display.flip()
                                        screen_score.fill(white)
                                        pygame.display.update()
                                        scoring =  "Level Complete !"
                                        scoring_1 = "\n"
                                        scoring_2 = "You Scored "+str(total_score)+"bonus( "+str(bonus)
                                        scoring_3 = " )"
                                        complete((scoring+scoring_1+scoring_2+scoring_3),black)
                                        screen_score.fill(green,rect=[280,175,120,60])
                                        play("Play Again (P)",black)
                                        screen_score.fill(red,rect=[480,175,70,60])
                                        exit1("Exit (E) ",black)
                                        screen_score.fill(blue,rect=[80,175,120,60])
                                        choose("Level-2 (2)",black)
                                        pygame.display.update()

                                    elif(score_all == 0 and total_sec<0):
                                        total_score = 0
                                        score_val(str(total_score),red)
                                        pygame.display.update()
                                        sleep(2)
                                        screen_score = pygame.display.set_mode((600,250))
                                        pygame.display.set_caption("ABC Scores")
                                        pygame.display.update()
                                        screen_score.fill(white)
                                        pygame.display.update()
                                        scoring =  "Level Complete !"
                                        scoring_1 = "\n"
                                        scoring_2 = "You Scored "+str(total_score)+"bonus( "+str(0)
                                        scoring_3 = " )"
                                        complete((scoring+scoring_1+scoring_2+scoring_3),black)
                                        screen_score.fill(green,rect=[280,175,120,60])
                                        play("Play Again (P)",black)
                                        screen_score.fill(red,rect=[480,175,100,60])
                                        exit1("Exit (E)",black)
                                        screen_score.fill(blue,rect=[80,175,120,60])
                                        choose("Level-2 (2)",black)
                                        pygame.display.flip()

                                        
                            
main.level_1()                              
                                    
                                    
                                    
                    
                

        
    
        
    
            
        
                


            
                
            
                
                
            
                
                
                
                
                
            

    
            

