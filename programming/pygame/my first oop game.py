import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

class Bullet:
    def __init__(self, x, y, colour) -> None:
        self.x = x
        self.y = y
        self.colour = colour

    def __repr__(self) -> str:
        return f'x:{self.x},y:{self.y},colour:{self.colour}'
    

bullet1 = Bullet(10, 10, RED)

print(bullet1.__repr__())

class Block(pygame.sprite.Sprite):
    def __init__(self, colour, height, width) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()


# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)



pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

blockList = pygame.sprite.Group()
allSpritesList = pygame.sprite.Group()


for i in range(50):
    block = Block(BLACK, 20, 15)
    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])

    blockList.add(block)
    allSpritesList.add(block)



# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    allSpritesList.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()