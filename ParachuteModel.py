from ParachuteDescriptor import ParachuteDescriptor


class ParachuteModel:
    def __init__(self):
        self.parachutes = []

    def get_parachutes(self):
        return self.parachutes

    def add_parachute(self, parachute: ParachuteDescriptor):
        self.parachutes.append(parachute)

    def remove_parachute(self, parachute: ParachuteDescriptor):
        self.parachutes.remove(parachute)
