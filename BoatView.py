import pygame

from BoatModel import BoatModel


class BoatView:
    def __init__(self, display: pygame.Surface, img: pygame.Surface, debug_mode=True):
        self.img = img
        self.display_surface = display
        self.debug_mode = debug_mode
        self.last_direction = None

    def draw(self, model: BoatModel):
        if self.last_direction is None:
            self.last_direction = model.direction
        if self.last_direction != model.direction:
            self.last_direction = model.direction
            self.img = pygame.transform.flip(self.img, True, False)

        self.display_surface.blit(self.img, (model.x, model.y))
        if self.debug_mode:
            pygame.draw.rect(self.display_surface, (1, 0, 0), (model.x, model.y, model.width, model.height), 2)
