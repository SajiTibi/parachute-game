from BoatModel import BoatModel


class BoatDriver:
    def __init__(self):
        self.boat_model = None

    def set_model(self, model: BoatModel):
        if model is None:
            raise Exception("Invalid model")
        self.boat_model = model

    def drive(self, direction):
        x, y = self.boat_model.get_position()
        new_x = x + direction
        self.boat_model.set_position(new_x, y)
        if direction != self.boat_model.get_direction():
            self.boat_model.set_direction( direction)
