import pygame as pg
import pygame.display as pd
import pygame.draw as pdr
import pygame.event as pe
import pygame.font as pf
import pygame.image as pm

pg.init()

# Open a pygame window
win = pd.set_mode((500,500))

# Set the window title to "D&D Manager"
pd.set_caption("D&D Manager")

# Set the window icon to icon.png
icon = pm.load('icon.png')
pd.set_icon(icon)

# Set pygame background color to white
bg_color = (255,255,255)
win.fill(bg_color)

# Draw the text "D&D Manager" on the window
win.blit(pf.Font(None,60).render("D&D Manager",True,(0,255,0)),(100,100))

# Make a new font Helvetica, size 30
font = pf.SysFont("Helvetica", 30)

# Create a button and a bounding box with gray background
buttonPos = (100,200)
button = font.render("Hello",True,(0,255,0))
bbox = button.get_rect()

# Draw the button and gray bounding box at the location of the button
win.blit(button,buttonPos)
pdr.rect(win,(0,0,0),bbox,2)

# Draw the screen
pd.flip()

# Main loop
run = True
while run:
    # Event loop
    for event in pe.get():
        # Quit if the quit button was pressed
        if event.type == pg.QUIT:
            run = False
        # If the "e" key was pressed
        # draw the text "Hello" to the screen
        elif event.type == pg.KEYDOWN and event.key == pg.K_e:
            text = font.render("Hello", True, (0,0,0))
            # Draw the text to the screen
            win.blit(text, (0,0))
        # If a mouse button was pressed
        # Check if it clicked the button
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pg.mouse.get_pos()
            # If the button was clicked
            if button.get_rect(topleft=(100,200)).collidepoint(pos):
                # Print "Hello" to the screen
                text = font.render("Bop", True, (0,0,0))
                # Draw the text to the screen
                win.blit(text, (0,0))
    # Redraw the screen
    pd.flip()
