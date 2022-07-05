from indexed.models.items.batter import Batter
from indexed.models.items.ingredients import Eggs, Flour, Milk
from indexed.models.items.tools import Mixer, RubberSpatula


class Skillet:
    def preheat(self):
        # magic
        pass


class Bowl:
    def __init__(self) -> None:
        self.milk: Milk = None
        self.eggs: Eggs = None
        self.flour: Flour = None
        self.batter: Batter = None

    def sift_in_flour(self, flour: Flour):
        # magic
        self.flour = flour

    def add_wet(self, milk: Milk, eggs: Eggs):
        self.milk = milk
        self.eggs = eggs

    def combine(self, mixer: Mixer):
        self.batter = mixer.brrr(self.milk, self.eggs, self.flour)

    def pour(self, skillet: Skillet, rubber_spatula: RubberSpatula):
        if not self.batter or self.batter.remaining == 0:
            ValueError("no batter")
        self.batter.remaining -= 1
        # magic
