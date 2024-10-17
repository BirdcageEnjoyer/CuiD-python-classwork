
#UPDATE 1 - added bouncing ball



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
velocityX = 5
velocityY = 3

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
  
    x += velocityX
    y += velocityY

    if x < 0 or x + velocityX > 700:
        velocityX *= -1
    if y < 0 or y + velocityY > 500:
        velocityY *= -1
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(TEAL)
 
    # --- Drawing code should go here
    circle = pygame.draw.circle(screen, (0, 255, 0), [x, y], 15)

    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(120)
 
# Close the window and quit.
pygame.quit()
