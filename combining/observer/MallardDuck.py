from Observable import Observable
from Observer import Observer
from Quackable import Quackable


class MallardDuck(Quackable):
    observable: Observable
        
    def __init__(self):
        self.observable = Observable(self)
        
    def quack(self) -> None:
        print("Quack")
        self.notifyObservers()
    
    def registerObserver(self, observer: Observer) -> None:
        self.observable.registerObserver(observer)
        
    def notifyObservers(self) -> None:
        self.observable.notifyObservers()
        
    # toString
    def __str__(self) -> str:
        return "Mallard Duck"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)