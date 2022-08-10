from Observable import Observable
from Observer import Observer
from Goose import Goose
from Quackable import Quackable


class GooseAdapter(Quackable):
    goose: Goose
    observable: Observable
        
    def __init__(self, goose: Goose):
        self.goose = goose
        self.observable = Observable(self)
        
    def quack(self) -> None:
        self.goose.honk()
        self.notifyObservers()
    
    def registerObserver(self, observer: Observer) -> None:
        self.observable.registerObserver(observer)
        
    def notifyObservers(self) -> None:
        self.observable.notifyObservers()
        
    # toString
    def __str__(self) -> str:
        return "Goose pretending to be a Duck"
    
    # toString for print
    def __repr__(self) -> str:
        return str(self)