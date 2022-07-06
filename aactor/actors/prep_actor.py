from thespian.actors import Actor, ActorAddress
from aactor.actors.messages import (
    PrepHardwareMessage,
    PrepHardwareResponseMessage,
    PrepIngredientsMessage,
    PrepIngredientsResponseMessage,
    PrepRequestMessage,
    PrepResponseMessage,
    PrepToolsMessage,
    PrepToolsResponseMessage,
)
from aactor.actors.prep.prep_hardware_actor import PrepHardwareActor
from aactor.actors.prep.prep_ingredients_actor import PrepIngredientsActor
from aactor.actors.prep.prep_tools_actor import PrepToolsActor
from common.models.hardware_model import HardwareModel
from common.models.ingredients_model import IngredientsModel
from common.models.prep_model import PrepModel
from common.models.tools_model import ToolsModel


class PrepActor(Actor):
    def __init__(self):
        super().__init__()
        self.requestor: ActorAddress = None
        self.prep_ingredients_actor: ActorAddress = None
        self.prep_hardware_actor: ActorAddress = None
        self.prep_tools_actor: ActorAddress = None
        self.ingredients: IngredientsModel = None
        self.hardware: HardwareModel = None
        self.tools: ToolsModel = None

    def check_ready(self):
        if not self.prep_ingredients_actor:
            self.prep_ingredients_actor = self.createActor(PrepIngredientsActor)
        if not self.prep_hardware_actor:
            self.prep_hardware_actor = self.createActor(PrepHardwareActor)
        if not self.prep_tools_actor:
            self.prep_tools_actor = self.createActor(PrepToolsActor)

    def receiveMessage(self, msg, sender):
        self.check_ready()
        if isinstance(msg, PrepRequestMessage):
            self.requestor = sender
            self.send(self.prep_ingredients_actor, PrepIngredientsMessage())
            self.send(self.prep_hardware_actor, PrepHardwareMessage())
            self.send(self.prep_tools_actor, PrepToolsMessage())
        elif isinstance(msg, PrepIngredientsResponseMessage):
            self.ingredients = msg.ingredients
        elif isinstance(msg, PrepHardwareResponseMessage):
            self.hardware = msg.hardware
        elif isinstance(msg, PrepToolsResponseMessage):
            self.tools = msg.tools
        else:
            raise NotImplementedError()
        if self.ingredients and self.hardware and self.tools:
            self.send(
                self.requestor,
                PrepResponseMessage(
                    PrepModel(self.ingredients, self.hardware, self.tools)
                ),
            )
