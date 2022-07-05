from common.models.hardware_model import HardwareModel
from common.models.items.hardware import Skillet, Bowl


def get_hardware() -> HardwareModel:
    skillet: Skillet = _get_skillet()
    bowl: Bowl = _get_mixing_bowl()
    return HardwareModel(skillet, bowl)


def _get_skillet() -> Skillet:
    # find and
    return Skillet()


def _get_mixing_bowl() -> Bowl:
    # find and
    return Bowl()
