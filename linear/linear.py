from datetime import datetime
from common.models.items.hardware import Skillet
from common.substeps.hardware import get_skillet
from linear.mix import mix


def make_pancakes():
    print("making linear pancakes")
    print(datetime.now())

    skillet: Skillet = get_skillet()
    skillet.preheat()

    mix(skillet)
