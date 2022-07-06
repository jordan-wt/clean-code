from common.models.hardware_model import HardwareModel
from common.models.ingredients_model import IngredientsModel
from common.models.items.hardware import Bowl, Skillet
from common.models.items.tools import RubberSpatula, Spatula
from common.models.prep_model import PrepModel
from common.models.tools_model import ToolsModel
from common_async.models.items.pancake import Pancake


class MakePancakesMessage:
    pass


class PrepRequestMessage:
    pass


class PrepResponseMessage:
    def __init__(self, prep: PrepModel) -> None:
        self.prep = prep


class PrepIngredientsMessage:
    pass


class PrepIngredientsResponseMessage:
    def __init__(self, ingredients: IngredientsModel) -> None:
        self.ingredients = ingredients


class PrepHardwareMessage:
    pass


class PrepHardwareResponseMessage:
    def __init__(self, hardware: HardwareModel) -> None:
        self.hardware = hardware


class PrepToolsMessage:
    pass


class PrepToolsResponseMessage:
    def __init__(self, tools: ToolsModel) -> None:
        self.tools = tools


class MixRequestMessage:
    def __init__(
        self, ingredients: IngredientsModel, bowl: Bowl, tools: ToolsModel
    ) -> None:
        self.ingredients = ingredients
        self.bowl = bowl
        self.tools = tools


class MixResponseMessage:
    def __init__(self, mixed: Bowl) -> None:
        self.mixed = mixed


class CookPreheatRequestMessage:
    def __init__(self, skillet: Skillet) -> None:
        self.skillet = skillet


class CookPancakesRequestMessage:
    def __init__(
        self, mixed: Bowl, rubber_spatula: RubberSpatula, spatula: Spatula
    ) -> None:
        self.mixed = mixed
        self.rubber_spatula = rubber_spatula
        self.spatula = spatula


class CookedPancakesResponseMessage:
    def __init__(self, pancakes: list[Pancake]) -> None:
        self.pancakes = pancakes
