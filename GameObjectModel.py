import pygame


# Model
class GameObjectModel(pygame.sprite.Sprite):
    def __init__(self, start_x: int, start_y: int, width: int, height: int):
        pygame.sprite.Sprite.__init__(self)
        self.x = start_x
        self.y = start_y
        self.speed = 1
        self.width = width
        self.height = height

    def get_speed(self):
        return self.speed

    def set_speed(self, speed: int):
        self.speed = speed

    def get_position(self):
        return self.x, self.y

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y

    def intersects(self, other):
        return not ((self.x + self.width < other.x) or (self.y + self.height < other.y) or (
                    self.x > other.x + other.width) or (
                            self.y > other.y + self.height))
