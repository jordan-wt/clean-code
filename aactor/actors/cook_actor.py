from thespian.actors import Actor, ActorAddress
from thespian.troupe import troupe
from aactor.actors.messages import (
    CookPancakesRequestMessage,
    CookedPancakesResponseMessage,
)
from common.models.items.hardware import Bowl, Skillet
from common.models.items.pancake import Pancake
from common.models.items.tools import RubberSpatula, Spatula


class CookActor(Actor):
    def __init__(self):
        super().__init__()
        self.requestor: ActorAddress = None
        self.cook_one_actor: ActorAddress = None
        self.skillet: Skillet = None
        self.expected_flapjacks = -1
        self.pancakes: list[Pancake] = []

    def check_ready(self):
        if not self.cook_one_actor:
            self.cook_one_actor = self.createActor(CookOneActor)

    def preheat(self):
        if not self.skillet:
            raise ValueError("skillet")
        self.skillet.preheat()

    def receiveMessage(self, msg, sender):
        self.check_ready()
        if isinstance(msg, CookPancakesRequestMessage):
            self.requestor = sender
            self.expected_flapjacks = msg.mixed.batter.remaining
            for p in range(msg.mixed.batter.remaining):
                self.send(
                    self.cook_one_actor,
                    CookOnePancakeRequestMessage(
                        self.skillet, msg.mixed, msg.rubber_spatula, msg.spatula
                    ),
                )
        if isinstance(msg, CookOnePancakeResponseMessage):
            self.pancakes.append(msg.pancake)
        if len(self.pancakes) == self.expected_flapjacks:
            self.send(self.requestor, CookedPancakesResponseMessage(self.pancakes))


@troupe(idle_count=10, max_count=10)
class CookOneActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, CookOnePancakeRequestMessage):
            msg.mixed.pour(msg.skillet, msg.rubber_spatula)
            msg.spatula.flip(msg.skillet)
            self.send(sender, CookOnePancakeResponseMessage(Pancake()))


class CookOnePancakeRequestMessage:
    def __init__(
        self,
        skillet: Skillet,
        mixed: Bowl,
        rubber_spatula: RubberSpatula,
        spatula: Spatula,
    ) -> None:
        self.skillet = skillet
        self.mixed = mixed
        self.rubber_spatula = rubber_spatula
        self.spatula = spatula


class CookOnePancakeResponseMessage:
    def __init__(self, pancake: Pancake) -> None:
        self.pancake = pancake
