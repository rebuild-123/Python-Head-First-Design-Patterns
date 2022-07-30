from Duck import Duck
from FlyNoWay import FlyNoWay
from MuteQuack import MuteQuack


class DecoyDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyNoWay())
        self.setQuackBehavior(MuteQuack())
        
    def display(self) -> None:
        print("I'm a duck Decoy")