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
Creating the grid of boxes and queue for processing the alg
'''
box_grid = list()
q = list()



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
box_grid[0][0].inQueue =True
q.append(box_grid[0][0])

def main():
    #Before starting the alghorytm - no start flag and no target set
    FLAG_STATUS.START_ALGORYTHM = False
    FLAG_STATUS.TARGET_SET = False
    '''
    Variable for executing the search
    '''
    search_inProgress = True
    target_box_def = None

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
                target_box_def = box_grid[a][b]
                FLAG_STATUS.TARGET_SET = True
                #print(target_box_def)

            elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] == True:
                '''
                Setting the wall only when the key is pressed and mouse is in motion
                '''
                pox_X = pygame.mouse.get_pos()[0]
                pox_Y = pygame.mouse.get_pos()[1]
                a = pox_X // box_width
                b = pox_Y // box_height
                box_grid[a][b].wall_box = True

            elif event.type == pygame.KEYDOWN and FLAG_STATUS.TARGET_SET:
                FLAG_STATUS.START_ALGORYTHM = True

        '''
        Executing the search alghorytm
        '''
        if FLAG_STATUS.START_ALGORYTHM:
            '''
            alghorytm logic
            '''
            if len(q) > 0 and search_inProgress:
                current_box = q.pop(0)
                current_box.processed = True
                '''
                Check - if the current box object is a TARGET
                '''
                if current_box == target_box_def:
                    search_inProgress = False
                else:
                    '''
                    Check every neighbour of THE CURRENT OBJECT
                    '''
                    for n in current_box.nextToObjArray:
                        if not n.wall_box and not n.inQueue:
                            n.inQueue = True
                            q.append(n)
            else:
                '''
                If the SOLUTION IS NOT AVAIABLE
                '''
                if search_inProgress:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No solution", "Target is unavailable")
                    search_inProgress = False
                    pygame.quit()
                    sys.exit()


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
                if box_grid[x][y].inQueue:
                    box_grid[x][y].draw_object(DEFINE.COLOR_inQueue)
                if box_grid[x][y].processed:
                    box_grid[x][y].draw_object(DEFINE.COLOR_visited)
                if box_grid[x][y].target_box:
                    box_grid[x][y].draw_object(DEFINE.COLOR_target)
                if box_grid[x][y].wall_box:
                    box_grid[x][y].draw_object(DEFINE.COLOR_wallPoint)

        pygame.display.flip()



if __name__ == '__main__':

    main()
