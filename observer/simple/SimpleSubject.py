from typing import List

from Observer import Observer
from Subject import Subject


class SimpleSubject(Subject):
    __observers: List[Observer]
    __value: int = 0
        
    def __init__(self):
        self.__observers = []
    
    def registerObserver(self, o: Observer) -> None:
        self.__observers.append(o)
        
    def removeObserver(self, o: Observer) -> None:
        self.__observers.remove(o)
        
    def notifyObservers(self) -> None:
        for observer in self.__observers:
            observer.update(self.value)
            
    def setValue(self, value: int) -> None:
        self.value = value
        self.notifyObservers()