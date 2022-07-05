from indexed.models.items.batter import Batter
from indexed.models.items.hardware import Skillet
from indexed.models.items.ingredients import Eggs, Flour, Milk


class Mixer:
    def brrr(self, milk: Milk, eggs: Eggs, flour: Flour):
        # magic
        return Batter()


class Spatula:
    def flip(self, skillet: Skillet):
        # magic
        pass


class RubberSpatula:
    pass


class MeasuringCups:
    def measure_milk(self, milk: Milk) -> Milk:
        # magic
        return milk

    def measure_flour(self, flour: Flour) -> Flour:
        # magic
        return flour


class MeasuringSpoons:
    pass
