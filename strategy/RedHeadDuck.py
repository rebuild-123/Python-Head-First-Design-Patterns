from Duck import Duck
from FlyWithWings import FlyWithWings
from Quack import Quack


class RedHeadDuck(Duck):
    def __init__(self) -> None:
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()
    
    def display(self) -> None:
        print("I'm a real Red Headed duck")