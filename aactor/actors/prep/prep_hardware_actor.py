from thespian.actors import Actor, ActorAddress
from aactor.actors.messages import PrepHardwareMessage, PrepHardwareResponseMessage
from common.models.hardware_model import HardwareModel
from common.models.items.hardware import Bowl, Skillet
from common.substeps.hardware import get_skillet, get_mixing_bowl


class PrepHardwareActor(Actor):
    def __init__(self):
        super().__init__()
        self.prep_requestor: ActorAddress = None
        self.prep_skillet_actor: ActorAddress = None
        self.prep_bowl_actor: ActorAddress = None
        self.skillet: Skillet = None
        self.bowl: Bowl = None

    def check_ready(self):
        if not self.prep_skillet_actor:
            self.prep_skillet_actor = self.createActor(PrepSkilletActor)
        if not self.prep_bowl_actor:
            self.prep_bowl_actor = self.createActor(PrepBowlActor)

    def receiveMessage(self, msg, sender):
        self.check_ready()
        if isinstance(msg, PrepHardwareMessage):
            self.prep_requestor = sender
            self.send(self.prep_skillet_actor, PrepSkilletMessage())
            self.send(self.prep_bowl_actor, PrepBowlMessage())
        elif isinstance(msg, PrepSkilletResponseMessage):
            self.skillet = msg.skillet
        elif isinstance(msg, PrepBowlResponseMessage):
            self.bowl = msg.bowl
        else:
            raise NotImplementedError()
        if self.skillet and self.bowl:
            self.send(
                self.prep_requestor,
                PrepHardwareResponseMessage(HardwareModel(self.skillet, self.bowl)),
            )


class PrepSkilletActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepSkilletMessage):
            skillet = get_skillet()
            self.send(sender, PrepSkilletResponseMessage(skillet))
        else:
            raise NotImplementedError()


class PrepBowlActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepBowlMessage):
            bowl = get_mixing_bowl()
            self.send(sender, PrepBowlResponseMessage(bowl))
        else:
            raise NotImplementedError()


class PrepSkilletMessage:
    pass


class PrepSkilletResponseMessage:
    def __init__(self, skillet: Skillet) -> None:
        self.skillet = skillet


class PrepBowlMessage:
    pass


class PrepBowlResponseMessage:
    def __init__(self, bowl: Bowl) -> None:
        self.bowl = bowl
