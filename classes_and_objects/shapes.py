import pygame
from colors import *

# AMONG US MAKER
def draw_amongus(window:pygame.display, color:tuple, x: int, y : int, scale=1, flip= False):
    """haha draw amongus hahahahahahhhahaha"""
    if flip:
        amogus_body = Ellipse(window,color, x * scale, y * scale,300 *scale,400 * scale)
        amogus_legs1 = Rectangle(window, color, (x+ 50)* scale, (y+ 300)* scale,50* scale,150* scale)
        amogus_legs2 = Rectangle(window, color, (x+ 200)* scale, (y + 300)* scale,50* scale,150* scale)
        amogus_backpack = Rectangle(window, color, (x + 275)* scale, (y + 50)* scale,75* scale,300* scale)
        glass = Ellipse(window, CC_BLUE, (x-50)* scale, (y+50)* scale ,300* scale,50* scale)
    else:
        amogus_body = Ellipse(window,color, x* scale , y* scale,300* scale,400* scale)
        amogus_legs1 = Rectangle(window, color, (x+ 50)* scale, (y+ 300)* scale,50* scale,150* scale)
        amogus_legs2 = Rectangle(window, color, (x+ 200)* scale, (y + 300)* scale,50* scale,150* scale)
        amogus_backpack = Rectangle(window, color, (x - 50)* scale, (y + 50)* scale,75* scale,300* scale)
        glass = Ellipse(window, CC_BLUE, (x+50)* scale, (y+50)* scale ,300* scale,50* scale)

    amongus = [amogus_body,amogus_backpack,amogus_legs1,amogus_legs2,glass]

    return amongus

# SHAPE CLASSES

class Shape():
    """Shapes class, barebones for any shape to be made"""
    def __init__(self, window:pygame.display, color:tuple, width=0):
        """window: The screen or window the shape is meant to be drawn on
        color: tuple of 3 RGB Values (0-255,0-255,0-255)
        width: This value determines whether the shape has a border | default =0 for no border, filled in"""
        self.window = window
        self.color = color
        self.width = width

    def change_color(self, new_color:tuple):
        """Changes the color of the shape
        new_color: a tuple of 3 ints, 0-255 (ex. (255,255,0))"""
        if not new_color is tuple:
            raise ValueError("Needs a tuple with 3 int values (0-255, 0-255, 0-255)")
        if not len(new_color) == 3:
            raise ValueError("Tuple need 3 int values in it.")
        
        self.color = new_color

    def change_width(self, new_width:int):
        """Changes the width of the shape, 0= filled in shape, input bigger than 0 will give the shape a border of that int
        new_width: int determines border width of the shape. 0 for filled in shape """
        self.width = new_width

class Line(Shape):
    """A class for a simple line"""
    def __init__(self,window:pygame.display, color:tuple, start_coord, end_coord, width=1):
        """window: The screen or window the shape is meant to be drawn on
        color: tuple of 3 RGB Values (0-255,0-255,0-255)
        start_coord: pair of int values the represent (x,y) coordinate points to start the line
        end_coord: pair of int values the represent (x,y) coordinate points to end the line
        width: This value determines the width of the line in pixels (px)
        """
        super().__init__(window, color, width)
        self.start = start_coord
        self.end = end_coord

    def draw(self):
        """Draws the line on the screen"""
        pygame.draw.line(self.window,self.color, self.start, self.end, self.width)

class Rectangle(Shape):
    """A class to draw rectangular shape"""
    def __init__(self, window:pygame.display, color:tuple, x:int, y:int ,side_width=1, side_length=1, line_width=0):
        """window: The screen or window the shape is meant to be drawn on
        color: tuple of 3 RGB Values (0-255,0-255,0-255)
        x: int value that determines the x-axis placement of the top left vertex of the rectangle (closer to 0: goes left, further from 0 goes right)
        y: int value that determines the y-axis placement of the top left vertex of the rectangle (closer to 0: goes up, further from 0 goes down)
        side_width: int value that determines how tall the rectangle is (going down from (x,y) coordinate)
        side_length: int value that determine how long the rectangle goes (going right from (x,y) coordinate)
        width: This value determines whether the shape has a border | default =0 for no border, filled in"""
        super().__init__(window,color, line_width)
        self.rect = pygame.Rect(x,y,side_width,side_length)

        self.x = x 
        self.y = y
        self.side_width = side_width
        self.side_length = side_length

    def change_side_lengths(self, new_width:int, new_length:int):
        self.rect = pygame.Rect(self.x,self.y,new_width,new_length)

        self.side_width = new_width
        self.side_length = new_length

    def change_side_width(self, new_width:int):
        self.change_side_lengths(new_width, self.side_length)

    def change_side_length(self, new_length:int):
        self.change_side_lengths(self.side_width, new_length)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect, self.width)

class Square(Rectangle):

    def __init__(self, window, color, x, y, side_length = 1, line_width = 0):
        super().__init__(window, color, x, y, side_length, side_length, line_width)

    def change_side_lengths(self, new_length: int):
        return super().change_side_lengths(new_length, new_length)
    
    def change_side_width(self, new_width:int):
        self.change_side_lengths(new_width, new_width)

    def change_side_length(self, new_length:int):
        self.change_side_lengths(new_length, new_length)

class Circ(Shape):
    
    def __init__(self, window, color, center_coords, radius, width=0):
        super().__init__(window,color, width)
        self.center = center_coords
        self.x, self.y = center_coords
        self.r = radius

    def change_radius(self, new_r:int):
        self.r = new_r

    def change_pos(self,new_x:int,new_y:int):
        self.center = (new_x,new_y)

        self.x = new_x
        self.y = new_y

    def change_x_pos(self, new_x:int):
        self.change_pos(new_x, self.y)
    
    def change_y_pos(self, new_y:int):
        self.change_pos(self.x, new_y)

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.center, self.r, self.width)

class Ellipse(Rectangle):

    def __init__(self, window, color, x, y, side_width=1, side_length=1, line_width = 0):
        super().__init__(window, color, x, y, side_width, side_length, line_width)

    def draw(self):
        pygame.draw.ellipse(self.window, self.color, self.rect, self.width)

class Polygon(Shape):

    def __init__(self,window, color, points, width=0):
        super().__init__(window,color,width)
        self.points = points


    def draw(self):
        pygame.draw.polygon(self.window,self.color,self.points,self.width)