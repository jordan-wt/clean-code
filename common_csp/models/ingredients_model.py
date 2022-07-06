from common_csp.models.items.ingredients import Milk, Eggs, Flour


class IngredientsModel:
    def __init__(self, milk: Milk, eggs: Eggs, flour: Flour) -> None:
        self.milk = milk
        self.eggs = eggs
        self.flour = flour
