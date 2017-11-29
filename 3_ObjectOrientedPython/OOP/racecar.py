class RaceCar:

    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining -= length*0.125
        self.laps += 1
        print("After {} lap, your fuel level is at {}".format(self.laps, self.fuel_remaining))