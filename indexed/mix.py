from common.models.ingredients_model import IngredientsModel
from common.models.items.hardware import Bowl
from common.models.tools_model import ToolsModel


def mix(ingredients: IngredientsModel, bowl: Bowl, tools: ToolsModel) -> Bowl:
    measured: IngredientsModel = _measure(ingredients, tools)
    bowl.sift_in_flour(measured.flour)
    bowl.add_wet(ingredients.milk, ingredients.eggs)
    bowl.combine(tools.mixer)
    return bowl


def _measure(ingredients: IngredientsModel, tools: ToolsModel) -> IngredientsModel:
    milk = tools.measuring_cups.measure_milk(ingredients.milk)
    eggs = tools.count_eggs(ingredients.eggs)
    flour = tools.measuring_cups.measure_flour(ingredients.flour)
    return IngredientsModel(milk, eggs, flour)
