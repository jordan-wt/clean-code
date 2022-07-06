import time
from common_csp.models.items.batter import Batter
from common_csp.models.items.hardware import Skillet
from common_csp.models.items.ingredients import Eggs, Flour, Milk


class Mixer:
    def brrr(self, milk: Milk, eggs: Eggs, flour: Flour):
        time.sleep(0.1)
        return Batter()


class Spatula:
    def flip(self, skillet: Skillet):
        time.sleep(0.1)


class RubberSpatula:
    pass


class MeasuringCups:
    def measure_milk(self, milk: Milk) -> Milk:
        time.sleep(0.1)
        return milk

    def measure_flour(self, flour: Flour) -> Flour:
        time.sleep(0.1)
        return flour


class MeasuringSpoons:
    pass
