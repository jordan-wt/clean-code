import time
from common_csp.models.items.batter import Batter
from common_csp.models.items.ingredients import Eggs, Flour, Milk


class Skillet:
    def __init__(self) -> None:
        self.preheated = False

    def preheat(self):
        # magic
        time.sleep(0.1)
        self.preheated = True


class Bowl:
    from common_csp.models.items.tools import Mixer, RubberSpatula

    def __init__(self) -> None:
        self.milk: Milk = None
        self.eggs: Eggs = None
        self.flour: Flour = None
        self.batter: Batter = None

    def sift_in_flour(self, flour: Flour):
        time.sleep(0.1)
        self.flour = flour

    def add_wet(self, milk: Milk, eggs: Eggs):
        time.sleep(0.1)
        self.milk = milk
        self.eggs = eggs

    def combine(self, mixer: Mixer):
        time.sleep(0.1)
        self.batter = mixer.brrr(self.milk, self.eggs, self.flour)

    def pour(self, skillet: Skillet, rubber_spatula: RubberSpatula):
        time.sleep(0.1)
        if not self.batter or self.batter.remaining == 0:
            raise ValueError("no batter")
        self.batter.remaining -= 1
