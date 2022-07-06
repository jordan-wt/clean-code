from common_csp.models.ingredients_model import IngredientsModel
from common_csp.models.items.hardware import Bowl
from common_csp.models.items.ingredients import Eggs, Flour, Milk
from common_csp.models.items.tools import Mixer
from common_csp.models.tools_model import ToolsModel


def mix(ingredients: IngredientsModel, bowl: Bowl, tools: ToolsModel) -> Bowl:
    measured: IngredientsModel = _measure(ingredients, tools)
    _sift(bowl, measured.flour)
    _add_wet(bowl, ingredients.milk, ingredients.eggs)
    _combine(bowl, tools.mixer)
    return bowl


def _measure(ingredients: IngredientsModel, tools: ToolsModel) -> IngredientsModel:
    milk = tools.measuring_cups.measure_milk(ingredients.milk)
    eggs = tools.count_eggs(ingredients.eggs)
    flour = tools.measuring_cups.measure_flour(ingredients.flour)
    return IngredientsModel(milk, eggs, flour)


def _sift(bowl: Bowl, flour: Flour):
    bowl.sift_in_flour(flour)


def _add_wet(bowl: Bowl, milk: Milk, eggs: Eggs):
    bowl.add_wet(milk, eggs)


def _combine(bowl: Bowl, mixer: Mixer):
    bowl.combine(mixer)
