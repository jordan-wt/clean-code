import time
from common.models.items.hardware import Bowl, Skillet
from common.models.items.pancake import Pancake
from common.models.items.tools import RubberSpatula, Spatula
from common.substeps.tools import get_rubber_spatula, get_spatula


def cook(skillet: Skillet, mixed: Bowl):
    rubber_spatula: RubberSpatula = get_rubber_spatula()
    spatula: Spatula = get_spatula()
    pancakes: list[Pancake]
    while mixed.batter.remaining > 0:  #
        mixed.pour(skillet, rubber_spatula)
        time.sleep(1)
        spatula.flip(skillet)
        time.sleep(1)
        pancakes.add(Pancake())
    print(f'you have made  {len(pancakes)} pancakes')
