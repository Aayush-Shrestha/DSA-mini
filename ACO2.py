import pygame
import sys
import numpy as np
import os

def main():
    window_width = 700
    window_height = 700

    window = pygame.display.set_mode((window_width, window_height))

    columns = 50
    rows =  50

    point = 7
    ant = 6
    gener = 6

    dist = np.zeros((point,point))
    pref = np.zeros((point,point))
    parr = np.zeros((point+2,ant+1))

    box_width = window_height//columns
    box_height = window_height//rows

    grid = []#empty array

    ratio = (window_height/rows)//1

    class Box:
        def __init__(self,i,j):
            self.x = i
            self.y = j
            self.node=False # node box
            
        def draw(self, win, color):
            pygame.draw.rect(win, color,(self.x * box_width,self.y* box_height,box_width-2, box_height-2))
            
    NOD = [] #array of nodes

    #grid
    for i in range(columns):
        arr = []
        for j in range(rows):
            arr.append(Box(i,j))
        grid.append(arr)
    def pupdate():
        global parr

        for i in range(1,point+1):    
            x= int(parr[i-1,ant])
            y= int(parr[i,ant])
            z=pref[x][y]
            z=z*8
            z=z//10
            pref[x][y]=z
            pref[y][x]=z


    def Astart(gen):
        i=0
        j=0
        n=0
        global parr
        parr = np.zeros((point+2,ant+1))
        for v in range(0,ant):
            p_temp=pref.copy()
            n=0
            while n!=point:
                l=1
                if n==point-1:
                    l=0
                for j in range(l,point):
                    rand =  np.random.randint(low=1, high= 40)
                    if p_temp[i][j]<=rand and  p_temp[i][j] !=0:
                        parr[n+1][v]=j
                        if n!=0:
                            p_temp[i,:]=0
                            p_temp[:,i]=0
                        n=n+1
                        w=dist[i][j]
                        parr[point+1][v] +=w
                        i=j
                        break
                    
        l= parr[point+1][0]    
        m=0    
        for k in range(1,ant):
            if l>parr[point+1][k]:
                m=k
        parr[:,ant]= parr[:,m]      
        
    def alg():
        global parr
        begin_search = False #start algorithm
        node_box_set=False
        node_n = 0
        while True:
            for event in pygame.event.get():
                # Quit Window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #mouse commands capture mouse position
                elif event.type == pygame.MOUSEBUTTONUP:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    
                    if  event.button==1 and node_n<point:
                        i = x// box_width
                        j =  y// box_height
                        node_box=grid[i][j]
                        node_box.node = True
                        node_box_set=True
                        NOD.append(node_box)
                        node_n +=1
                #start algorithm
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_SPACE and len(NOD)>=point:
                        for i in range(0,point-1):
                            for j in range(i+1,point):
                                dist[i][j] = dist[j][i]=(((NOD[i].x-NOD[j].x)**2) +  (NOD[i].y-NOD[j].y)**2)**.5 
                                pref[i][j] = pref[j][i] = dist[i][j] //1     
                        for gen in range(0, gener ):
                            Astart(gen)
                        begin_search=True
                    elif event.key == pygame.K_c:
                        main()
                    elif event.key == pygame.K_BACKSPACE:
                        pygame.quit()
                        os.system('python all.py')
                    
                    
    #fill window with black color
            window.fill((0, 0, 0))

            for i in range(columns):
                for j  in range(rows):
                    box=grid[i][j]
                    box.draw(window,(60,80,100))#grey blue bg
                    if box.node:
                        box.draw(window,(150,000,150))#node color
            if begin_search==True:
                #display path
                for i in range(1,point+1):
                    a = int(parr[i-1,ant])
                    b = int(parr[i,ant])
                    x1 = ratio*NOD[a].x + 1
                    y1 = ratio*NOD[a].y + 1
                    x2 = ratio*NOD[b].x + 1
                    y2 = ratio*NOD[b].y + 1
                    
                    pygame.draw.line(window,(200,200,200), (x1, y1), (x2, y2),4)
            pygame.display.flip()

    alg()
main()