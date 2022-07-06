from common_csp.models.ingredients_model import IngredientsModel
from common_csp.models.hardware_model import HardwareModel
from common_csp.models.tools_model import ToolsModel


class PrepModel:
    def __init__(
        self, ingredients: IngredientsModel, hardware: HardwareModel, tools: ToolsModel
    ) -> None:
        self.ingredients = ingredients
        self.hardware = hardware
        self.tools = tools
