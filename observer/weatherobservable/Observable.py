from abc import ABC, abstractmethod

from Observer import Observer


class Observable(ABC):
    def __init__(self):
        self.observers: List[Observer] = []
    
    def addObserver(self, observer: Observer) -> None:
        self.observers.append(observer)
    
    def setChanged(self) -> None:
        pass
    
    def notifyObservers(self) -> None:
        for observer in self.observers: observer.update(self, None)