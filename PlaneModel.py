from GameObjectModel import GameObjectModel


class PlaneModel(GameObjectModel):
    def __init__(self, start_x: int, start_y: int, width: int, height: int, allowed_width: int):
        super().__init__(start_x, start_y, width, height)
        self.allowed_width = allowed_width

    def get_allowed_width(self):
        return self.allowed_width
