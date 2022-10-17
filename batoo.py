from tkinter import messagebox, Tk
import pygame
import sys

window_width = 700
window_height = 700

window = pygame.display.set_mode((window_width, window_height))

columns = 50
rows =  50

box_width = window_width//columns
box_height= window_height//rows
grid = []#empty array

class Box:
    def __init__(self,i,j):
        self.x = i
        self.y = j
        self.start=False#start box
        self.wall=False#wall box
        self.target=False#target box
        self.node=False # node box
        
    def draw(self, win, color):
        pygame.draw.rect(win, color,(self.x * box_width,self.y* box_height,box_width-2, box_height-2))

#grid
for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Box(i,j))
    grid.append(arr)

# start box pre define garne ho?
#maile pre define gareko xu natra chaneg garaula
start_box = grid[0][0]
start_box.start = True

def main():
    begin_algo = False #start algorithm
    target_box_set= False


    while True:
        for event in pygame.event.get():
            # Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #mouse commands capture mouse position
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                #left mouse button is wall button 0
                if event.buttons[0]:
                    i = x // box_width
                    j = y// box_height
                    grid[i][j].wall =True
                # target point right mouse button 2
                if event.buttons[2] and not target_box_set:
                    i = x// box_width
                    j =  y// box_height
                    target_box=grid[i][j]
                    target_box.target = True
                    target_box_set=True
            #start algorithm
            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True
                
            
#fill window with black color
        window.fill((0, 0, 0))

        for i in range(columns):
            for j  in range(rows):
                box=grid[i][j]
                box.draw(window,(60,80,100))#grey blue
                if box.start:
                    box.draw(window,(200,0,0))
                if box.wall:
                    box.draw(window,(150,150,150))
                if box.target:
                    box.draw(window,(200,200,0))
        pygame.display.flip()


main()
# ant colony 
