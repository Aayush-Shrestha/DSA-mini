import pygame
import sys
import numpy as np
import os
import random

# Constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
COLUMNS = 50
ROWS = 50
POINT = 8
ANT = 12
GENER = 9

# Arrays
dist = np.zeros((POINT, POINT))
pref = np.zeros((POINT, POINT))
parr = np.zeros((POINT + 2, ANT + 1))

# Box dimensions
box_width = WINDOW_HEIGHT // COLUMNS
box_height = WINDOW_HEIGHT // ROWS

# Grid setup
grid = [[None] * ROWS for _ in range(COLUMNS)]

# Node setup
NOD = []


class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.node = False  # Node box

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width - 2, box_height - 2))


def initialize_grid():
    for i in range(COLUMNS):
        for j in range(ROWS):
            grid[i][j] = Box(i, j)


def update_pheromones():
    global parr
    for i in range(1, POINT + 1):
        x = int(parr[i - 1, ANT])
        y = int(parr[i, ANT])
        z = pref[x][y]
        z = z * 9
        z = z // 10
        pref[x][y] = z
        pref[y][x] = z


def ant_movement(gen):
    global parr
    i, j, n, n1, x = 0, 0, 0, 0, 0
    a = list(range(1, POINT))
    parr = np.zeros((POINT + 2, ANT + 1))
    for v in range(0, ANT):
        p_temp = pref.copy()
        n = 0
        while n != POINT - 1:
            random.shuffle(a)
            if n1 == n and x < 100:
                x = x + 10
            n1 = n
            for j in a:
                rand = np.random.randint(low=5, high=x)
                if p_temp[i][j] <= rand and p_temp[i][j] != 0:
                    parr[n + 1][v] = j
                    if n != 0:
                        p_temp[:, i] = p_temp[i, :] = 0
                    n = n + 1
                    w = dist[i][j]
                    parr[POINT + 1][v] += w
                    i = j
                    break
        parr[n + 1][v] = 0
        p_temp[i, :] = 0
        p_temp[:, i] = 0
        parr[POINT + 1][v] += dist[i][j]
    l = parr[POINT + 1][0]
    m = 0
    for k in range(1, ANT):
        if l > parr[POINT + 1][k]:
            m = k
    parr[:, ANT] = parr[:, m]


def draw_grid(window):
    for i in range(COLUMNS):
        for j in range(ROWS):
            box = grid[i][j]
            color = (255, 255, 255) if not box.node else (255, 0, 0)  # Node color
            box.draw(window, color)


def draw_path(window, ratio):
    for i in range(1, POINT + 1):
        a = int(parr[i - 1, ANT])
        b = int(parr[i, ANT])
        x1 = ratio * NOD[a].x + 5
        y1 = ratio * NOD[a].y + 5
        x2 = ratio * NOD[b].x + 5
        y2 = ratio * NOD[b].y + 5
        pygame.draw.line(window, (0, 0, 0), (x1, y1), (x2, y2), 4)


def display_instructions(window, font):
    text = font.render("Left Click: Add Node | Spacebar: Run Algorithm | C: Clear | Backspace: Reset", True, (0, 0, 0))
    window.blit(text, (10, 10))


def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    initialize_grid()

    ratio = (WINDOW_HEIGHT / ROWS) // 1

    begin_search = False
    node_n = 0

    font = pygame.font.Font(None, 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if event.button == 1 and node_n < POINT:
                    i = x // box_width
                    j = y // box_height
                    node_box = grid[i][j]
                    node_box.node = True
                    NOD.append(node_box)
                    node_n += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(NOD) >= POINT:
                    random.shuffle(NOD)
                    for i in range(0, POINT - 1):
                        for j in range(i + 1, POINT):
                            dist[i][j] = dist[j][i] = (((NOD[i].x - NOD[j].x) ** 2) +
                                                       (NOD[i].y - NOD[j].y) ** 2) ** 0.5
                            pref[i][j] = pref[j][i] = dist[i][j] // 1
                    for gen in range(0, GENER):
                        ant_movement(gen)
                        print(parr[:, ANT])
                    begin_search = True
                elif event.key == pygame.K_c:
                    main()
                elif event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    os.system('python all.py')

        window.fill((220, 220, 220))
        draw_grid(window)
        if begin_search:
            draw_path(window, ratio)
        display_instructions(window, font)

        pygame.display.flip()


if __name__ == "__main__":
    main()
