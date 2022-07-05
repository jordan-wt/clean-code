from common.models.items.tools import (
    MeasuringCups,
    MeasuringSpoons,
    Mixer,
    RubberSpatula,
    Spatula,
)
from common.models.tools_model import ToolsModel


def get_tools() -> ToolsModel:
    mixer: Mixer = get_mixer()
    spatula: Spatula = get_spatula()
    rubber_spatula: RubberSpatula = get_rubber_spatula()
    measuring_cups: MeasuringCups = get_measuring_cups()
    measuring_spoons: MeasuringSpoons = get_measuring_spoons()
    return ToolsModel(mixer, spatula, rubber_spatula, measuring_cups, measuring_spoons)

def get_mixer() -> Mixer:
    # find and
    return Mixer()

def get_spatula() -> Spatula:
    # find and
    return Spatula()

def get_rubber_spatula() -> RubberSpatula:
    # find and
    return RubberSpatula()

def get_measuring_cups() -> MeasuringCups:
    # find and
    return MeasuringCups()

def get_measuring_spoons() -> MeasuringSpoons:
    # find and
    return MeasuringSpoons()