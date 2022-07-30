from Duck import Duck
from FlyBehavior import FlyBehavior
from FlyNoWay import FlyNoWay
from QuackBehavior import QuackBehavior
from Squeak import Squeak


class RubberDuck(Duck):
    # def __init__(self) -> None:
    #     self.flyBehavior = FlyNoWay()
    #     # self.quackBehavior = Squeak()
    #     self.quackBehavior = lambda: print("Squeak")    
    
    def __init__(self, flyBehavior: FlyBehavior, quackBehavior: QuackBehavior) -> None:
        self.flyBehavior = flyBehavior
        self.quackBehavior = quackBehavior
    
    def display(self) -> None:
        print("I'm a rubber duckie")