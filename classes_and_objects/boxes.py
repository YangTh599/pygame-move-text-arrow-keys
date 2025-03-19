# These are Classes that help with on screen graphics

#font = pygame.font.Font("C:\\Windows/Users/YangTh599/Documents/GitHub/pygame-template/fonts/MoreSugar-Regular.ttf") # MORESUGAR Font

from colors import *
import pygame
from os.path import join
pygame.init()

class Text_box():

    def __init__(self, window, x, y, width, height, text, text_color = WHITE,rect_color = THAYER_GREEN,font="Comic Sans MS",text_size = 24, draw_rect = True, centered = True, rotation = 0):
        self.rect = pygame.Rect(x,y,width,height)
        self.window = window

        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.draw_rect = draw_rect
        self.rect_color = rect_color
        self.centered = centered
        self.rotation = rotation

        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.font = font
        self.text_font = pygame.font.SysFont(font, text_size)

    # ----- MUTATORS -----

    def change_font(self, new_font):
        if (new_font[-4:] == ".ttf" or new_font[-4:] == ".otf"):
            self.text_font = pygame.font.Font(new_font, self.text_size)
        else:
            self.text_font = pygame.font.SysFont(new_font, self.text_size)

        self.font = new_font

    def change_font_color(self, new_color):
        if not new_color is tuple:
            raise ValueError("Needs a tuple with 3 int values (0-255, 0-255, 0-255)")
        
        self.text_color = new_color

    def change_rect_color(self, new_color):
        if not new_color is tuple:
            raise ValueError("Needs a tuple with 3 int values (0-255, 0-255, 0-255)")
        
        self.rect_color = new_color

    def italicize(self, italicize = True):
        if not (self.font[-4:] == ".ttf" or self.font[-4:] == ".otf"):
            self.text_font = pygame.font.SysFont(self.font, self.text_size, italic=italicize)
        else:
            self.text_font.set_italic(True)
    
    def bolden(self, boldize = True):
        if not (self.font[-4:] == ".ttf" or self.font[-4:] == ".otf"):
            self.text_font = pygame.font.SysFont(self.font, self.text_size, bold=boldize)
        else:
            self.text_font.set_bold(True)

    def rotate(self, rotation):
        self.rotation = rotation

    def update_text(self, new_text):
        self.text = new_text

    # ----- DRAW FUNCTIONS -----

    def draw_textbox(self):
        text = self.text_font.render(self.text, True, self.text_color)
        if self.rotation != 0:
            text = pygame.transform.rotate(text, self.rotation)
        if self.draw_rect:
            pygame.draw.rect(self.window, self.rect_color, self.rect)
        if self.centered:
            text_rect = text.get_rect(center=self.rect.center)
            self.window.blit(text, text_rect)
        
        else:
            self.window.blit(text, [self.x,self.y])

    def draw_text(self):
        text = self.text_font.render(self.text, True, self.text_color)
        if self.rotation != 0:
            text = pygame.transform.rotate(text, self.rotation)
        self.window.blit(text, [self.x,self.y])

class Image_box():

    def __init__(self,window, x, y, width, height, image):
        self.window = window
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(join('assets','images',image))

    def draw_image(self):
        self.window.blit(self.image, (self.x, self.y))

