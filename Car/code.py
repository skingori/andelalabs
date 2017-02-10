class Car(object):
    """A Car object."""

    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, name='General', model="GM", car_type="saloon"):
        self.name = name
        self.model = model
        self.type = car_type
        self.num_of_doors = 2 if self.name in ('Koenigsegg', 'Porshe') else self.num_of_doors
        self.num_of_wheels = self.num_of_wheels if self.type == 'saloon' else 8

    def is_saloon(self):
        return self.type == 'saloon'

    def drive(self, acc):
        if self.name == 'MAN':
            self.speed = 77
        else:
            self.speed = 1000
        return self
