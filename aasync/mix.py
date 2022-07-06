import asyncio
from common_async.models.ingredients_model import IngredientsModel
from common_async.models.items.hardware import Bowl
from common_async.models.tools_model import ToolsModel


async def mix(ingredients: IngredientsModel, bowl: Bowl, tools: ToolsModel) -> Bowl:
    measured: IngredientsModel = await _measure(ingredients, tools)
    await bowl.sift_in_flour(measured.flour)
    await bowl.add_wet(ingredients.milk, ingredients.eggs)
    await bowl.combine(tools.mixer)
    return bowl


async def _measure(
    ingredients: IngredientsModel, tools: ToolsModel
) -> IngredientsModel:
    milk = asyncio.create_task(tools.measuring_cups.measure_milk(ingredients.milk))
    eggs = asyncio.create_task(tools.count_eggs(ingredients.eggs))
    flour = asyncio.create_task(tools.measuring_cups.measure_flour(ingredients.flour))
    return IngredientsModel(await milk, await eggs, await flour)
