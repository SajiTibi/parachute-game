from PlaneModel import PlaneModel


class PlaneController:

    def __init__(self):
        self.plane_model = None

    def set_plane_model(self, model: PlaneModel):
        if model is None:
            raise Exception("Invalid model")
        self.plane_model = model

    def drive(self):
        x, y = self.plane_model.get_position()
        new_x = (x - self.plane_model.get_speed()) % (self.plane_model.get_allowed_width())
        self.plane_model.set_position(new_x, y)
