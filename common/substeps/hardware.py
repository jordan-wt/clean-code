import time
from common.models.hardware_model import HardwareModel
from common.models.items.hardware import Skillet, Bowl


def get_hardware() -> HardwareModel:
    skillet: Skillet = get_skillet()
    bowl: Bowl = get_mixing_bowl()
    return HardwareModel(skillet, bowl)


def get_skillet() -> Skillet:
    # time cost
    time.sleep(0.1)
    # find and
    return Skillet()


def get_mixing_bowl() -> Bowl:
    # time cost
    time.sleep(0.1)
    # find and
    return Bowl()
