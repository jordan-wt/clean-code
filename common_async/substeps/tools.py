import asyncio
from common_async.models.items.tools import (
    MeasuringCups,
    MeasuringSpoons,
    Mixer,
    RubberSpatula,
    Spatula,
)
from common_async.models.tools_model import ToolsModel


async def get_tools() -> ToolsModel:
    mixer: Mixer = asyncio.create_task(get_mixer())
    spatula: Spatula = asyncio.create_task(get_spatula())
    rubber_spatula: RubberSpatula = asyncio.create_task(get_rubber_spatula())
    measuring_cups: MeasuringCups = asyncio.create_task(get_measuring_cups())
    measuring_spoons: MeasuringSpoons = asyncio.create_task(get_measuring_spoons())
    return ToolsModel(
        await mixer,
        await spatula,
        await rubber_spatula,
        await measuring_cups,
        await measuring_spoons,
    )


async def get_mixer() -> Mixer:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return Mixer()


async def get_spatula() -> Spatula:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return Spatula()


async def get_rubber_spatula() -> RubberSpatula:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return RubberSpatula()


async def get_measuring_cups() -> MeasuringCups:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return MeasuringCups()


async def get_measuring_spoons() -> MeasuringSpoons:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return MeasuringSpoons()
