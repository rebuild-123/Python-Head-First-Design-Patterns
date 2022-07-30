from abc import ABC, abstractmethod

from FlyBehavior import FlyBehavior
from QuackBehavior import QuackBehavior


class Duck(ABC):
    flyBehavior: FlyBehavior
    quackBehavior: QuackBehavior
    
    def __init__(self):
        pass
        
    def setFlyBehavior(self, fb: FlyBehavior) -> None:
        self.flyBehavior = fb
        
    def setQuackBehavior(self, qb: QuackBehavior) -> None:
        self.quackBehavior = qb
        
    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError
        
    def performFly(self) -> None:
        self.flyBehavior.fly()
        
    def performQuack(self) -> None:
        self.quackBehavior.quack()
        
    def swim(self) -> None:
        print("All ducks float, even decoys!")