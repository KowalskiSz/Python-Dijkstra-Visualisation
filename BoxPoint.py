import pygame

import DEFINE
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

        #Algorythm properies
        self.inQueue = False
        self.processed = False

        self.nextToObjArray = list()

    '''
    Draw the object on the grid
    '''
    def draw_object(self, color):
        pygame.draw.rect(self.win, color, (count_position(self.b_w,self.x),
                                                count_position(self.b_h,self.y),
                                                self.b_w - 2, self.b_h - 2))


    '''
    Getting the neighbours of current OBJ Point of the GRID
    '''
    def get_neighboursPoints(self, gridArray):
        '''
        Searching for points vertically
        '''
        if self.x > 0:
            self.nextToObjArray.append(gridArray[self.x - 1][self.y])
        if self.x < DEFINE.columns - 1:
            self.nextToObjArray.append(gridArray[self.x + 1][self.y])
        '''
        Searching for points vertically
        '''
        if self.y > 0:
            self.nextToObjArray.append(gridArray[self.x][self.y - 1])
        if self.y < DEFINE.rows - 1:
            self.nextToObjArray.append(gridArray[self.x][self.y + 1])
