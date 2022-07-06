import asyncio
from common_async.models.items.batter import Batter
from common_async.models.items.ingredients import Eggs, Flour, Milk


class Skillet:
    async def preheat(self):
        # magic
        await asyncio.sleep(0.1)


class Bowl:
    from common_async.models.items.tools import Mixer, RubberSpatula

    def __init__(self) -> None:
        self.milk: Milk = None
        self.eggs: Eggs = None
        self.flour: Flour = None
        self.batter: Batter = None

    async def sift_in_flour(self, flour: Flour):
        await asyncio.sleep(0.1)
        self.flour = flour

    async def add_wet(self, milk: Milk, eggs: Eggs):
        await asyncio.sleep(0.1)
        self.milk = milk
        self.eggs = eggs

    async def combine(self, mixer: Mixer):
        await asyncio.sleep(0.1)
        self.batter = await mixer.brrr(self.milk, self.eggs, self.flour)

    async def pour(self, skillet: Skillet, rubber_spatula: RubberSpatula):
        await asyncio.sleep(0.1)
        if not self.batter or self.batter.remaining == 0:
            raise ValueError("no batter")
        self.batter.remaining -= 1
