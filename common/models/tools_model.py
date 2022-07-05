from indexed.models.items.ingredients import Eggs
from indexed.models.items.tools import (
    Mixer,
    Spatula,
    RubberSpatula,
    MeasuringCups,
    MeasuringSpoons,
)


class ToolsModel:
    def __init__(
        self,
        mixer: Mixer,
        spatula: Spatula,
        rubber_spatula: RubberSpatula,
        measuring_cups: MeasuringCups,
        measuring_spoons: MeasuringSpoons,
    ) -> None:
        self.mixer: Mixer = mixer
        self.spatula: Spatula = spatula
        self.rubber_spatula: RubberSpatula = rubber_spatula
        self.measuring_cups: MeasuringCups = measuring_cups
        self.measuring_spoons: MeasuringSpoons = measuring_spoons
    
    def count_eggs(eggs: Eggs):
        # magic
        return eggs
