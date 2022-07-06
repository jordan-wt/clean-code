import time
from common_csp.models.ingredients_model import IngredientsModel
from common_csp.models.items.ingredients import Eggs, Flour, Milk


def get_ingredients() -> IngredientsModel:
    milk: Milk = get_milk()
    eggs: Eggs = get_eggs()
    flour: Flour = get_flour()
    return IngredientsModel(milk, eggs, flour)


def get_milk() -> Milk:
    # time cost
    time.sleep(0.1)
    # find and
    return Milk()


def get_eggs() -> Eggs:
    # time cost
    time.sleep(0.1)
    # find and
    return Eggs()


def get_flour() -> Flour:
    # time cost
    time.sleep(0.1)
    # find and
    return Flour()
