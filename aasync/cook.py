import asyncio
from common_async.models.items.hardware import Bowl, Skillet
from common_async.models.items.pancake import Pancake
from common_async.models.items.tools import RubberSpatula, Spatula


async def cook(
    skillet: Skillet, mixed: Bowl, rubber_spatula: RubberSpatula, spatula: Spatula
) -> "list[Pancake]":
    tasks = []
    for i in range(mixed.batter.remaining):
        t = cook_one(skillet, mixed, rubber_spatula, spatula)
        tasks.append(asyncio.create_task(t))
    pancakes = await asyncio.gather(*tasks)
    print(f"{mixed.batter.remaining} units of pancake batter remaining")
    return pancakes


async def cook_one(
    skillet: Skillet, mixed: Bowl, rubber_spatula: RubberSpatula, spatula: Spatula
):
    await mixed.pour(skillet, rubber_spatula)
    await spatula.flip(skillet)
    return Pancake()
