class Towel:
    id: int
    name: str

    def __init__(self, external_params: tuple):
        self.id = external_params[0]
        self.name = external_params[1]
