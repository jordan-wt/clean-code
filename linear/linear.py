from common.models.items.hardware import Skillet
from common.substeps.hardware import _get_skillet
from linear.mix import mix

def make_pancakes():
    # prep
    skillet: Skillet = _get_skillet()
    skillet.preheat()
    
    mix(skillet)
    