from thespian.actors import ActorSystem, ActorAddress
from datetime import datetime
from aactor.actors.make_pancakes_actor import MakePancakesActor
from aactor.actors.messages import (
    CookedPancakesResponseMessage,
    MakePancakesMessage,
)


def make_pancakes():
    print("making actor pancakes")
    print(datetime.now())
    acs = ActorSystem("multiprocQueueBase")
    make_pancakes_actor: ActorAddress = acs.createActor(MakePancakesActor)
    result = acs.ask(make_pancakes_actor, MakePancakesMessage())
    if not isinstance(result, CookedPancakesResponseMessage):
        ValueError(f"invalid pancake response: {type(result)}")
    print(f"you have made {len(result.pancakes)} pancakes")
    print(datetime.now())
