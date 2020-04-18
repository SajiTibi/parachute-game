from typing import List

from GameObjectModel import GameObjectModel


class ParachuteDescriptor(GameObjectModel):
    def __init__(self, start_x: int, start_y: int,width:int,height:int):
        super().__init__(start_x,start_y,width,height)

