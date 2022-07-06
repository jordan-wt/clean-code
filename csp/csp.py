from datetime import datetime
from common_csp.models.items.hardware import Bowl
from common_csp.models.items.pancake import Pancake
from common_csp.models.prep_model import PrepModel
from indexed.cook import cook
from indexed.mix import mix
from indexed.prep import get_prep


def make_pancakes():
    print("making indexed pancakes")
    print(datetime.now())
    prep: PrepModel = get_prep()
    prep.hardware.skillet.preheat()
    mixed: Bowl = mix(prep.ingredients, prep.hardware.bowl, prep.tools)
    cooked: set[Pancake] = cook(
        prep.hardware.skillet, mixed, prep.tools.rubber_spatula, prep.tools.spatula
    )
    print(f"you have made {len(cooked)} pancakes")
    print(datetime.now())
