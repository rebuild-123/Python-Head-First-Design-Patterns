from typing import List

from Observer import Observer


class Observable:
    def __init__(self):
        self.observers: List[Observer] = []
    
    def setChanged(self):
        pass
    
    def notifyObservers(self, value):
        for observer in self.observers: observer.update(self, value)
            
    def addObserver(self, observer: Observer):
        self.observers.append(observer)