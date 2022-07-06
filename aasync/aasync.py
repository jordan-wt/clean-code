import asyncio
from datetime import datetime
from common_async.models.items.hardware import Bowl
from common_async.models.items.pancake import Pancake
from common_async.models.prep_model import PrepModel
from aasync.cook import cook
from aasync.mix import mix
from aasync.prep import get_prep


def make_pancakes():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(make_pancakes_async())


async def make_pancakes_async():
    print("making async pancakes")
    print(datetime.now())
    prep: PrepModel = await get_prep()
    await prep.hardware.skillet.preheat()
    mixed: Bowl = await mix(prep.ingredients, prep.hardware.bowl, prep.tools)
    cooked: set[Pancake] = await cook(
        prep.hardware.skillet, mixed, prep.tools.rubber_spatula, prep.tools.spatula
    )
    print(f"you have made {len(cooked)} pancakes")
    print(datetime.now())
