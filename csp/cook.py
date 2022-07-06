from common_csp.models.items.hardware import Bowl, Skillet
from common_csp.models.items.pancake import Pancake
from common_csp.models.items.tools import RubberSpatula, Spatula


def cook(
    skillet: Skillet, mixed: Bowl, rubber_spatula: RubberSpatula, spatula: Spatula
) -> "list[Pancake]":
    pancakes: list[Pancake] = []
    while mixed.batter.remaining > 0:  #
        mixed.pour(skillet, rubber_spatula)
        spatula.flip(skillet)
        pancakes.append(Pancake())
    print(f"{mixed.batter.remaining} units of pancake batter remaining")
    return pancakes
