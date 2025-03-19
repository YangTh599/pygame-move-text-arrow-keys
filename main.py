import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes

def init_game():
    """Initiates Pygame, Pygame.font, and sets the Screen window and caption"""
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window,boxes):
    """DRAW FUNCTION | allows screen graphics to be added"""
    #BACKGROUND
    window.fill(WHITE) # 15
    

    #FOREGROUND
    for box in boxes:
        box.draw_textbox()

    #UPDATE DISPLAY
    pygame.display.update()

def handle_events(char):
    """Handles any pygame event such as key input"""
    vel = 5
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    char[0].update_text("up")
                elif event.key == pygame.K_DOWN:
                    char[0].update_text("down")
                elif event.key == pygame.K_LEFT:
                    char[0].update_text("left")
                elif event.key == pygame.K_RIGHT:
                    char[0].update_text("right")
                else:
                    char[0].update_text(event.unicode)
                
            
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if not (char[0].y) < 0:
            char[0].change_y_pos(char[0].y - vel)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if not (char[0].y + char[0].height) > SCREEN_HEIGHT:
            char[0].change_y_pos(char[0].y + vel)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if not (char[0].x) < 0:
            char[0].change_x_pos(char[0].x - vel)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if not (char[0].x + char[0].width) > SCREEN_WIDTH:
            char[0].change_x_pos(char[0].x + vel)


    return True

def main(): # MAIN FUNCTION
    """Main Function : main"""
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE
    textbox1 = boxes.Text_box(window, (SCREEN_WIDTH //2), (SCREEN_HEIGHT//2), 150,100,"The last key you press will show up here.", text_color= BLACK)
    
    tbs = [textbox1]
    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick


        run = handle_events(tbs)
        

        
        draw(window,tbs) # UPDATES SCREEN

    pygame.quit()
    sys.quit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

