from ParachuteModel import ParachuteModel


class ParachuteController:
    def __init__(self):
        self.parachute_model = None

    def set_model(self, model: ParachuteModel):
        if model is None:
            raise Exception("Invalid model")
        self.parachute_model = model

    def fall(self):
        """
            at fist i had controller for each parachute, however since we our parachutes are pretty much identical
            i thought of controller more like a monitor(watching  and the parachuter model more like a generator
        """
        for parachute in self.parachute_model.get_parachutes():
            x, y = parachute.get_position()
            parachute.set_position(x, y + parachute.get_speed())
