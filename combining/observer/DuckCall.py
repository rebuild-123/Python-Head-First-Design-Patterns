from Observable import Observable
from Observer import Observer
from Quackable import Quackable


class DuckCall(Quackable):
    observable: Observable
        
    def __init__(self):
        self.observable = Observable(self)
        
    def quack(self) -> None:
        print("Kwak")
        self.notifyObservers()
    
    def registerObserver(self, observer: Observer) -> None:
        self.observable.registerObserver(observer)
        
    def notifyObservers(self) -> None:
        self.observable.notifyObservers()
        
    # toString
    def __str__(self) -> str:
        return "Duck Call"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)