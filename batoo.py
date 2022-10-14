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
    def draw(self, win, color):
        pygame.draw.rect(win, color,(self.x * box_width,self.y* box_height,box_width-2, box_height-2))

#grid
for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Box(i,j))
    grid.append(arr)


def main():
    while True:
        for event in pygame.event.get():
            # Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
#fill window with black color
        window.fill((0, 0, 0))

        for i in range(columns):
            for j  in range(rows):
                box=grid[i][j]
                box.draw(window,(60,80,100))#grey blue
        pygame.display.flip()


main()