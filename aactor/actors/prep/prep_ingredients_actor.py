from thespian.actors import Actor, ActorAddress
from aactor.actors.messages import (
    PrepIngredientsMessage,
    PrepIngredientsResponseMessage,
)
from common.models.ingredients_model import IngredientsModel
from common.models.items.ingredients import Eggs, Flour, Milk
from common.substeps.ingredients import get_eggs, get_flour, get_milk


class PrepIngredientsActor(Actor):
    def __init__(self):
        super().__init__()
        self.prep_requestor: ActorAddress = None
        self.prep_milk_actor: ActorAddress = None
        self.prep_eggs_actor: ActorAddress = None
        self.prep_flour_actor: ActorAddress = None
        self.milk: Milk = None
        self.eggs: Eggs = None
        self.flour: Flour = None

    def check_ready(self):
        if not self.prep_milk_actor:
            self.prep_milk_actor = self.createActor(PrepMilkActor)
        if not self.prep_eggs_actor:
            self.prep_eggs_actor = self.createActor(PrepEggsActor)
        if not self.prep_flour_actor:
            self.prep_flour_actor = self.createActor(PrepFlourActor)

    def receiveMessage(self, msg, sender):
        self.check_ready()
        if isinstance(msg, PrepIngredientsMessage):
            self.prep_requestor = sender
            self.send(self.prep_milk_actor, PrepMilkMessage())
            self.send(self.prep_eggs_actor, PrepEggsMessage())
            self.send(self.prep_flour_actor, PrepFlourMessage())
        elif isinstance(msg, PrepMilkResponseMessage):
            self.milk = msg.milk
        elif isinstance(msg, PrepEggsResponseMessage):
            self.eggs = msg.eggs
        elif isinstance(msg, PrepFlourResponseMessage):
            self.flour = msg.flour
        else:
            raise NotImplementedError()
        if self.milk and self.eggs and self.flour:
            self.send(
                self.prep_requestor,
                PrepIngredientsResponseMessage(
                    IngredientsModel(self.milk, self.eggs, self.flour)
                ),
            )


class PrepMilkActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepMilkMessage):
            milk = get_milk()
            self.send(sender, PrepMilkResponseMessage(milk))
        else:
            raise NotImplementedError()


class PrepEggsActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepEggsMessage):
            eggs = get_eggs()
            self.send(sender, PrepEggsResponseMessage(eggs))
        else:
            raise NotImplementedError()


class PrepFlourActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepFlourMessage):
            flour = get_flour()
            self.send(sender, PrepFlourResponseMessage(flour))
        else:
            raise NotImplementedError()


class PrepMilkMessage:
    pass


class PrepMilkResponseMessage:
    def __init__(self, milk: Milk) -> None:
        self.milk = milk


class PrepEggsMessage:
    pass


class PrepEggsResponseMessage:
    def __init__(self, eggs: Eggs) -> None:
        self.eggs = eggs


class PrepFlourMessage:
    pass


class PrepFlourResponseMessage:
    def __init__(self, flour: Flour) -> None:
        self.flour = flour
