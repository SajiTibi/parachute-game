from typing import List

import pygame

from ParachuteDescriptor import ParachuteDescriptor


class ParachuteView:
    def __init__(self, display: pygame.Surface, img: pygame.Surface, debug_mode=True):
        self.img = img
        self.display_surface = display
        self.debug_mode = debug_mode

    def draw(self, models: List[ParachuteDescriptor]):
        for model in models:
            self.display_surface.blit(self.img, (model.x, model.y))
            if self.debug_mode:
                pygame.draw.rect(self.display_surface, (1, 0, 0), (model.x, model.y, model.width, model.height), 2)
