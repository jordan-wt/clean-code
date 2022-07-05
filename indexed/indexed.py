from indexed.cook import cook
from indexed.mix import mix
from common.models.items.hardware import Bowl
from common.models.items.pancake import Pancake
from common.models.prep_model import PrepModel
from indexed.prep import get_prep


def make_pancakes():
    prep: PrepModel = get_prep()
    prep.hardware.skillet.preheat()
    mixed: Bowl = mix(prep.ingredients, prep.hardware.bowl, prep.tools)
    cooked: list[Pancake] = cook(
        prep.hardware.skillet, mixed, prep.tools.rubber_spatula, prep.tools.spatula
    )
    print(f'you have made  {len(cooked)} pancakes')
