class User:
    id: int
    first_name: str
    last_name: str
    birthdate: str

    def __init__(self, external_entity: tuple):
        self.id = external_entity[0]
        self.first_name = external_entity[1]
        self.last_name = external_entity[2]
        self.birthdate = external_entity[3]

    def toString(self):
        return f'{self.id}, {self.first_name}, {self.last_name}, {self.birthdate}'