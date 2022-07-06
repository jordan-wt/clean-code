from csp.csp import Channel, process
from common_csp.models.prep_model import PrepModel
from common_csp.substeps.ingredients import get_ingredients
from common_csp.substeps.hardware import get_hardware
from common_csp.substeps.tools import get_tools


@process
def get_prep(chan: Channel) -> PrepModel:
    ingredients = get_ingredients()
    hardware = get_hardware()
    tools = get_tools()
    return PrepModel(ingredients, hardware, tools)
