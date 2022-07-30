from Duck import Duck
from FlyWithWings import FlyWithWings
from Quack import Quack


class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()
        
    def display(self) -> None:
        print("I'm a real Mallard duck")