import pygame
from CountCoordinates import count_position


class BoxPoint:

    def __init__(self, x_pos, y_pos, window, box_w, box_h):
        self.x = x_pos
        self.y = y_pos
        self.win = window
        self.b_w = box_w
        self.b_h = box_h
        #Flags
        self.start_box = False
        self.target_box = False
        self.wall_box = False

    '''
    Draw the object on the grid
    '''
    def draw_object(self, color):
        pygame.draw.rect(self.win, color, (count_position(self.b_w,self.x),
                                                count_position(self.b_h,self.y),
                                                self.b_w - 2, self.b_h - 2))



