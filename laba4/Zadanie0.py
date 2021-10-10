import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen.fill(WHITE)
pygame.display.set_caption("My program")
pygame.display.flip()

circle(screen, (240, 240, 50), (250, 200), 100)
circle(screen, BLACK, (250, 200), 100, 1)

circle(screen, (255, 100, 220), (290, 190), 30)
circle(screen, (255, 100, 220), (210, 190), 30)
circle(screen, (190, 130, 140), (290, 190), 30, 1)
circle(screen, (190, 130, 140), (210, 190), 30, 1)

pygame.draw.line(screen, BLACK, (260, 160), (310, 140), 12)
pygame.draw.line(screen, BLACK, (240, 160), (190, 140), 12)

circle(screen, BLACK, (290, 190), 17)
circle(screen, BLACK, (210, 190), 17)

pygame.draw.rect(screen, (0, 0, 0), ((230, 250), (70, 10)))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


