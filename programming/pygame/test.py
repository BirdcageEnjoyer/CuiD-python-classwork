import pygame
pygame.init()
done = False
clock = pygame.time.Clock()
size = (700, 500)
screen = pygame.display.set_mode(size)
title = pygame.display.set_caption("game1")


WHITE = (255, 255, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


screen.fill(WHITE)
pygame.display.flip()
clock.tick(60)

pygame.quit()