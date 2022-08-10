from typing import List

from Observer import Observer
from Quackable import Quackable


class QuackCounter(Quackable):
    duck: Quackable
    numberOfQuacks: List[int] = [0]
        
    def __init__(self, duck: Quackable):
        self.duck = duck
        
    def quack(self) -> None:
        self.duck.quack()
        self.numberOfQuacks[0] += 1
        
    @staticmethod
    def getQuacks() -> int:
        return QuackCounter.numberOfQuacks[0]
    
    def registerObserver(self, observer: Observer) -> None:
        self.duck.registerObserver(observer)
        
    def notifyObservers(self) -> None:
        self.duck.notifyObservers()
        
    # toString
    def __str__(self) -> str:
        return str(self.duck)
    
    # toString for print
    def __repr__(self) -> str:
        return repr(self.duck)