class Airplane:

    def __init__(self, mark, model, year, max_speed):
        self.mark = mark
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.__is_flying = False

    @property
    def take_off(self):
        self.is_flying = True
        take_off_announcement = f'{self.mark} {self.model} was take off.'
        return take_off_announcement

    def fly(self, distance):
        self.odometer += distance
        fly_announcement = f'{self.mark} {self.model} will fly {self.odometer}km at a max speed {self.max_speed}km/h.'
        return fly_announcement

    @property
    def land(self):
        self.is_flying = False
        land_announcement = f'{self.mark} {self.model} has landed.'
        return land_announcement



eagle = Airplane('Як', '141', 2003, 1800)
print(eagle.land)
print(eagle.fly(2000))
print(eagle.take_off)



