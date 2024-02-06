import sys

import pygame
from pygame.locals import QUIT
from map import Map

pygame.init()
DISPLAYSURF = pygame.display.set_mode((450, 450))
pygame.display.set_caption('Hello World!')

map_group = pygame.sprite.Group()
map = Map(map_group)

while True:
    for event in pygame.event.get():
        DISPLAYSURF.fill('white')
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            map.update()

    map_group.draw(DISPLAYSURF, (0, 0))

    pygame.display.update()
