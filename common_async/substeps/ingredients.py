import asyncio
from common_async.models.ingredients_model import IngredientsModel
from common_async.models.items.ingredients import Eggs, Flour, Milk


async def get_ingredients() -> IngredientsModel:
    milk: Milk = asyncio.create_task(get_milk())
    eggs: Eggs = asyncio.create_task(get_eggs())
    flour: Flour = asyncio.create_task(get_flour())
    return IngredientsModel(await milk, await eggs, await flour)


async def get_milk() -> Milk:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return Milk()


async def get_eggs() -> Eggs:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return Eggs()


async def get_flour() -> Flour:
    # time cost
    await asyncio.sleep(0.1)
    # find and
    return Flour()
