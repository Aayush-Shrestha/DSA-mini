import pygame
import os
import pygame_widgets
from pygame_widgets.button import Button

def now(x):
    pygame.quit()
    if x == 1 :
        os.system('python ACO2.py')
    elif x == 2 :
        os.system('python A_star.py')
    elif x == 3 :
        os.system('python Dijkstra.py')
# Set up Pygame
pygame.init()
win = pygame.display.set_mode((700, 700))

# Creates the button with optional parameters
button1 = Button(
    # Mandatory Parameters
    win,  # Surface to place button on
    200,  # X-coordinate of top left corner
    100,  # Y-coordinate of top left corner
    300,  # Width
    100,  # Height

    # Optional Parameters
    text='Ant Colony',  # Text to display
    fontSize=50,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
    hoverColour=(150, 0, 0),  # Colour of button when being hovered over
    #pressedColour=(0, 200, 20),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: now(1)  # Function to call when clicked on
)
button2 = Button(

    win,  # Surface to place button on
    200,  # X-coordinate of top left corner
    300,  # Y-coordinate of top left corner
    300,  # Width
    100,  # Height

    text='A-Star',  # Text to display
    fontSize=50,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
    hoverColour=(150, 0, 0),  # Colour of button when being hovered over
    #pressedColour=(0, 200, 20),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: now(2)  # Function to call when clicked on
)
button3 = Button(

    win,  # Surface to place button on
    200,  # X-coordinate of top left corner
    500,  # Y-coordinate of top left corner
    300,  # Width
    100,  # Height

    text='Dijkstra',  # Text to display
    fontSize=50,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
    hoverColour=(150, 0, 0),  # Colour of button when being hovered over
    #pressedColour=(0, 200, 20),  # Colour of button when being clicked
    radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: now(3)  # Function to call when clicked on
)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((100, 100, 100))

    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()


