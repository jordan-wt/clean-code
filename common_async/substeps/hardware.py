import asyncio
from common_async.models.hardware_model import HardwareModel
from common_async.models.items.hardware import Skillet, Bowl


async def get_hardware() -> HardwareModel:
    skillet: Skillet = asyncio.create_task(get_skillet())
    bowl: Bowl = asyncio.create_task(_get_mixing_bowl())
    return HardwareModel(await skillet, await bowl)


async def get_skillet() -> Skillet:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return Skillet()


async def _get_mixing_bowl() -> Bowl:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return Bowl()
