from common.models.prep_model import PrepModel
from common.substeps.ingredients import get_ingredients
from common.substeps.hardware import get_hardware
from common.substeps.tools import get_tools


def get_prep() -> PrepModel:
    ingredients = get_ingredients()
    hardware = get_hardware()
    tools = get_tools()
    return PrepModel(ingredients, hardware, tools)
