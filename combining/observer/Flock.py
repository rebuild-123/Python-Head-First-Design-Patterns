from typing import Iterator, List

from Observer import Observer
from Quackable import Quackable


class Flock(Quackable):
    ducks: List[Quackable]
        
    def __init__(self):
        self.ducks = []
        
    def add(self, duck: Quackable):
        self.ducks.append(duck)
        
    def quack(self) -> None:
        iterator: Iterator[Quackable] = iter(self.ducks)
        duck: Quackable = next(iterator, None)
        while duck != None:
            duck.quack()
            duck: Quackable = next(iterator, None)
                
    def registerObserver(self, observer: Observer) -> None:
        iterator: Iterator[Quackable] = iter(self.ducks)
        duck: Quackable = next(iterator, None)
        while duck != None:
            duck.registerObserver(observer)
            duck: Quackable = next(iterator, None)
                
    def notifyObservers(self) -> None:
        pass
                
    # toString
    def __str__(self) -> str:
        return "Flock of Ducks"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)