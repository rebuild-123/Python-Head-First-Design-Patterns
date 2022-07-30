from Duck import Duck
from FlyNoWay import FlyNoWay
from Quack import Quack


class ModelDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Quack()
        
    def display(self) -> None:
        print("I'm a model duck")