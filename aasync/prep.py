import asyncio
from common_async.models.prep_model import PrepModel
from common_async.substeps.ingredients import get_ingredients
from common_async.substeps.hardware import get_hardware
from common_async.substeps.tools import get_tools


async def get_prep() -> PrepModel:
    ingredients = asyncio.create_task(get_ingredients())
    hardware = asyncio.create_task(get_hardware())
    tools = asyncio.create_task(get_tools())
    return PrepModel(await ingredients, await hardware, await tools)
