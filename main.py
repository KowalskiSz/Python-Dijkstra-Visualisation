import pygame
from tkinter import messagebox, Tk
import sys
import DEFINE
import BoxPoint

'''
Rewrite the project BUT make each BOX a uniq OBJ - 
in order to have own properties, and share same methods
'''

#Sigle box dimentions
box_width = DEFINE.window_width // DEFINE.columns
box_height = DEFINE.window_height // DEFINE.rows

window = pygame.display.set_mode((DEFINE.window_width,DEFINE.window_height))
pygame.display.set_caption("Djikstra Visualization")

'''
Creating the grid of boxes
'''
box_grid = list()

'''
Creating array of BOX Bojects - each obj is a box on a grid
'''
for i in range(DEFINE.columns):
    temp_arr = list()
    for j in range(DEFINE.rows):
        temp_arr.append(BoxPoint.BoxPoint(i,j,
                                 window,box_width
                                 ,box_height))
    box_grid.append(temp_arr)

#set the start box
box_grid[0][0].start_box = True


def main():
    while True:
        for event in pygame.event.get():

            # Quit window and terminate the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.fill((0,0,0))

        '''
        Plotting the grid on the screen 
        '''
        for x in range(DEFINE.columns):
            for y in range(DEFINE.rows):
                box_grid[x][y].draw_object(DEFINE.COLOR_mainBox)
                if box_grid[x][y].start_box:
                    box_grid[x][y].draw_object(DEFINE.COLOR_startingPoint)

        pygame.display.flip()



if __name__ == '__main__':

    main()
