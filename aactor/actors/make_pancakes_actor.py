from thespian.actors import Actor, ActorAddress
from aactor.actors.cook_actor import CookActor
from aactor.actors.messages import (
    CookPancakesRequestMessage,
    CookPreheatRequestMessage,
    CookedPancakesResponseMessage,
    MakePancakesMessage,
    MixRequestMessage,
    MixResponseMessage,
    PrepRequestMessage,
    PrepResponseMessage,
)
from aactor.actors.mix_actor import MixActor
from aactor.actors.prep_actor import PrepActor
from common.models.items.hardware import Bowl
from common.models.items.pancake import Pancake

from common.models.prep_model import PrepModel


class MakePancakesActor(Actor):
    def __init__(self):
        super().__init__()
        self.origin: ActorAddress = None
        self.prep_actor: ActorAddress = None
        self.mix_actor: ActorAddress = None
        self.cook_actor: ActorAddress = None
        self.prep: PrepModel = None
        self.mixed: Bowl = None
        self.cooked: list[Pancake] = None

    def check_ready(self):
        if not self.prep_actor:
            self.prep_actor = self.createActor(PrepActor)
        if not self.mix_actor:
            self.mix_actor = self.createActor(MixActor)
        if not self.cook_actor:
            self.cook_actor = self.createActor(CookActor)

    def receiveMessage(self, msg, sender):
        self.check_ready()
        if isinstance(msg, MakePancakesMessage):
            self.origin = sender
            self.send(self.prep_actor, PrepRequestMessage())
            return
        if isinstance(msg, PrepResponseMessage):
            self.prep = msg.prep
            self.send(
                self.cook_actor, CookPreheatRequestMessage(self.prep.hardware.skillet)
            )
            self.send(
                self.mix_actor,
                MixRequestMessage(
                    self.prep.ingredients, self.prep.hardware.bowl, self.prep.tools
                ),
            )
        if isinstance(msg, MixResponseMessage):
            self.mixed = msg.mixed
            self.send(
                self.cook_actor,
                CookPancakesRequestMessage(
                    self.mixed, self.prep.tools.rubber_spatula, self.prep.tools.spatula
                ),
            )
        if isinstance(msg, CookedPancakesResponseMessage):
            self.send(self.origin, msg)
