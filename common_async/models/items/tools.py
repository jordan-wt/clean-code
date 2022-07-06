import asyncio
from common_async.models.items.batter import Batter
from common_async.models.items.hardware import Skillet
from common_async.models.items.ingredients import Eggs, Flour, Milk


class Mixer:
    async def brrr(self, milk: Milk, eggs: Eggs, flour: Flour):
        await asyncio.sleep(0.1)
        return Batter()


class Spatula:
    async def flip(self, skillet: Skillet):
        await asyncio.sleep(0.1)


class RubberSpatula:
    pass


class MeasuringCups:
    async def measure_milk(self, milk: Milk) -> Milk:
        await asyncio.sleep(0.1)
        return milk

    async def measure_flour(self, flour: Flour) -> Flour:
        await asyncio.sleep(0.1)
        return flour


class MeasuringSpoons:
    pass
