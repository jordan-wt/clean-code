from thespian.actors import Actor, ActorAddress
from aactor.actors.messages import PrepToolsMessage, PrepToolsResponseMessage
from common.models.tools_model import ToolsModel
from common.models.items.tools import (
    MeasuringCups,
    MeasuringSpoons,
    Mixer,
    RubberSpatula,
    Spatula,
)
from common.substeps.tools import (
    get_measuring_cups,
    get_measuring_spoons,
    get_mixer,
    get_rubber_spatula,
    get_spatula,
)


class PrepToolsActor(Actor):
    def __init__(self):
        super().__init__()
        self.prep_requestor: ActorAddress = None
        self.prep_mixer_actor: ActorAddress = None
        self.prep_spatula_actor: ActorAddress = None
        self.prep_rubber_spatula_actor: ActorAddress = None
        self.prep_measuring_cups_actor: ActorAddress = None
        self.prep_measuring_spoons_actor: ActorAddress = None

        self.mixer: Mixer = None
        self.spatula: Spatula = None
        self.rubber_spatula: RubberSpatula = None
        self.measuring_cups: MeasuringCups = None
        self.measuring_spoons: MeasuringSpoons = None

    def check_ready(self):
        if not self.prep_mixer_actor:
            self.prep_mixer_actor = self.createActor(PrepMixerActor)
        if not self.prep_spatula_actor:
            self.prep_spatula_actor = self.createActor(PrepSpatulaActor)
        if not self.prep_rubber_spatula_actor:
            self.prep_rubber_spatula_actor = self.createActor(PrepRubberSpatulaActor)
        if not self.prep_measuring_cups_actor:
            self.prep_measuring_cups_actor = self.createActor(PrepMeasuringCupsActor)
        if not self.prep_measuring_spoons_actor:
            self.prep_measuring_spoons_actor = self.createActor(
                PrepMeasuringSpoonsActor
            )

    def receiveMessage(self, msg, sender):
        self.check_ready()
        if isinstance(msg, PrepToolsMessage):
            self.prep_requestor = sender
            self.send(self.prep_mixer_actor, PrepMixerMessage())
            self.send(self.prep_spatula_actor, PrepSpatulaMessage())
            self.send(self.prep_rubber_spatula_actor, PrepRubberSpatulaMessage())
            self.send(self.prep_measuring_cups_actor, PrepMeasuringCupsMessage())
            self.send(self.prep_measuring_spoons_actor, PrepMeasuringSpoonsMessage())
        elif isinstance(msg, PrepMixerResponseMessage):
            self.mixer = msg.mixer
        elif isinstance(msg, PrepSpatulaResponseMessage):
            self.spatula = msg.spatula
        elif isinstance(msg, PrepRubberSpatulaResponseMessage):
            self.rubber_spatula = msg.rubber_spatula
        elif isinstance(msg, PrepMeasuringCupsResponseMessage):
            self.measuring_cups = msg.measuring_cups
        elif isinstance(msg, PrepMeasuringSpoonsResponseMessage):
            self.measuring_spoons = msg.measuring_spoons
        else:
            raise NotImplementedError()
        if (
            self.mixer
            and self.spatula
            and self.rubber_spatula
            and self.measuring_cups
            and self.measuring_spoons
        ):
            self.send(
                self.prep_requestor,
                PrepToolsResponseMessage(
                    ToolsModel(
                        self.mixer,
                        self.spatula,
                        self.rubber_spatula,
                        self.measuring_cups,
                        self.measuring_spoons,
                    )
                ),
            )


class PrepMixerActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepMixerMessage):
            mixer = get_mixer()
            self.send(sender, PrepMixerResponseMessage(mixer))
        else:
            raise NotImplementedError()


class PrepSpatulaActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepSpatulaMessage):
            spatula = get_spatula()
            self.send(sender, PrepSpatulaResponseMessage(spatula))
        else:
            raise NotImplementedError()


class PrepRubberSpatulaActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepRubberSpatulaMessage):
            rubber_spatula = get_rubber_spatula()
            self.send(sender, PrepRubberSpatulaResponseMessage(rubber_spatula))
        else:
            raise NotImplementedError()


class PrepMeasuringCupsActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepMeasuringCupsMessage):
            measuring_cups = get_measuring_cups()
            self.send(sender, PrepMeasuringCupsResponseMessage(measuring_cups))
        else:
            raise NotImplementedError()


class PrepMeasuringSpoonsActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, PrepMeasuringSpoonsMessage):
            measuring_spoons = get_measuring_spoons()
            self.send(sender, PrepMeasuringSpoonsResponseMessage(measuring_spoons))
        else:
            raise NotImplementedError()


class PrepMixerMessage:
    pass


class PrepMixerResponseMessage:
    def __init__(self, mixer: Mixer) -> None:
        self.mixer = mixer


class PrepSpatulaMessage:
    pass


class PrepSpatulaResponseMessage:
    def __init__(self, spatula: Spatula) -> None:
        self.spatula = spatula


class PrepRubberSpatulaMessage:
    pass


class PrepRubberSpatulaResponseMessage:
    def __init__(self, rubber_spatula: RubberSpatula) -> None:
        self.rubber_spatula = rubber_spatula


class PrepMeasuringCupsMessage:
    pass


class PrepMeasuringCupsResponseMessage:
    def __init__(self, measuring_cups: MeasuringCups) -> None:
        self.measuring_cups = measuring_cups


class PrepMeasuringSpoonsMessage:
    pass


class PrepMeasuringSpoonsResponseMessage:
    def __init__(self, measuring_spoons: MeasuringSpoons) -> None:
        self.measuring_spoons = measuring_spoons
