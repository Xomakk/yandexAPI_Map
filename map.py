import pygame
from geo import download_map


class Map(pygame.sprite.Sprite):
    ZOOM_MAX = 20
    ZOOM_MIN = 1
    PRESS_DELTA = 0.1
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self.ll = [82.924504, 55.030439]
        self.zoom = 3
        self.type = 'map'

        self.update_image()

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] and self.zoom < self.ZOOM_MAX:
            print(123)
            self.zoom += 1
          
        if keys[pygame.K_DOWN] and self.zoom > self.ZOOM_MIN:
            print(234)
            self.zoom -= 1

        self.update_image()
    
    def update_image(self):
        download_map(
            ll=",".join(list(map(str, self.ll))),
            zoom=self.zoom,
            map_type = self.type
        )
        
        self.image = pygame.image.load('map.png').convert()
        self.rect = self.image.get_rect()