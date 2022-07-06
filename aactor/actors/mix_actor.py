from thespian.actors import Actor, ActorAddress
from aactor.actors.messages import (
    MixRequestMessage,
    MixResponseMessage,
)
from common.models.items.hardware import Bowl
from common.models.items.ingredients import Eggs, Flour, Milk
from common.models.items.tools import MeasuringCups, Mixer
from common.models.tools_model import ToolsModel


class MixActor(Actor):
    def __init__(self):
        super().__init__()
        self.requestor: ActorAddress = None
        self.measure_milk_actor: ActorAddress = None
        self.measure_eggs_actor: ActorAddress = None
        self.measure_flour_actor: ActorAddress = None

        self.bowl: Bowl = None
        self.mixer: Mixer = None
        self.measured_milk: Milk = None
        self.counted_eggs: Eggs = None
        self.measured_flour: Flour = None

    def check_ready(self):
        if not self.measure_milk_actor:
            self.measure_milk_actor = self.createActor(MeasureMilkActor)
        if not self.measure_eggs_actor:
            self.measure_eggs_actor = self.createActor(MeasureEggsActor)
        if not self.measure_flour_actor:
            self.measure_flour_actor = self.createActor(MeasureFlourActor)

    def receiveMessage(self, msg, sender):
        self.check_ready()
        if isinstance(msg, MixRequestMessage):
            self.requestor = sender
            self.bowl = msg.bowl
            self.mixer = msg.tools.mixer
            self.send(
                self.measure_milk_actor,
                MeasureMilkMessage(msg.tools.measuring_cups, msg.ingredients.milk),
            )
            self.send(
                self.measure_eggs_actor,
                MeasureEggsMessage(msg.tools, msg.ingredients.eggs),
            )
            self.send(
                self.measure_flour_actor,
                MeasureFlourMessage(msg.tools.measuring_cups, msg.ingredients.flour),
            )
        elif isinstance(msg, MeasureMilkResponseMessage):
            self.measured_milk = msg.measured_milk
        elif isinstance(msg, MeasureEggsResponseMessage):
            self.counted_eggs = msg.counted_eggs
        elif isinstance(msg, MeasureFlourResponseMessage):
            self.measured_flour = msg.measured_flour
        else:
            raise NotImplementedError()
        if self.measured_milk and self.counted_eggs and self.measured_flour:
            self.bowl.sift_in_flour(self.measured_flour)
            self.bowl.add_wet(self.measured_milk, self.counted_eggs)
            self.bowl.combine(self.mixer)
            self.send(self.requestor, MixResponseMessage(self.bowl))


class MeasureMilkActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, MeasureMilkMessage):
            measured_milk = msg.measuring_cups.measure_milk(msg.milk)
            self.send(sender, MeasureMilkResponseMessage(measured_milk))
        else:
            raise NotImplementedError()


class MeasureEggsActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, MeasureEggsMessage):
            counted_eggs = msg.tools.count_eggs(msg.eggs)
            self.send(sender, MeasureEggsResponseMessage(counted_eggs))
        else:
            raise NotImplementedError()

    def count_eggs(eggs: Eggs):
        pass


class MeasureFlourActor(Actor):
    def receiveMessage(self, msg, sender):
        if isinstance(msg, MeasureFlourMessage):
            measured_flour = msg.measuring_cups.measure_flour(msg.flour)
            self.send(sender, MeasureFlourResponseMessage(measured_flour))
        else:
            raise NotImplementedError()


class MeasureMilkMessage:
    def __init__(self, measuring_cups: MeasuringCups, milk: Milk) -> None:
        self.measuring_cups = measuring_cups
        self.milk = milk


class MeasureMilkResponseMessage:
    def __init__(self, measured_milk: Milk) -> None:
        self.measured_milk = measured_milk


class MeasureEggsMessage:
    def __init__(self, tools: ToolsModel, eggs: Eggs) -> None:
        self.tools = tools
        self.eggs = eggs


class MeasureEggsResponseMessage:
    def __init__(self, counted_eggs: Eggs) -> None:
        self.counted_eggs = counted_eggs


class MeasureFlourMessage:
    def __init__(self, measuring_cups: MeasuringCups, flour: Flour) -> None:
        self.measuring_cups = measuring_cups
        self.flour = flour


class MeasureFlourResponseMessage:
    def __init__(self, measured_flour: Flour) -> None:
        self.measured_flour = measured_flour
