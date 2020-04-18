from typing import List

from GameObjectModel import GameObjectModel


class BoatModel(GameObjectModel):
    def __init__(self,  start_x: int, start_y: int, width: int, height: int):
        super().__init__(start_x,start_y, width, height)
        self.direction = -1

    def get_direction(self):
        return self.direction

    def set_direction(self, new_direction: int):
        self.direction = new_direction
