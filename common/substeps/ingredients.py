from common.models.ingredients_model import IngredientsModel
from common.models.items.ingredients import Eggs, Flour, Milk


def get_ingredients() -> IngredientsModel:
    milk: Milk = get_milk()
    eggs: Eggs = get_eggs()
    flour: Flour = get_flour()
    return IngredientsModel(milk, eggs, flour)


def get_milk() -> Milk:
    # find and
    return Milk()


def get_eggs() -> Eggs:
    # find and
    return Eggs()


def get_flour() -> Flour:
    # find and
    return Flour()
