from common.models.ingredients_model import IngredientsModel
from common.models.hardware_model import HardwareModel
from common.models.tools_model import ToolsModel


class PrepModel:
    def __init__(
        self, ingredients: IngredientsModel, hardware: HardwareModel, tools: ToolsModel
    ) -> None:
        self.ingredients = ingredients
        self.hardware = hardware
        self.tools = tools
