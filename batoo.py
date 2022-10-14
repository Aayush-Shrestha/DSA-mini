from tkinter import messagebox, Tk
import pygame
import sys

window_width = 600
window_height = 600

window = pygame.display.set_mode((window_width, window_height))


def main():
    while True:
        for event in pygame.event.get():
            # Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #

        window.fill((0, 0, 0))

        pygame.display.flip()


main()