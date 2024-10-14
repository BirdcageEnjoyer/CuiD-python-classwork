


# Pygame base template for opening a window
 
#  Sample Python/Pygame Programs
#  Simpson College Computer Science
#  http://programarcadegames.com/
#  http://simpson.edu/computer-science/
 
#  Explanation video: http://youtu.be/vRB_983kUMc

 
import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TEAL = (51, 255, 255)
x = 1
y = 1
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
canvas_size = (32*700, 32*500)
gravity = 1
initialYVel = -100
initialXVel = -110
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
  

    
    x+=1
    y+=1
    if x >= 600 and y >= 400:
        x = 1
        y = 1
    
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(TEAL)
 
    # --- Drawing code should go here
    pygame.draw.circle(screen, (0, 255, 0), [x, y], 100)
    pygame.draw.rect(screen, (0, 255, 0), [0, 400, 700, 100])
    pygame.draw.rect(screen, (255, 0, 255), [400, 250, 200, 150])
    pygame.draw.line(screen, (0, 0, 0), [350, 250], [500, 180])
    pygame.draw.line(screen, (0, 0, 0), [500, 180], [650, 250])
    pygame.draw.line(screen, (0, 0, 0), [350, 250], [650, 250])
    
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(120)
 
# Close the window and quit.
pygame.quit()
