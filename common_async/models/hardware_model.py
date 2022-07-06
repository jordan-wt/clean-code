from common_async.models.items.hardware import Skillet, Bowl


class HardwareModel:
    def __init__(self, skillet: Skillet, bowl: Bowl) -> None:
        self.skillet = skillet
        self.bowl = bowl
