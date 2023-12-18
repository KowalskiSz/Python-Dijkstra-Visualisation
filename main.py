import pygame
from tkinter import messagebox, Tk
import sys
import DEFINE
import BoxPoint
import FLAG_STATUS

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
Creating array of BOX Oojects - each obj is a box on a grid, has its own properties and methods
'''
for i in range(DEFINE.columns):
    temp_arr = list()
    for j in range(DEFINE.rows):
        temp_arr.append(BoxPoint.BoxPoint(i,j,
                                 window,box_width
                                 ,box_height))
    box_grid.append(temp_arr)
'''
Set neighbourds for all the PIONTS OBJ
'''
for i in range(DEFINE.columns):
    for j in range(DEFINE.rows):
        box_grid[i][j].get_neighboursPoints(box_grid)




#set the start box
box_grid[0][0].start_box = True


def main():
    #Before starting the alghorytm - no start flag and no target set
    FLAG_STATUS.START_ALGORYTHM = False
    FLAG_STATUS.TARGET_SET = False

    while True:
        for event in pygame.event.get():

            # Quit window and terminate the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] == True and not FLAG_STATUS.TARGET_SET:
                '''
                Settng the taget box 
                '''
                pox_X = pygame.mouse.get_pos()[0]
                pox_Y = pygame.mouse.get_pos()[1]
                a = pox_X // box_width #the coordiantes must be divided bo box dimentions to get exact coords that maches the grid positions
                b = pox_Y // box_height
                box_grid[a][b].target_box = True
                FLAG_STATUS.TARGET_SET = True

            elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] == True:
                '''
                Setting the wall only whan the key is pressed and mouse is in motion
                '''
                pox_X = pygame.mouse.get_pos()[0]
                pox_Y = pygame.mouse.get_pos()[1]
                a = pox_X // box_width
                b = pox_Y // box_height
                box_grid[a][b].wall_box = True


        window.fill((0,0,0))

        '''
        Plotting the grid on the screen 
        '''
        for x in range(DEFINE.columns):
            for y in range(DEFINE.rows):
                '''
                Displaying the objects by going througt the grid array of objs and refering to proper flags
                '''
                box_grid[x][y].draw_object(DEFINE.COLOR_mainBox)
                if box_grid[x][y].start_box:
                    box_grid[x][y].draw_object(DEFINE.COLOR_startingPoint)
                elif box_grid[x][y].target_box:
                    box_grid[x][y].draw_object(DEFINE.COLOR_target)
                elif box_grid[x][y].wall_box:
                    box_grid[x][y].draw_object(DEFINE.COLOR_wallPoint)

        pygame.display.flip()



if __name__ == '__main__':

    main()
