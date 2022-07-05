from common.models.items.hardware import Bowl, Skillet
from common.models.items.ingredients import Eggs, Flour, Milk
from common.models.items.tools import MeasuringCups, MeasuringSpoons, Mixer
from common.substeps.hardware import _get_mixing_bowl
from common.substeps.ingredients import get_eggs, get_flour, get_milk
from common.substeps.tools import get_measuring_cups, get_measuring_spoons, get_mixer
from linear.cook import cook


def mix(skillet: Skillet):
    mixer: Mixer = get_mixer()
    measuring_cups: MeasuringCups = get_measuring_cups()
    measuring_spoons: MeasuringSpoons = get_measuring_spoons()

    bowl: Bowl = _get_mixing_bowl()

    milk: Milk = get_milk()
    eggs: Eggs = get_eggs()
    flour: Flour = get_flour()

    measured_milk = measuring_cups.measure_milk(milk)
    measured_eggs = count_eggs(eggs)
    measured_flour = measuring_cups.measure_flour(flour)

    bowl.sift_in_flour(measured_flour)
    bowl.add_wet(measured_milk, measured_eggs)
    bowl.combine(mixer)

    cook(skillet, bowl)


def count_eggs(eggs: Eggs) -> Eggs:
    # magic
    return eggs
